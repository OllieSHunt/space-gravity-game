import math
import pygame
import pymunk

import config

from entities.physics_entity import PhysicsEntity
from entities.wall import Wall
from animation import AnimationPlayer

class Player(PhysicsEntity):
    def __init__(self, space: pymunk.Space, start_pos: pygame.Vector2 = pygame.Vector2(0, 0)):
        self.moving_left = False
        self.moving_right = False
        self.starting_jump = False

        # The normal of the last collision
        #
        # Set at the start of the update function
        # Reset at the end of the update function
        self.collision_normal = None

        # The player's collision box and its position relative to the sprite
        collision_box = pygame.Rect((2, 2), (8, 8))

        # Call constructor of parent class
        PhysicsEntity.__init__(self,
                               space=space,
                               start_pos=start_pos,
                               collision_box=collision_box,
                               mass=1,
                               friction=0.5,
                               body_type=pymunk.Body.DYNAMIC
                           )

    # Inherated from the Entity class
    def update(self):
        # Call function for every collision to get the normal
        self.body.each_arbiter(self.get_collision_normal)

        # Move the player
        if self.moving_left:
            self.body.apply_force_at_local_point((-config.PLAYER_MOVE_SPEED, 0))

        # Move the player
        if self.moving_right:
            self.body.apply_force_at_local_point((config.PLAYER_MOVE_SPEED, 0))

        # Handle jumps
        if self.starting_jump and self.collision_normal != None:
            vector = -self.collision_normal.rotated(-self.body.angle) * config.PLAYER_JUMP_FORCE
            self.body.apply_impulse_at_local_point(vector)
            self.anim_player.swith_animation("player_push")
        self.starting_jump = False

        # Reset the collision normal
        self.collision_normal = None

    # Inherated from the Entity class
    def handle_events(self, events):
        for event in events:
            # Handle relevent key presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.moving_left = True
                elif event.key == pygame.K_RIGHT:
                    self.moving_right = True
                elif event.key == pygame.K_SPACE:
                    self.starting_jump = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.moving_left = False
                elif event.key == pygame.K_RIGHT:
                    self.moving_right = False

    # Inherated from the Entity class
    def draw(self, other_surface: pygame.Surface):
        # Animation stuff
        if self.anim_player.next_if_ready():
            self.image = self.anim_player.get_frame()

        # Call this same meathod in the parent class
        super().draw(other_surface)

    # Inherated from the Entity class
    def load_sprite(self):
        self.anim_player = AnimationPlayer('assets/player', 12, playing="player_idle")
        return self.anim_player.get_frame()

    # I call this every time this object collides with something using the
    # Body.each_arbiter meathod.
    def get_collision_normal(self, arbiter):
        self.collision_normal = arbiter.normal
