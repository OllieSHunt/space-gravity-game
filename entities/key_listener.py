import pygame
from collections.abc import Callable

from entities.entity import Entity

# This entity triggers a callback when a key is pressed by the user.
class KeyListener(Entity):
    def __init__(self, key_id: int, callback: Callable):
        self.key_id = key_id
        self.callback = callback

        # Call parent constructor
        Entity.__init__(self, (0, 0))

    # Inherited from the Entity class
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == self.key_id:
                self.callback()

    # Inherited from the Entity class
    def draw(self, other_surface: pygame.Surface):
        # Don't draw anything
        pass

    # Inherited from the Entity class
    def load_sprite(self) -> pygame.Surface:
        # This is a timer entity, it should not have a sprite
        return pygame.Surface((0, 0))
