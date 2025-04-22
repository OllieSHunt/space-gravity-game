import pygame

from entities.wall import Wall

# A wall but without a texture
class InvisibleWall(Wall):
    # Inherated from the Entity class
    def load_sprite(self) -> pygame.Surface:
        # This wall is invisible, so the surface has a size of 0
        return pygame.Surface((0, 0))
