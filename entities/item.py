import pygame
import pymunk
import random

from entities.sensor_entity import SensorEntity
from animation import AnimationPlayer
from custom_events import *

class Item(SensorEntity):
    def __init__(self, space: pymunk.Space, pos: pygame.Vector2):
        collision_box = pygame.Rect(0, 1, 4, 4)
        SensorEntity.__init__(self, space, collision_box, pos)

    # Inherated from the Entity class
    def draw(self, other_surface: pygame.Surface):
        # Animation stuff
        self.image = self.anim_player.get_frame()
        self.anim_player.next_if_ready()

        # Call this same meathod in the parent class
        super().draw(other_surface)

    # Inherated from the Entity class
    def load_sprite(self) -> pygame.Surface:
        item_types = [
            "cog",
            "spanner",
        ]
        
        # Pick a random animation from this list to play
        self.anim_player = AnimationPlayer('assets/items', 4)
        self.anim_player.switch_animation(random.choice(item_types))
        return self.anim_player.get_frame()

    # Inherated from the SensorEntity class
    def sensor_just_activated(self):
        # Delete this item
        delete_event = pygame.event.Event(DELETE_ENTITIES_EVENT, {"entities": [self]})
        pygame.event.post(delete_event)
