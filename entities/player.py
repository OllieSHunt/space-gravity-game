import pygame
import pymunk

import config

from entities.physics_entity import PhysicsEntity
from entities.wall import Wall

class Player(PhysicsEntity):
    # This is run when the class is first created
    def __init__(self, space: pymunk.Space, start_pos: pygame.Vector2 = pygame.Vector2(0, 0)):
        self.moving_left = False
        self.moving_right = False

        # We need to know the size of the sprite for the PyhsicsEntity constructor.
        # 
        # The load_sprite function is called again during the Entity constructor, but I
        # think that the performance impact from loading the sprite twice is probalby
        # very small.
        rect = self.load_sprite().get_rect()
        rect.x = start_pos.x
        rect.y = start_pos.y

        # Call constructor of parent class
        PhysicsEntity.__init__(self, space, rect, 1, 0.5, pymunk.Body.DYNAMIC)

    # Inherated from the Entity class
    def update(self, entities, events, space):
        # self.body.angle = 0
        # self.body.angular_velocity = 0

        for event in events:
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
        
        if self.moving_left:
            self.body.apply_force_at_local_point((-config.PLAYER_MOVE_SPEED, 0))
        if self.moving_right:
            self.body.apply_force_at_local_point((config.PLAYER_MOVE_SPEED, 0))

    # Inherated from the Entity class
    def load_sprite(self):
        # Create an sprite from a shape
        square = pygame.Surface((4, 4))
        square.fill("white")
        return square.convert()
