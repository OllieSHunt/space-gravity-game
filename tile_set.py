import csv
import pygame

# This class represents a set of tiles that can be built up into a tile map.
class TileSet:
    # Takes a path to the sprite sheet for this tile set.
    #
    # This expects the sprite sheet to be in a specific format.
    # See `/home/ollie/code/space-gravity-game/assets/tilesets/template_tileset.png`
    def __init__(self, sprite_sheet: str, tile_width: int, tile_height: int):
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.sprite_sheet = pygame.image.load(sprite_sheet).convert_alpha()
        self.tiles = []

        sheet_width = self.sprite_sheet.get_width() / self.tile_width
        sheet_height = self.sprite_sheet.get_height() / self.tile_height

        if not sheet_width.is_integer() or not sheet_height.is_integer():
            raise Exception("Tile size not divisible by the sprite sheet size")

        # Convert sheet width and height from floats to intagers
        sheet_width = int(sheet_width)
        sheet_height = int(sheet_height)

        # Split the sprite sheet up into tiles (using pygame subsurfaces)
        for x in range(0, sheet_width):
            for y in range(0, sheet_height):
                # Work out where this tile is in the sprite sheet
                subsurface_rect = pygame.Rect(
                    x * tile_width,
                    y * tile_height,
                    self.tile_width,
                    self.tile_height,
                )

                # Fetch the tile from the sprite sheet
                self.tiles.append(self.sprite_sheet.subsurface(subsurface_rect))

    # Takes an ID and returns a pygame subsurface of a tile matching this ID
    def get_by_id(self, id: int):
        id += 1
        return self.tiles[id]
