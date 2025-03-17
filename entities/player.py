import pygame
import pymunk

import config

from entities.physics_entity import PhysicsEntity
from entities.wall import Wall

class Player(PhysicsEntity):
    def __init__(self, space: pymunk.Space, start_pos: pygame.Vector2 = pygame.Vector2(0, 0)):
        self.moving_left = False
        self.moving_right = False

        # The player's collision box and its position relative to the sprite
        collision_box = pygame.Rect((2, 2), (8, 8))

        # Call constructor of parent class
        PhysicsEntity.__init__(self,
                               space=space,
                               start_pos=start_pos,
                               collision_box=collision_box,
                               mass=1,
                               friction=0.5,
                               body_type=pymunk.Body.DYNAMIC
                           )

    # Inherated from the Entity class
    def update(self):
        # Move the player
        if self.moving_left:
            self.body.apply_force_at_local_point((-config.PLAYER_MOVE_SPEED, 0))
        if self.moving_right:
            self.body.apply_force_at_local_point((config.PLAYER_MOVE_SPEED, 0))

    # Inherated from the Entity class
    def handle_events(self, events):
        for event in events:
            # Handle relevent key presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.moving_left = True
                elif event.key == pygame.K_RIGHT:
                    self.moving_right = True
                elif event.key == pygame.K_SPACE:
                    self.body.apply_impulse_at_local_point((0, -config.PLAYER_JUMP_FORCE))
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.moving_left = False
                elif event.key == pygame.K_RIGHT:
                    self.moving_right = False

    # Inherated from the Entity class
    def load_sprite(self):
        return pygame.image.load('assets/player/player_idle.png').convert_alpha()
