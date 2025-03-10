import pygame

from entities.entity import Entity

class Wall(Entity):
    # This is run when the class is first created
    def __init__(self, rect: pygame.Rect):
        self.rect = rect
        
        # Call constructor of parent class
        Entity.__init__(self, pygame.Vector2(rect.x, rect.y))
        
    # Inherated from the Entity class
    def load_sprite(self):
        # Create an sprite from a shape
        square = pygame.Surface((self.rect.width, self.rect.height))
        square.fill("lightgrey")
        return square.convert()