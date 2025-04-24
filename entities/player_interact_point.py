import pygame
import pymunk
from collections.abc import Callable

from entities.sensor_entity import SensorEntity
from entities.arrow import Arrow
from entities.text_box import TextBox
from animation import AnimationPlayer
from custom_events import *

# A point the player can walk up to and press a button to do something.
# e.g. "Press [JUMP] to fix the rocket booster."
class PlayerInteractPoint(SensorEntity):
    def __init__(self,
            space: pymunk.Space,
            font: pygame.font.Font,
            prompt: str,
            max_text_width: int,
            key: int,
            callback: Callable,
            start_pos: pygame.Vector2 = pygame.Vector2(0, 0),
        ):
        self.key = key
        self.prompt = prompt
        self.callback = callback

        collision_box = pygame.Rect(0, 0, 8, 12)

        # The arrow sprite
        self.arrow = Arrow(start_pos)

        # The text box that apears when near the interaction point
        self.text_box = TextBox(prompt, font, max_width=max_text_width, pos=start_pos)

        # In order to properly position the text box, I need to know its size.
        # The text box won't deside what size its sprite is untill after draw is
        # called for the first time.
        self.text_box.draw(pygame.Surface((0, 0)))

        self.text_box.position = pygame.Vector2(
            start_pos.x - (self.text_box.image.get_width() / 2) + (self.arrow.image.get_width() / 2),
            start_pos.y - self.text_box.image.get_height(),
        )

        SensorEntity.__init__(self, space, collision_box, start_pos)

    # Inherated from the Entity class
    def update(self):
        self.text_box.update()

        # Call update function of SensorEntity
        super().update()

    def draw(self, other_surface: pygame.Surface):
        self.arrow.draw(other_surface)

        # Only draw the text box if the player is near the interation point
        if self.is_active:
            self.text_box.draw(other_surface)

    # Inherated from the Entity class
    def load_sprite(self) -> pygame.Surface:
        return self.arrow.load_sprite()

    # Inherated from the Entity class
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                # If the correct key is pressed AND the player is near the interaction point...
                if event.key == self.key and self.is_active:
                    self.callback()

                    # Delete self
                    delete_event = pygame.event.Event(DELETE_ENTITIES_EVENT, {"entities": [self]})
                    pygame.event.post(delete_event)
