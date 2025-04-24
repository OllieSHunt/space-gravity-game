import pygame
import pymunk

from entities.player import Player
from entities.wall import Wall
from entities.invisible_wall import InvisibleWall
from entities.gravity_button import GravityButton
from entities.electric_hazard import ElectricHazard
from entities.npcs.autopilot import AutoPilotNPC
from entities.text_box import TextBox
from entities.timer import TimerEntity
from entities.background import StarBackground
from entities.arrow import Arrow
from entities.level_transition import LevelTransition
from entities.hazzard_box import HazardBox
from entities.rocket_booster import RocketBooster
from entities.player_interact_point import PlayerInteractPoint
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

        # Invisable walls before the start of the level
        InvisibleWall(space, pygame.Rect(152, -130, 8, 130)),
        InvisibleWall(space, pygame.Rect(176, -130, 8, 130)),
        InvisibleWall(space, pygame.Rect(152, -130, 32, 8)),

        LevelTransition(level_2, space, pygame.Rect(0, 0, 8, 24), pygame.Vector2(config.CANVAS_SIZE_X + 4, 56)),

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

        # Invisable wall at the start of the level
        InvisibleWall(space, pygame.Rect(-12, 56, 8, 24)),

        LevelTransition(level_3, space, pygame.Rect(0, 0, 20, 8), pygame.Vector2(228, config.CANVAS_SIZE_Y + 4)),

        Player(space, pygame.Vector2(0, 68)),
    ]

def level_3(space: pymunk.Space):
    # Spawn entities
    return [
        StarBackground(),
        TileMap(space, "assets/tilemaps/level3.tmx"),

        # Invisable walls before the start of the level
        InvisibleWall(space, pygame.Rect(224, -130, 8, 130)),
        InvisibleWall(space, pygame.Rect(244, -130, 8, 130)),
        InvisibleWall(space, pygame.Rect(224, -130, 24, 8)),

        # These hazards are in the order you find them in the level

        ElectricHazard(space, pygame.Vector2(206, 16), 90, pygame.Vector2(206, 36), 4700),
        ElectricHazard(space, pygame.Vector2(206, 36), 270),

        ElectricHazard(space, pygame.Vector2(181, 24), 90, pygame.Vector2(181, 44), 4200),
        ElectricHazard(space, pygame.Vector2(181, 44), 270),

        GravityButton(space, pygame.Vector2(119, 114), 270),

        ElectricHazard(space, pygame.Vector2(124, 80), 180, pygame.Vector2(104, 96), 4000),
        ElectricHazard(space, pygame.Vector2(104, 96), 0),

        ElectricHazard(space, pygame.Vector2(124, 60), 180, pygame.Vector2(104, 76), 4500),
        ElectricHazard(space, pygame.Vector2(104, 76), 0),

        GravityButton(space, pygame.Vector2(84, 66), 270),

        LevelTransition(level_4, space, pygame.Rect(0, 0, 32, 8), pygame.Vector2(32, config.CANVAS_SIZE_Y + 4)),

        Player(space, pygame.Vector2(231, -100)),
    ]

def level_4(space: pymunk.Space):
    # Spawn entities
    return [
        StarBackground(),
        TileMap(space, "assets/tilemaps/level4.tmx"),

        # Invisable walls before the start of the level
        InvisibleWall(space, pygame.Rect(24, -130, 8, 130)),
        InvisibleWall(space, pygame.Rect(56, -130, 8, 130)),
        InvisibleWall(space, pygame.Rect(24, -130, 40, 8)),

        GravityButton(space, pygame.Vector2(28, 102), 270),
        GravityButton(space, pygame.Vector2(208, 60), 90),
        GravityButton(space, pygame.Vector2(272, 90), 270),

        ElectricHazard(space, pygame.Vector2(191, 55), 225, pygame.Vector2(136, 24), 5000),
        ElectricHazard(space, pygame.Vector2(136, 24), 90),

        ElectricHazard(space, pygame.Vector2(196, 46), 180, pygame.Vector2(76, 32), 4500),
        ElectricHazard(space, pygame.Vector2(76, 32), 45),

        # This kills the player if they fall into the bottomless pit
        HazardBox(space, pygame.Rect(0, config.CANVAS_SIZE_Y + 100, config.CANVAS_SIZE_X, 16)),
        InvisibleWall(space, pygame.Rect(0, config.CANVAS_SIZE_Y, 32, 120)),
        InvisibleWall(space, pygame.Rect(216, config.CANVAS_SIZE_Y, 32, 120)),

        LevelTransition(level_5, space, pygame.Rect(0, 0, 8, 22), pygame.Vector2(config.CANVAS_SIZE_X + 4, 76)),

        Player(space, pygame.Vector2(40, -100)),
    ]

def level_5(space: pymunk.Space):
    rocket_booster = RocketBooster(pygame.Vector2(24, 12))

    # Spawn entities
    return [
        StarBackground(),
        rocket_booster,
        TileMap(space, "assets/tilemaps/level5.tmx"),

        # Invisable wall at the start of the level
        InvisibleWall(space, pygame.Rect(-12, 76, 8, 24)),

        Player(space, pygame.Vector2(0, 88)),

        # Nested interaction points to create a small minigame
        PlayerInteractPoint(
            space,
            config.font,
            "Press [f] to fix",
            999,
            pygame.K_f,
            lambda: pygame.event.post(pygame.event.Event(SPAWN_ENTITIES_EVENT, {"entities": [
                TimerEntity(rocket_booster.mostly_fix, 0),
                PlayerInteractPoint(
                    space,
                    config.font,
                    "Press [f] to fix",
                    999,
                    pygame.K_f,
                    lambda: pygame.event.post(pygame.event.Event(SPAWN_ENTITIES_EVENT, {"entities": [
                        TimerEntity(rocket_booster.fix, 0),
                        PlayerInteractPoint(
                            space,
                            config.font,
                            "Press [f] to fix",
                            999,
                            pygame.K_f,
                            rocket_booster.activate,
                            pygame.Vector2(53, 70)
                        ),
                    ]})),
                    pygame.Vector2(24, 82)
                ),
            ]})),
            pygame.Vector2(44, 74)
        ),
    ]
