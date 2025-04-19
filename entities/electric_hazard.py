import pygame
import pymunk
import math
from copy import copy

from entities.entity import Entity
from animation import AnimationPlayer
from custom_events import *
import config
import utils
import collision_handlers

# A thing that spawns ElectricZap entities
class ElectricHazard(Entity):
    # Arguments:
    #
    # space: a pymunk Space
    #
    # start_pos: where this entity is
    #
    # rotation: rotation in degrees
    #
    # target: the point to fire electrisity at
    #
    # frequency: how often (in miliseconds) to spawn an ElectricZap entity
    def __init__(self,
                space: pymunk.Space,
                start_pos: pygame.Vector2 = pygame.Vector2(0, 0),
                rotation: int = 0,
                target: pygame.Vector2 = None,
                frequency: int = None,
            ):
        self.space = space
        self.target = target
        self.frequency = frequency
        self.timer = 0
        self.last_timer_tick = pygame.time.get_ticks()
        
        # Call constructor of parent class
        Entity.__init__(self, start_pos)

        self.image = pygame.transform.rotate(self.image, -rotation)

    # Inherated from the Entity class
    def update(self):
        if self.frequency != None:
            # Get how much time as gone by since the last time this function was called
            time = pygame.time.get_ticks()
            elapsed = time - self.last_timer_tick
            self.last_timer_tick = pygame.time.get_ticks()

            # Advance the timer
            self.timer += elapsed

            # Check if timer has gone on long enough
            if self.timer >= self.frequency:
                # Spawn some electircity and reset the timer
                self.timer = 0

                start = copy(self.position)
                end = copy(self.target)

                start.x += self.image.get_width() / 2
                start.y += self.image.get_height() / 2
                end.x += self.image.get_width() / 2
                end.y += self.image.get_height() / 2

                electric = ElectricZap(
                    self.space,
                    start,
                    end,
                    self.frequency / 2,
                    self.frequency / 2.5,
                )

                pygame.event.post(pygame.event.Event(SPAWN_ENTITIES_EVENT, {"entities": [electric]}))

    # Inherated from the Entity class
    def load_sprite(self) -> pygame.Surface:
        return pygame.image.load('assets/electric_hazard/electric_hazard.png').convert_alpha()

# An arc of electricity
class ElectricZap(Entity):
    def __init__(self,
                space: pymunk.Space,
                start: pygame.Vector2,
                end: pygame.Vector2,
                lifetime: int=0,
                warning_duration: int=0
            ):
        self.lifetime = lifetime
        self.warning_duration = warning_duration
        self.timer = 0
        self.last_timer_tick = pygame.time.get_ticks()
        self.start = start
        self.end = end

        # Create a pymunk body and shape for this entity.
        # The collision shape will be made later.
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        space.add(self.body)
        
        # Call constructor of parent class
        Entity.__init__(self, start)

    # Inherated from the Entity class
    def update(self):
        # Get how much time as gone by since the last time this function was called
        time = pygame.time.get_ticks()
        elapsed = time - self.last_timer_tick
        self.last_timer_tick = pygame.time.get_ticks()

        # Advance the timer
        self.timer += elapsed

        # Check if timer has gone on long enough
        if self.timer >= self.warning_duration and self.anim_player.current_anim == "warning":
            # Change animation
            self.anim_player.switch_animation("zap")

            # Create a collision shape for this body
            segment = pymunk.Segment(self.body, (self.start.x, self.start.y), (self.end.x, self.end.y), 1)
            segment.sensor = True
            segment.collision_type = collision_handlers.HAZARD_COLLISION_TYPE
            self.body.space.add(segment)

        if self.timer >= self.lifetime:
            # Delete self
            pygame.event.post(pygame.event.Event(DELETE_ENTITIES_EVENT, {"entities": [self]}))

    # Inherated from the Entity class
    def draw(self, other_surface: pygame.Surface):
        # Get next animation frame (but only if enough time has passed since last frame)
        if self.anim_player.next_if_ready():
            self.image = self.anim_player.get_frame()

        # Draw the animation frame repeated between the start and end positions
        current = self.start
        while True:
            # Calculate the sprite rotation
            # Copied from: https://stackoverflow.com/questions/10473930/how-do-i-find-the-angle-between-2-points-in-pygame
            dx = self.end.x - current.x
            dy = self.end.y - current.y
            rads = math.atan2(-dy,dx)
            degs = math.degrees(rads)

            # Crop the image if it would go past the destination
            dist_to_dest = current.distance_to(self.end)
            len_of_img = self.image.get_width()
            new_len = len_of_img - max(len_of_img - dist_to_dest, 0)
            croped_image = self.image.subsurface(0, 0, new_len, self.image.get_height())

            # Pad croped image with empty space to make it the same size as a regular image
            final_img = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
            final_img.blit(croped_image, (0, 0))
            
            # Rotate and draw image
            # https://stackoverflow.com/questions/15098900/how-to-set-the-pivot-point-center-of-rotation-for-pygame-transform-rotate
            img_rect = final_img.get_rect()
            pivot = pygame.Vector2(0, img_rect.centery)
            pivot_offset = img_rect.center - pivot

            rotated_image = pygame.transform.rotate(final_img, degs)
            rotated_offset = pivot_offset.rotate(degs)

            new_rect = rotated_image.get_rect()
            new_rect = rotated_image.get_rect(center=new_rect.center-pivot_offset)

            other_surface.blit(rotated_image, current + new_rect.topleft)

            # Move to next point
            current = current.move_towards(self.end, self.image.get_width())

            # Check if at end of electric beam
            if current == self.end:
                break

    # Inherated from the Entity class
    def load_sprite(self) -> pygame.Surface:
        self.anim_player = AnimationPlayer('assets/electric_zap', 26)
        self.anim_player.switch_animation("warning")
        return self.anim_player.get_frame()
