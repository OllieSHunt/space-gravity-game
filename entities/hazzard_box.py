import pygame
import pymunk

from entities.entity import Entity
import collision_handlers

# Invisable box that kills the player if touched
class HazardBox(Entity):
    def __init__(self, space: pymunk.Space, box: pygame.Rect):
        # Create a pymunk body and shape for this entity.
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = pymunk.Vec2d(box.x + (box.width / 2), box.y + (box.height / 2))

        # Create a collision shape for this body
        poly = pymunk.Poly.create_box(self.body, (box.width, box.height))
        poly.sensor = True
        poly.collision_type = collision_handlers.HAZARD_COLLISION_TYPE

        space.add(self.body, poly)
        
        # Call constructor of parent class
        Entity.__init__(self, pygame.Vector2(box.x, box.y))

    # Inherated from the Entity class
    def draw(self, other_surface: pygame.Surface):
        # Don't draw anything
        pass

    # Inherated from the Entity class
    def load_sprite(self) -> pygame.Surface:
        # This is invisible, so the surface has a size of 0
        return pygame.Surface((0, 0))
