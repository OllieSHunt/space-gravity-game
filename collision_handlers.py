# These links to the pyumnk docs will help explain what is in this file:
#
# They also explain the difference between masks, filters, categories, groups,
# and collision types.
# 
# https://www.pymunk.org/en/latest/pymunk.html#pymunk.Space.add_collision_handler
# https://www.pymunk.org/en/latest/pymunk.html#pymunk.ShapeFilter

import pymunk
import pygame

from custom_events import *
import entitiy_bundles

PLAYER_COLLISION_TYPE = 1
HAZARD_COLLISION_TYPE = 2

PLAYER_OBJECT_CATEGORY = 0b1

# For player collisions with hazards
def handle_player_hazard_collision(arbiter: pymunk.Arbiter, space: pymunk.Space, data):
    restart_event = pygame.event.Event(RESTART_LEVEL_EVENT)
    pygame.event.post(restart_event)

    return True
