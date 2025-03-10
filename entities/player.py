import pygame

from entities.entity import Entity

class Player(Entity):
    # This is run when the class is first created
    def __init__(self, start_pos: pygame.Vector2 = pygame.Vector2(0, 0)):
        # Call constructor of parent class
        Entity.__init__(self, start_pos)

    # Inherated from the Entity class
    def update(self, entities, events):
        pass

    # Inherated from the Entity class
    def load_sprite(self):
        # Create an sprite from a shape
        square = pygame.Surface((4, 4))
        square.fill("white")
        return square.convert()