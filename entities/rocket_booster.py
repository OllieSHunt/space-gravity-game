import pygame

from entities.entity import Entity
from animation import AnimationPlayer

# The rocket booster that the player has to fix in the first mission.
class RocketBooster(Entity):
    # def __init__(self, start_pos: pygame.Vector2 = pygame.Vector2(0, 0)):
    #     Entity.__init__(self, start_pos)

    # Inherated from the Entity class
    def draw(self, other_surface: pygame.Surface):
        # Animation stuff
        self.image = self.anim_player.get_frame()
        self.anim_player.next_if_ready()

        # Call this same meathod in the parent class
        super().draw(other_surface)

    # Inherated from the Entity class
    def load_sprite(self) -> pygame.Surface:
        self.anim_player = AnimationPlayer('assets/rocket_booster', 128)
        self.anim_player.switch_animation("broken_rocket")
        return self.anim_player.get_frame()

    # Switch this rocket booster to a fixed sprite
    def fix(self):
        self.anim_player.switch_animation("fixed_rocket")

    # Switch this rocket booster to an active animation
    def activate(self):
        self.anim_player.switch_animation("active_rocket")
