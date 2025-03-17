import pygame
import pymunk

from entities.physics_entity import PhysicsEntity

class Wall(PhysicsEntity):
    def __init__(self, space: pymunk.Space, rect: pygame.Rect):
        # Call constructor of parent class
        PhysicsEntity.__init__(self, space, rect, 1, 0.8, pymunk.Body.STATIC)
        
    # Inherated from the Entity class
    def load_sprite(self):
        # Create the sprite based of the size of the physics body
        square = pygame.Surface(self.get_size())
        square.fill("lightgrey")
        return square.convert_alpha()
