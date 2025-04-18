# This link to the pyumnk docs will help explain what is in this file:
# https://www.pymunk.org/en/latest/pymunk.html#pymunk.Space.add_collision_handler

import pymunk

# For player collisions with hazards
HAZARD_COLLISION_TYPE = 1

# For player collisions with hazards
def handle_hazard_collision(arbiter: pymunk.Arbiter, space: pymunk.Space, data):
    print("oww")
    return True
