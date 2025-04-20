import pygame
import textwrap

from entities.entity import Entity
import utils

# For displaying text in a box. e.g. NPC dialoge
class TextBox(Entity):
    def __init__(self, text: str, font: pygame.font.Font, max_width: int = 99999, start_pos: pygame.Vector2 = pygame.Vector2(0, 0)):
        self.text = text
        self.font = font
        self.max_width = max_width

        self.background_sprite_sheet = pygame.image.load("assets/text_box/text_box.png")

        # Call constructor of parent class
        Entity.__init__(self, start_pos)

    # Inherated from the Entity class
    def draw(self, other_surface: pygame.Surface):
        # TODO: Only call this when the text changes instead of every frame
        self.render_text_box(1, 1)

        other_surface.blit(self.image, self.position)

    def render_text_box(self, border_size, padding):
        # Split text into lines
        lines = textwrap.wrap(self.text, self.max_width)

        # Make an image that is the correct size
        width, height = utils.size_of_text_array(lines, self.font)
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
            line_y = border_size + padding + (i * self.font.get_height())
            
            self.image.blit(rendered_line, (line_x, line_y))
