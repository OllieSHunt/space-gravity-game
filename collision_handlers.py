# This link to the pyumnk docs will help explain what is in this file:
# https://www.pymunk.org/en/latest/pymunk.html#pymunk.Space.add_collision_handler

import pymunk
import pygame

from custom_events import *
import entitiy_bundles

PLAYER_COLLISION_TYPE = 1
HAZARD_COLLISION_TYPE = 2

# For player collisions with hazards
def handle_player_hazard_collision(arbiter: pymunk.Arbiter, space: pymunk.Space, data):
    restart_event = pygame.event.Event(RESTART_LEVEL_EVENT)
    pygame.event.post(restart_event)

    return True
