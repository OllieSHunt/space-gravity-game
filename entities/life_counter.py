import pygame

from entities.entity import Entity
import config

class LifeCounter(Entity):
    def __init__(self, font: pygame.font.Font, pos: pygame.Vector2=pygame.Vector2(0, 0)):
        self.font = font

        self.lives = config.PLAYER_LIVES
        self.background_color = "white"

        self.last_blink_time = 0
        self.blink_interval = 250

        Entity.__init__(self, pos)
    
    # Inherated from the Entity class
    def draw(self, other_surface: pygame.Surface):
        # TODO: An icon for each life instead of just text.

        # Blink red if on last life
        if self.lives <= 1 and pygame.time.get_ticks() - self.last_blink_time > self.blink_interval:
            self.last_blink_time = pygame.time.get_ticks()

            # Switch between white and red
            if self.background_color == "white":
                self.background_color = "red"
            elif self.background_color == "red":
                self.background_color = "white"
            else:
                raise Error("Unexpected background color for LifeCounter")

        text_surface = self.font.render("Lives: " + str(self.lives), False, "black", self.background_color)
        other_surface.blit(text_surface, (0, 0))
