import pygame
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
    def __init__(self, path: str):
        self.tiled_map = pytmx.util_pygame.load_pygame("assets/tilemaps/test_map.tmx")

        # Call constructor of parent class
        Entity.__init__(self)

    # Inherated from the Entity class
    def draw(self, other_surface: pygame.Surface):
        # Draw each tile in the tile map
        for layer in self.tiled_map:
            for x, y, image in layer.tiles():
                width, height = image.get_rect().size
                other_surface.blit(image, (x * width, y * height))
