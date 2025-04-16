import pygame
import os

from tile_set import TileSet
import utils

# A collection of tiles.
# See tile_set.py
class TileMap:
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

# This class represents one layer in a TileMap
#
# It is not intened to be used directly. You should use TileMap instead.
class TileMapLayer:
    # "layer_data" is a 2d array of tile IDs
    def __init__(self, tile_set: TileSet, layer_data: list[list[int]]):
        self.layer_data = layer_data
        self.tile_set = tile_set

        # TEMP
        print(self.layer_data[0])
        print(self.tile_set)
        print("")
