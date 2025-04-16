import pygame
import os

from entities.entity import Entity
from tile_set import TileSet
import config
import utils

# A collection of tiles.
class TileMap(Entity):
    # This function needs the path to a tile map file and a tile set to render.
    #
    # I am using the Tiled editor to make tile maps: https://www.mapeditor.org/
    #
    # The tile map file should be a group of .csv files exported from the
    # Tiled editor (one .csv file per layer). Aditionaly, when creating the
    # tile map in Tiled, you should use exactly one layer per tile set. This is
    # done to make the importing the tiles easier.
    #
    # The "layers" paramiter is a dictonary containing the paths to the tile
    # sets for each layer. The key is the file name of the layer and the value
    # is the tile set.
    #
    # NOTE: Currently does not support changes to the tile map after creation
    def __init__(self, layers: dict[str, TileSet]):
        self.layers = []

        # Parse all the .csv files one by one
        for file_path, tile_set in layers.items():
            csv_data = utils.parse_csv(file_path)

            # Convert csv_data from a 2D list of str to a 2D list of int
            csv_data = list(map(lambda x: list(map(int, x)), csv_data))

            layer = TileMapLayer(tile_set, csv_data)
            self.layers.append(layer)

        # Call constructor of parent class
        Entity.__init__(self)

    # Inherated from the Entity class
    def load_sprite(self) -> pygame.Surface:
        # Create an image as big as the main screen
        image = pygame.Surface((config.CANVAS_SIZE_X, config.CANVAS_SIZE_Y))
        
        # Draw each layer
        for layer in self.layers:
            layer.draw(image)

        return image

# This class represents one layer in a TileMap
#
# It is not intened to be used directly. You should use TileMap instead.
class TileMapLayer:
    # "layer_data" is a 2d array of tile IDs
    def __init__(self, tile_set: TileSet, layer_data: list[list[int]]):
        self.layer_data = layer_data
        self.tile_set = tile_set

    # Draws this tile map layer onto a pygame surface
    #
    # NOTE: This meathod is not the most efficient, you should avoid calling it
    # too often.
    def draw(self, surface: pygame.Surface):
        # other_surface.blit(self.image, self.position)

        for y, row in enumerate(self.layer_data):
            for x, tile_id in enumerate(row):
                tile_sprite = self.tile_set.get_by_id(tile_id)
                tile_pos = (x * tile_sprite.get_width(), y * tile_sprite.get_height())

                surface.blit(tile_sprite, tile_pos)
