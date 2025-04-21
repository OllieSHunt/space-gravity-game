import pymunk
import pygame
from collections.abc import Callable

from entities.entity import Entity
from entities.sensor_entity import SensorEntity
from custom_events import *

# This moves the player to another level when triggered.
class LevelTransition(SensorEntity):
    def __init__(self, level_callback: Callable[[pymunk.Space], list[Entity]], space: pymunk.Space, collision_box: pygame.Rect, start_pos: pygame.Vector2):
        self.level_callback = level_callback

        # Call constructor of parent class
        SensorEntity.__init__(self, space, collision_box, start_pos)

    # Inherated from the Entity class
    def draw(self, other_surface: pygame.Surface):
        # Don't draw anything
        pass

    # Inherated from the Entity class
    def load_sprite(self) -> pygame.Surface:
        # This entity should not have a sprite
        return pygame.Surface((0, 0))

    # Inherated from the SensorEntity class
    def sensor_just_activated(self):
        load_level_event = pygame.event.Event(LOAD_LEVEL_EVENT, {"level_callback": self.level_callback})
        pygame.event.post(load_level_event)
