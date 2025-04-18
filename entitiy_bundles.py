import pygame
import pymunk

from entities.player import Player
from entities.wall import Wall
from entities.gravity_button import GravityButton
from tile_map import TileMap
import config

def level_1(space: pymunk.Space):
    # Set gravity
    space.gravity = (0, config.GRAVITY_STRENGTH)

    # Spawn entities
    return [
        Player(space, start_pos=pygame.Vector2(20, 0)),
        GravityButton(space, start_pos=pygame.Vector2(15, 19), rotation=270),
        TileMap(space, "assets/tilemaps/level1.tmx"),
    ]
