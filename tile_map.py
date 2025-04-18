import pygame
import pymunk
import pymunk.autogeometry
import pytmx
from random import random
import shapely
import os

from entities.entity import Entity
import config
import utils

# A collection of tiles.
class TileMap(Entity):
    # This function needs the path to a tile map file.
    # 
    # The file must be a .tmx from the Tiled editor: https://www.mapeditor.org/
    #
    # NOTE: Tile maps do not currently support having their tiles changed after creation
    def __init__(self, space: pymunk.Space, path: str):
        self.tiled_map = pytmx.util_pygame.load_pygame(path)

        self.load_collision_shapes(space)

        # Call constructor of parent class
        Entity.__init__(self)

    # Inherated from the Entity class
    def load_sprite(self) -> pygame.Surface:
        # Create an empty surface
        surface = pygame.Surface((
            self.tiled_map.width * self.tiled_map.tilewidth,
            self.tiled_map.height * self.tiled_map.tileheight
        ), pygame.SRCALPHA)

        # Draw each tile in the tile map
        for layer in self.tiled_map:
            for x, y, image in layer.tiles():
                surface.blit(image, (x * self.tiled_map.tilewidth, y * self.tiled_map.tileheight))

        return surface

    # Creates colliders for this tile map in the pymunk Space
    #
    # WARNING: This function is *very* inefficint and should be run as little as
    # possible.
    def load_collision_shapes(self, space: pymunk.Space):
        # TODO: make tiles all one polygon to avoid odd player jumping behaviour and also performance
        
        # Create a physics body for this tile map
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        space.add(body)

        polys = []
        
        # Get collider shapes for each tile
        for gid, colliders in self.tiled_map.get_tile_colliders():
            # Find the all the places there is an instance of this tile
            for x, y, z in self.tiled_map.get_tile_locations_by_gid(gid):
                # For each of this tiles colliders...
                for collider in colliders:
                    collider_offset = (
                        x * self.tiled_map.tilewidth,
                        y * self.tiled_map.tileheight
                    )

                    # Get the polygon for this collilder and offset it by the offset
                    poly = list(map(lambda pos: (pos[0] + collider_offset[0], pos[1] + collider_offset[1]), collider.apply_transformations()))

                    # Convert to a shapely polygon and add to this list
                    poly = shapely.Polygon(poly)
                    polys.append(poly)

        # Combine all the collision shapes
        union = shapely.union_all(polys)

        for poly in union.geoms:
            points = list(poly.exterior.coords)
            points.reverse()

            for polyline in pymunk.autogeometry.convex_decomposition(points, 0.5):
                print(polyline)
                pymunk_poly = pymunk.Poly(body, polyline)
                # Set this polygon's debug colour to something random
                pymunk_poly.color = pygame.Color(int(random() * 255), int(random() * 255), int(random() * 255))
                space.add(pymunk_poly)
