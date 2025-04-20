import pygame

from entities.npcs.npc import NPC
from animation import AnimationPlayer

class AutoPilotNPC(NPC):
    def __init__(self, start_pos: pygame.Vector2 = pygame.Vector2(0, 0)):
        self.sprite_folder = "assets/npcs/autopilot"
        self.sprite_width = 25
        self.default_anim = "autopilot_idle"
        self.idle_chance = 200
        self.idle_anims = [
            "autopilot_blink",
            "autopilot_yawn",
        ]

        # Call parent const
        NPC.__init__(self, start_pos)
