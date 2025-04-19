# This file contains generic stuff that did not fit anyware else

import pymunk
import os
import csv
import math
from typing import Any

import config
from collision_handlers import *

# Creates a new pymunk Space and sets it up
def new_pymunk_space():
    space = pymunk.Space()
    space.gravity = (0, config.GRAVITY_STRENGTH)

    # Add collision handler for player hazards
    plr_hzd_handler = space.add_collision_handler(PLAYER_COLLISION_TYPE, HAZARD_COLLISION_TYPE)
    plr_hzd_handler.begin = handle_player_hazard_collision

    return space

# Takes the path to a .csv file and returns a 2D array with the .csv's data in.
#
# Will return `None` if `csv_path` is not a valid csv file.
def parse_csv(csv_path: str) -> list[list[str]] | None:
    file_name, file_extension = os.path.splitext(csv_path)

    # Check this is a .csv file AND it actualy is a file (not a directory)
    if not os.path.isfile(csv_path) or file_extension != ".csv":
        return None

    csv_data = []
    csv_file = open(csv_path, "r")

    for row in csv.reader(csv_file):
        csv_data.append(row)

    return csv_data

# Rotates a surface and blits it onto another surface
# 
# This function was copied from Stackoverflow because maths is hard and I spend
# 2 days of near non-stop work trying to figure it out for myself.
# https://stackoverflow.com/questions/15098900/how-to-set-the-pivot-point-center-of-rotation-for-pygame-transform-rotate/69312319#69312319
def blitRotate(surf: pygame.Surface, image: pygame.Surface, origin: pygame.Vector2, pivot: pygame.Vector2, angle: float):
    image_rect = image.get_rect(topleft = (origin[0] - pivot[0], origin[1]-pivot[1]))
    offset_center_to_pivot = pygame.math.Vector2(origin) - image_rect.center
    rotated_offset = offset_center_to_pivot.rotate(-angle)
    rotated_image_center = (origin[0] - rotated_offset.x, origin[1] - rotated_offset.y)
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)
    surf.blit(rotated_image, rotated_image_rect)

# Gets the angle between two pygame vector2s
# 
# Copied from: https://stackoverflow.com/questions/10473930/how-do-i-find-the-angle-between-2-points-in-pygame
def angleBetween(a: pygame.Vector2, b: pygame.Vector2):
    dx = b.x - a.x
    dy = b.y - a.y
    rads = math.atan2(-dy,dx)
    return math.degrees(rads)
