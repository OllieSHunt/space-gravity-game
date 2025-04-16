import pygame
import pymunk
import pytmx
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
        self.tiled_map = pytmx.util_pygame.load_pygame("assets/tilemaps/test_map.tmx")

        self.load_collision_shapes(space)

        # Call constructor of parent class
        Entity.__init__(self)

    # Inherated from the Entity class
    def load_sprite(self) -> pygame.Surface:
        surface = pygame.Surface((config.CANVAS_SIZE_X, config.CANVAS_SIZE_Y))

        # Draw each tile in the tile map
        for layer in self.tiled_map:
            for x, y, image in layer.tiles():
                width, height = image.get_rect().size
                surface.blit(image, (x * width, y * height))

        return surface

    # Creates colliders for this tile map in the pymunk Space
    #
    # WARNING: This function is *very* inefficint and should be run as little as
    # possible.
    def load_collision_shapes(self, space: pymunk.Space):
        # Create a physics body for this tile map
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        space.add(body)
        
        # Get collider shapes for each tile
        for gid, colliders in self.tiled_map.get_tile_colliders():
            tile = self.tiled_map.get_tile_properties_by_gid(gid)
            width = tile["width"]
            height = tile["height"]

            # Find the all the places there is an instance of this tile
            for x, y, z in self.tiled_map.get_tile_locations_by_gid(gid):
                # For each of this tiles colliders...
                for collider in colliders:
                    # Create a polygon for this collider and add it to the pymunk Space
                    poly = pymunk.Poly(
                                       body,
                                       vertices=collider.apply_transformations(),
                                       transform=pymunk.Transform.translation(x * width, y * height),
                                   )
                    space.add(poly)
