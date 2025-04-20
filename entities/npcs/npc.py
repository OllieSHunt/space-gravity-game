import pygame
import random

from entities.entity import Entity
from animation import AnimationPlayer

# When inherating this class, you need to define the following in the contructor:
#
# self.sprite_folder 
# self.sprite_width 
# self.default_anim
# self.idle_chance 
# self.idle_anims 
#
# See AutoPilotNPC for an example
class NPC(Entity):
    # Inherated from the Entity class
    def update(self):
        self.play_random_idle()

    # Inherated from the Entity class
    def draw(self, other_surface: pygame.Surface):
        # Animation stuff
        self.image = self.anim_player.get_frame()
        self.anim_player.next_if_ready()

        # Call this same meathod in the parent class
        super().draw(other_surface)

    # Inherated from the Entity class
    def load_sprite(self) -> pygame.Surface:
        self.anim_player = AnimationPlayer(self.sprite_folder, self.sprite_width)
        self.anim_player.switch_animation(self.default_anim)
        return self.anim_player.get_frame()

    # This has a chance of playing a random one-off idle animation.
    # e.g. blinking, yawning, etc...
    def play_random_idle(self):
        # Only do idle animations when the player is in the idle state
        if self.anim_player.current_anim == self.default_anim:
            # Deside whether to play an idle animation or not
            if random.randint(0, self.idle_chance) == 0:
                # Choose and swith to a random idle animation
                anim = random.choice(self.idle_anims)
                self.anim_player.switch_animation(anim, self.default_anim)
