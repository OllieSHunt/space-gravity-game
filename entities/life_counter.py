import pygame

from entities.entity import Entity

class LifeCounter(Entity):
    def __init__(self, font: pygame.font.Font, pos: pygame.Vector2=pygame.Vector2(0, 0)):
        self.lives = 3
        self.font = font

        Entity.__init__(self, pos)
    
    # Inherated from the Entity class
    def draw(self, other_surface: pygame.Surface):
        # TODO: An icon for each life instead of just text.
        text_surface = self.font.render("Lives: " + str(self.lives), False, "black", "white")
        other_surface.blit(text_surface, (0, 0))
