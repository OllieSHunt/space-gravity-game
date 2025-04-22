import pygame
import pymunk

from entities.player import Player
from entities.wall import Wall
from entities.gravity_button import GravityButton
from entities.electric_hazard import ElectricHazard
from entities.npcs.autopilot import AutoPilotNPC
from entities.text_box import TextBox
from entities.timer import TimerEntity
from entities.background import StarBackground
from entities.arrow import Arrow
from entities.level_transition import LevelTransition
from tile_map import TileMap
from custom_events import *
import config

def level_1(space: pymunk.Space):
    # Set gravity
    space.gravity = (0, config.GRAVITY_STRENGTH)

    # Spawn entities
    return [
        StarBackground(),
        TileMap(space, "assets/tilemaps/level1.tmx"),
        AutoPilotNPC(pygame.Vector2(49, 75)),

        LevelTransition(level_2, space, pygame.Rect(0, 0, 8, 20), pygame.Vector2(config.CANVAS_SIZE_X + 4, 56)),

        GravityButton(space, pygame.Vector2(80, 98), 270),

        # Wait a few seconds before spawning the player
        TimerEntity(lambda: pygame.event.post(pygame.event.Event(SPAWN_ENTITIES_EVENT, {"entities": [
            Player(space, pygame.Vector2(163, -100)),
        ]})), 2000),

        # Spawn dialogue for the autopilot after a delay
        TimerEntity(lambda: pygame.event.post(pygame.event.Event(SPAWN_ENTITIES_EVENT, {"entities": [
            TextBox([
                "Oh!",
                "Hello there robot 3742.",
                "...",
                "As you're here, could you do me a favour?",
                "As you can see, we're moving rather slowly at the moment.",
                "This is due to a malfunctioning thruster.",
                "Do you think you could fix it for me?",
                "Our pasengers are counting on you so please hurry.",
                "...",
            ], config.font, 5000, 30, (40, 110)),

            # Nested timer to add pauses
            TimerEntity(lambda: pygame.event.post(pygame.event.Event(SPAWN_ENTITIES_EVENT, {"entities": [
                TextBox([
                    "You may need to use these blue gravity buttons to assist you.",
                    "I'm sure the pasengers won't mind a few switches in gravity...",
                    "...as long as you don't do it too offten.",
                ], config.font, 5000, 30, (40, 110)),

                # Spawn arrow pointing at gravity button
                Arrow(pygame.Vector2(74, 86)),

                # Nested timer to add pauses
                TimerEntity(lambda: pygame.event.post(pygame.event.Event(SPAWN_ENTITIES_EVENT, {"entities": [
                    TextBox([
                        "Oh, and one more thing...",
                        "Don't forget about your magnet atachment!",
                        "You can activate it by pressing [ENTER]",
                    ], config.font, 5000, 30, (40, 110)),

                    # Give the player another prompt if they are stuck
                    TimerEntity(lambda: pygame.event.post(pygame.event.Event(SPAWN_ENTITIES_EVENT, {"entities": [
                        TextBox([
                            "You're still here?",
                            "Remember, our pasengers are counting on you!",
                            "You can use [ENTER] to toggle your magnet...",
                            "...and toggle gravity using these blue buttons.",
                            "Please hurry and fix the thruster.",
                        ], config.font, 5000, 30, (40, 110))
                    ]})), 120000),
                ]})), 18000),
            ]})), 45000),
        ]})), 4000),
    ]

def level_2(space: pymunk.Space):
    # Spawn entities
    return [
        StarBackground(),
        TileMap(space, "assets/tilemaps/level2.tmx"),

        # LevelTransition(level_3, space, pygame.Rect(0, 0, 20, 8), pygame.Vector2(228, config.CANVAS_SIZE_Y + 4)),

        Player(space, pygame.Vector2(0, 68)),
    ]
