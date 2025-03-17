import pygame
import pymunk

import config

from entities.entity import Entity
from entities.wall import Wall

class Player(Entity):
    # This is run when the class is first created
    def __init__(self, space: pymunk.Space, start_pos: pygame.Vector2 = pygame.Vector2(0, 0)):
        # Call constructor of parent class
        Entity.__init__(self, start_pos)

        # Set up physics stuff using pymunk
        self.body = pymunk.Body()
        self.body.position = (start_pos.x + (self.rect.width / 2), start_pos.y + (self.rect.height / 2))
        self.poly = pymunk.Poly.create_box(self.body, size=(self.rect.width, self.rect.height))
        self.poly.mass = 1
        self.poly.friction = 0.5
        space.add(self.body, self.poly)

        self.moving_left = False
        self.moving_right = False

    # Inherated from the Entity class
    def update(self, entities, events, space):
        self.body.angle = 0
        self.body.angular_velocity = 0

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

    def draw(self, other_surface: pygame.Surface):
        # Update the sprites position
        self.rect.x = self.body.position.x - (self.rect.width / 2)
        self.rect.y = self.body.position.y - (self.rect.height / 2)
        

        super().draw(other_surface)

    # Inherated from the Entity class
    def load_sprite(self):
        # Create an sprite from a shape
        square = pygame.Surface((4, 4))
        square.fill("white")
        return square.convert()