import math
import pygame
import pymunk

import config

from entities.sensor_entity import SensorEntity
from animation import AnimationPlayer

class GravityButton(SensorEntity):
    def __init__(self, space: pymunk.Space, start_pos: pygame.Vector2 = pygame.Vector2(0, 0), rotation=0):
        # The collision box and its position relative to the sprite
        collision_box = pygame.Rect((0, 1), (3, 6))

        # Call constructor of parent class
        SensorEntity.__init__(self, space, collision_box, start_pos)

        self.body.angle = math.radians(rotation)

    # Inherated from the Entity class
    def update(self):
        # Call this same meathod in the parent class
        super().update()

    # Inherated from the Entity class
    def draw(self, other_surface: pygame.Surface):
        # Animation stuff
        if self.anim_player.next_if_ready():
            self.image = self.anim_player.get_frame()

        # Call this same meathod in the parent class
        super().draw(other_surface)

    # Inherated from the Entity class
    def load_sprite(self):
        self.anim_player = AnimationPlayer('assets/physics_button', 4)
        self.anim_player.swith_animation("physics_button_idle")
        return self.anim_player.get_frame()

    # Inherated from the SensorEntity class
    def sensor_just_activated(self):
        self.anim_player.swith_animation("physics_button_pressed")

        space = self.poly.space

        # Toggle gravity
        if space.gravity.length == 0:
            space.gravity = (0, config.GRAVITY_STRENGTH)
        else:
            space.gravity = (0, 0)

    # Inherated from the SensorEntity class
    def sensor_just_deactivated(self):
        self.anim_player.swith_animation("physics_button_idle")
