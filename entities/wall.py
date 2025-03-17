import pygame
import pymunk

from entities.entity import Entity

class Wall(Entity):
    # This is run when the class is first created
    def __init__(self, space: pymunk.Space, rect: pygame.Rect):
        self.rect = rect
        # Call constructor of parent class
        Entity.__init__(self, pygame.Vector2(rect.x, rect.y))

        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = (self.rect.x + (self.rect.width / 2), self.rect.y + (self.rect.height / 2))
        self.poly = pymunk.Poly.create_box(self.body, size=(self.rect.width, self.rect.height))
        self.poly.mass = 10
        self.poly.friction = 0.8
        space.add(self.body, self.poly)

    def draw(self, other_surface: pygame.Surface):
        # If the wall does not move, then its sprite does not need updating
        # # Update the sprites position
        # self.rect.x = self.body.position.x
        # self.rect.y = self.body.position.y

        super().draw(other_surface)
        
    # Inherated from the Entity class
    def load_sprite(self):
        # Create an sprite from a shape
        square = pygame.Surface((self.rect.width, self.rect.height))
        square.fill("lightgrey")
        return square.convert()