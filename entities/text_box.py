import pygame
import textwrap

from entities.entity import Entity
from custom_events import *
import utils

# For displaying text in a box. e.g. NPC dialoge
#
# This can display some constant text, or switch texts after a delay. When
# there is not more text to show, it will delete itself.
class TextBox(Entity):
    def __init__(self,
                text: list[str] | str,
                font: pygame.font.Font,
                delay: int=None,
                max_width: int = 99999,
                pos: pygame.Vector2 = pygame.Vector2(0, 0)
            ):
        self.font = font
        self.max_width = max_width

        self.delay = delay
        self.timer_last_tick = pygame.time.get_ticks()

        # all_texts will be set if this box should scroll between several texts
        self.all_texts = None
        self.current_text = 0

        self.last_frame_text = "" # This is used for change detection

        # Check if one string was passed or a list of strings
        if isinstance(text, str):
            self.text = text
        else: # Not a str, must be a list[str]
            self.all_texts = text
            self.text = text[self.current_text]

        # Call constructor of parent class
        Entity.__init__(self, pos)

    # Inherated from the Entity class
    def update(self):
        # If the text box should change after some time
        if self.delay != None:
            time = pygame.time.get_ticks()
            elapsed = time - self.timer_last_tick

            if elapsed >= self.delay:
                # If there are other texts to show
                if self.all_texts != None:
                    self.timer_last_tick = pygame.time.get_ticks()

                    self.current_text += 1

                    if self.current_text < len(self.all_texts):
                        # Show the next piece of text
                        self.text = self.all_texts[self.current_text]
                    else:
                        # Delete this entity
                        delete_event = pygame.event.Event(DELETE_ENTITIES_EVENT, {"entities": [self]})
                        pygame.event.post(delete_event)
                else:
                    # Delete this entity
                    delete_event = pygame.event.Event(DELETE_ENTITIES_EVENT, {"entities": [self]})
                    pygame.event.post(delete_event)

    # Inherated from the Entity class
    def draw(self, other_surface: pygame.Surface):
        # Only re-render the text when the text changes
        if self.text != self.last_frame_text:
            self.last_frame_text = self.text
            self.render_text_box(1, 1, -2)

        other_surface.blit(self.image, self.position)

    # Inherated from the Entity class
    def load_sprite(self) -> pygame.Surface:
        return pygame.Surface((0, 0))

    def render_text_box(self, border_size, padding, line_spaceing):
        # Split text into lines
        lines = textwrap.wrap(self.text, self.max_width)

        # Make an image that is the correct size
        width, height = utils.size_of_text_array(lines, line_spaceing, self.font)
        width += (border_size * 2) + (padding * 2)
        height += (border_size * 2) + (padding * 2)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)

        # Text background and border
        self.image.fill(pygame.color.Color("black"))
        self.image.fill(pygame.color.Color("white"), (
            (border_size, border_size),
            (width - (border_size * 2), height - (border_size * 2)),
        ))

        # Draw each line
        for i, line in enumerate(lines):
            rendered_line = self.font.render(line, False, pygame.color.Color("black"))
            line_x = border_size + padding
            line_y = (border_size + padding + (i * (self.font.get_height() + line_spaceing))) + line_spaceing
            
            self.image.blit(rendered_line, (line_x, line_y))
