import pygame

import config

from entities.entity import Entity
from entities.wall import Wall

class Player(Entity):
    # This is run when the class is first created
    def __init__(self, start_pos: pygame.Vector2 = pygame.Vector2(0, 0)):
        self.velocity = pygame.Vector2()
        self.gravity = True
    
        # Call constructor of parent class
        Entity.__init__(self, start_pos)

    # Inherated from the Entity class
    def update(self, entities, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.velocity.x -= config.PLAYER_MOVE_SPEED
                elif event.key == pygame.K_RIGHT:
                    self.velocity.x += config.PLAYER_MOVE_SPEED
                elif event.key == pygame.K_SPACE:
                    self.velocity.y -= config.PLAYER_JUMP_FORCE
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.velocity.x += config.PLAYER_MOVE_SPEED
                elif event.key == pygame.K_RIGHT:
                    self.velocity.x -= config.PLAYER_MOVE_SPEED
        
        # Apply gravity
        if self.gravity:
            self.velocity.y += config.GRAVITY_STRENGTH
        
        # Stop the player from going throug walls
        for entity in entities:
            # Move player to see if they will collide with the other entity
            #posible_position = self.rect.position
            #posible_position.x += config.PLAYER_MOVE_SPEED
        
            # If other entity is not self AND other is of type wall AND rects overlap
            if entity != self and isinstance(entity, Wall) and self.rect.colliderect(entity.rect):
                print("Collision!")
        
        # Update the play's position based on the current velocity
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

    # Inherated from the Entity class
    def load_sprite(self):
        # Create an sprite from a shape
        square = pygame.Surface((4, 4))
        square.fill("white")
        return square.convert()