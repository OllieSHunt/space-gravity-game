import pygame
import pymunk

from entities.player import Player
from entities.wall import Wall
from entities.gravity_button import GravityButton

def level_1(space: pymunk.Space):
    return [
        Player(space, start_pos=pygame.Vector2(20, 0)),
        Wall(space, pygame.Rect(0, 45, 70, 5)),
        Wall(space, pygame.Rect(0, 0, 5, 100)),
        Wall(space, pygame.Rect(65, 0, 5, 100)),
        Wall(space, pygame.Rect(0, 25, 40, 5)),
        Wall(space, pygame.Rect(0, 0, 70, 1)),
        GravityButton(space, start_pos=pygame.Vector2(15, 19), rotation=270),
    ]