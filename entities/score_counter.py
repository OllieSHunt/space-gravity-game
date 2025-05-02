import pygame

from entities.entity import Entity

class ScoreCounter(Entity):
    def __init__(self):
        self.score = 0
        
        Entity.__init__(self, pygame.Vector2(0, 0))

    # Inherated from the Entity class
    def draw(self, other_surface: pygame.Surface):
        # Don't draw anything
        pass

    # Inherated from the Entity class
    def load_sprite(self) -> pygame.Surface:
        # This is invisible, so the surface has a size of 0
        return pygame.Surface((0, 0))
