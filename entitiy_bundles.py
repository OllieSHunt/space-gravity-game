import pygame
import pymunk

from entities.player import Player
from entities.wall import Wall
from entities.gravity_button import GravityButton
from entities.electric_hazard import ElectricHazard
from tile_map import TileMap
import config

def level_1(space: pymunk.Space):
    # Set gravity
    space.gravity = (0, config.GRAVITY_STRENGTH)

    # Spawn entities
    return [
        Player(space, pygame.Vector2(20, 0)),
        GravityButton(space, pygame.Vector2(16, 58), 270),
        ElectricHazard(space, pygame.Vector2(52, 72), 90, pygame.Vector2(100, 136), 4000),
        ElectricHazard(space, pygame.Vector2(100, 136), 270),
        TileMap(space, "assets/tilemaps/level1.tmx"),
    ]
