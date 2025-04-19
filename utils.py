# This file contains generic stuff that did not fit anyware else

import pymunk
import os
import csv
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
