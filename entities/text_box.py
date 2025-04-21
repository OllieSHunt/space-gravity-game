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
        self.border_size = 1
        self.padding = 1
        self.line_spaceing = -2

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

            # Work out the size of this textbox
            lines = textwrap.wrap(self.text, self.max_width)
            self.width, self.height = utils.size_of_text_array(lines, self.line_spaceing, self.font)

        else: # Not a str, must be a list[str]
            self.all_texts = text
            self.text = text[self.current_text]

            # Work out the size of this textbox
            self.width, self.height = 0, 0
            for each_text in self.all_texts:
                lines = textwrap.wrap(each_text, self.max_width)
                width, height = utils.size_of_text_array(lines, self.line_spaceing, self.font)

                if width > self.width:
                    self.width = width
                if height > self.height:
                    self.height = height

        # Account for border and padding in the textbox size
        self.width += (self.border_size * 2) + (self.padding * 2)
        self.height += (self.border_size * 2) + (self.padding * 2)

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
            self.render_text_box()

        other_surface.blit(self.image, self.position)

    # Inherated from the Entity class
    def load_sprite(self) -> pygame.Surface:
        return pygame.Surface((0, 0))

    # This resets self.image to be a blank, text box
    def clear_textbox(self):
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

        # Text background and border
        self.image.fill(pygame.color.Color("black"))
        self.image.fill(pygame.color.Color("white"), (
            (self.border_size, self.border_size),
            (self.width - (self.border_size * 2), self.height - (self.border_size * 2)),
        ))

    def render_text_box(self):
        self.clear_textbox()

        # Split text into lines
        lines = textwrap.wrap(self.text, self.max_width)

        # Draw each line
        for i, line in enumerate(lines):
            rendered_line = self.font.render(line, False, pygame.color.Color("black"))
            line_x = (self.border_size + self.padding) + (((self.image.get_width() - (self.border_size + self.padding)) / 2) - (rendered_line.get_width() / 2))
            line_y = ((self.border_size + self.padding + (i * (self.font.get_height() + self.line_spaceing))) + self.line_spaceing)
            
            self.image.blit(rendered_line, (line_x, line_y))
