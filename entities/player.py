import math
import random
import functools
import pygame
import pymunk

from entities.physics_entity import PhysicsEntity
from entities.wall import Wall
from animation import AnimationPlayer
from custom_events import *
import config
from collision_handlers import *

class Player(PhysicsEntity):
    def __init__(self, space: pymunk.Space, start_pos: pygame.Vector2 = pygame.Vector2(0, 0)):
        self.moving_left = False
        self.moving_right = False
        self.starting_jump = False
        self.magnet_active = False

        # The player's collision box and its position relative to the sprite
        collision_box = pygame.Rect((2, 2), (8, 8))

        # Call constructor of parent class
        PhysicsEntity.__init__(self,
                               space=space,
                               start_pos=start_pos,
                               collision_box=collision_box,
                               density=1,
                               friction=0.8,
                               body_type=pymunk.Body.DYNAMIC
                           )

        # Set the shape type and filter for each of the player's collision shapes
        for shape in self.body.shapes:
            shape.collision_type = PLAYER_COLLISION_TYPE
            shape.filter = pymunk.ShapeFilter(categories=PLAYER_OBJECT_CATEGORY)

    # Inherated from the Entity class
    def update(self):
        # Chance to play random idle animation
        self.play_random_idle()

        # Move the player
        if self.moving_left:
            self.body.angular_velocity = -config.PLAYER_ROTATE_SPEED
            
        # Move the player
        if self.moving_right:
            self.body.angular_velocity = config.PLAYER_ROTATE_SPEED

        # Handle jumps
        if self.starting_jump:
            # Call function for every collision to get the normal
            collision_normals = []
            self.body.each_arbiter(lambda arbiter: collision_normals.append(arbiter.normal))

            # If touching a wall:
            if len(collision_normals) != 0:
                # 1. Combine all the collision normals into one vector
                # 2. Rotate that vector to be relative to the way the player is facing
                # 3. Scale the vector to config.PLAYER_JUMP_FORCE
                # 4. Apply the vector to the player's pyhsics body
                combind_collision_normal = functools.reduce(lambda x, y: x+y, collision_normals).normalized()
                vector = -combind_collision_normal.rotated(-self.body.angle).scale_to_length(config.PLAYER_JUMP_FORCE)
                self.body.apply_impulse_at_local_point(vector)

            # Start the jump animation
            self.anim_player.switch_animation("player_push", switch_when_done="player_idle")

        if self.magnet_active:
            # Find the nearest wall
            # The filter is to exclude the player
            filter = pymunk.ShapeFilter(mask=pymunk.ShapeFilter.ALL_MASKS() ^ PLAYER_OBJECT_CATEGORY)
            query = self.body.space.point_query_nearest(self.body.position, 99999, filter)

            if query != None:
                # Move the player towards found wall
                direction = (query.point - self.body.position).normalized()
                force = direction * config.PLAYER_MAGNET_STRENGTH
                self.body.apply_force_at_local_point(force.rotated(-self.body.angle))

        self.starting_jump = False

    # Inherated from the Entity class
    def handle_events(self, events):
        for event in events:
            # Handle relevent key presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.moving_left = True
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.moving_right = True
                elif event.key == pygame.K_UP or event.key == pygame.K_SPACE or event.key == pygame.K_w:
                    self.starting_jump = True
                elif event.key == pygame.K_e or event.key == pygame.K_RETURN:
                    self.magnet_active = not self.magnet_active
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.moving_left = False
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.moving_right = False

    # Inherated from the Entity class
    def draw(self, other_surface: pygame.Surface):
        # Animation stuff
        if self.anim_player.next_if_ready():
            self.image = self.anim_player.get_frame()

        # Call this same meathod in the parent class
        super().draw(other_surface)

    # Inherated from the Entity class
    def load_sprite(self) -> pygame.Surface:
        self.anim_player = AnimationPlayer('assets/player', 12)
        self.anim_player.switch_animation("player_idle")
        return self.anim_player.get_frame()

    # This has a chance of playing a random one-off idle animation.
    # e.g. blinking, yawning, etc...
    def play_random_idle(self):
        idle_chance = 512
        idle_anims = [
            "player_blink",
            "player_yawn",
            "player_spin",
        ]

        # Only do idle animations when the player is in the idle state
        if self.anim_player.current_anim == "player_idle":
            # Deside whether to play an idle animation or not
            if random.randint(0, idle_chance) == 0:
                # Choose and swith to a random idle animation
                anim = random.choice(idle_anims)
                self.anim_player.switch_animation(anim, "player_idle")
