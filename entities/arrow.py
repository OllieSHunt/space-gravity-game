import pygame

from entities.entity import Entity
from animation import AnimationPlayer

# For pointing at stuff
class Arrow(Entity):
    # Inherated from the Entity class
    def draw(self, other_surface: pygame.Surface):
        # Animation stuff
        self.image = self.anim_player.get_frame()
        self.anim_player.next_if_ready()

        # Call this same meathod in the parent class
        super().draw(other_surface)

    # Inherated from the Entity class
    def load_sprite(self) -> pygame.Surface:
        self.anim_player = AnimationPlayer('assets/arrow', 8)
        self.anim_player.switch_animation("arrow_down")
        return self.anim_player.get_frame()
