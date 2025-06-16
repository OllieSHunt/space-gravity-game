import pygame

from entities.text_box import TextBox
import config

class LifeCounter(TextBox):
    def __init__(self, font: pygame.font.Font):
        self.lives = config.PLAYER_LIVES

        # This keeps track of what the lives counter said last frame.
        self.prev_lives = self.lives

        # Parent's constructor
        TextBox.__init__(self,
            text = "Lives: " + str(self.lives) + " ",
            font = font,
            pos = pygame.Vector2(239, -2),
        )    

    # Inherated from the Entity class
    def draw(self, other_surface: pygame.Surface):
        # Only update text if something has changed
        if self.lives != self.prev_lives:
            self.text = "Lives: " + str(self.lives) + " "

            # Flash red if only one life left
            if self.lives <= 1:
                self.is_flashing = True

        self.prev_lives = self.lives

        # Call this same function in the parent class
        super().draw(other_surface)
