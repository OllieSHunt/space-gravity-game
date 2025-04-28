import pygame

from entities.entity import Entity

class ScoreCounter(Entity):
    def __init__(self):
        self.score = 0
        
        Entity.__init__(self, pygame.Vector2(0, 0))
