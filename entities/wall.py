import pygame
import pymunk

from entities.physics_entity import PhysicsEntity

class Wall(PhysicsEntity):
    # This is run when the class is first created
    def __init__(self, space: pymunk.Space, rect: pygame.Rect):
        # Call constructor of parent class
        PhysicsEntity.__init__(self, space, rect, 1, 0.8, pymunk.Body.STATIC)
        
    # Inherated from the Entity class
    def load_sprite(self):
        # Create an sprite from a shape
        square = pygame.Surface((self.rect.width, self.rect.height))
        square.fill("lightgrey")
        return square.convert()
