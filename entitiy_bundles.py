import pygame
import pymunk

from entities.player import Player
from entities.wall import Wall
from entities.gravity_button import GravityButton
from entities.electric_hazard import ElectricHazard
from entities.npcs.autopilot import AutoPilotNPC
from entities.text_box import TextBox
from tile_map import TileMap
import config

def level_1(space: pymunk.Space):
    # Set gravity
    space.gravity = (0, config.GRAVITY_STRENGTH)

    # Spawn entities
    return [
        TileMap(space, "assets/tilemaps/level1.tmx"),
        Player(space, pygame.Vector2(20, 0)),
        ElectricHazard(space, pygame.Vector2(7, 64), 90, pygame.Vector2(7, 120), 4000),
        ElectricHazard(space, pygame.Vector2(7, 120), 270),
        GravityButton(space, pygame.Vector2(185, 142), 270),
        GravityButton(space, pygame.Vector2(177, 100), 90),
        GravityButton(space, pygame.Vector2(100, 142), 270),
        AutoPilotNPC(pygame.Vector2(119, 119)),
        TextBox("I am a text box. At the time of writing this string, I am not actualy a text box yet. But soon I will be a text box. At the moment I am just a string in a text editor.", config.font, 30, pygame.Vector2(50, 50)),
    ]
