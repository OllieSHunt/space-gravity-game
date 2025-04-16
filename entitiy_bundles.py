import pygame
import pymunk

from entities.player import Player
from entities.wall import Wall
from entities.gravity_button import GravityButton
import tile_set
import tile_map


def level_1(space: pymunk.Space):
    tile_set1 = tile_set.TileSet("assets/tilesets/template_tileset.png", 4, 4)
    tile_set2 = tile_set.TileSet("assets/tilesets/ship_tileset.png", 4, 4)

    tiles = tile_map.TileMap({
        "assets/tilemaps/test_map/test_map_Tile Layer 1.csv": tile_set1,
        "assets/tilemaps/test_map/test_map_test.csv": tile_set2,
    })

    return [
        tiles,
        Player(space, start_pos=pygame.Vector2(20, 0)),
        GravityButton(space, start_pos=pygame.Vector2(15, 19), rotation=270),
        # Wall(space, pygame.Rect(0, 45, 70, 5)),
        # Wall(space, pygame.Rect(0, 0, 5, 100)),
        # Wall(space, pygame.Rect(65, 0, 5, 100)),
        # Wall(space, pygame.Rect(0, 25, 40, 5)),
        # Wall(space, pygame.Rect(0, 0, 70, 1)),
    ]
