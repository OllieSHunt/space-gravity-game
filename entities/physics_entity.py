import math
import pygame
import pymunk

from entities.entity import Entity

class PhysicsEntity(Entity):
    # For an example of how to use inhereit this calass, see player.py
    def __init__(self,
                 space: pymunk.Space,
                 start_pos: pygame.Vector2,
                 collision_box: pygame.Rect,
                 density: float,
                 friction: float,
                 body_type: int
             ):
        # Create physics body
        self.body = pymunk.Body(body_type=body_type)
        self.body.position = (start_pos.x + (collision_box.width / 2), start_pos.y + (collision_box.height / 2))
        self.body.center_of_gravity = pymunk.vec2d.Vec2d(
            collision_box.centerx,
            collision_box.centery,
        )

        # Create a polygon and atatch it to the box
        self.poly = pymunk.Poly.create_box(self.body, size=(collision_box.width, collision_box.height))
        self.poly.friction = friction
        self.poly.density = density

        # Add body and poly to the pymunk Space
        space.add(self.body, self.poly)

        self.sprite_offset = pygame.Vector2(collision_box.top, collision_box.left)

        # Call constructor of parent class
        Entity.__init__(self, start_pos)

    # Inherated from the Entity class
    def draw(self, other_surface: pygame.Surface):
        # Moves the pygame sprite to the same location as the pymunk physics body
        self.position = self.body.position - (self.get_size() / 2)

        # Rotate the pygame sprite to match the physics body
        rotation = (180 / math.pi) * self.body.angle # radians -> degrees
        rotated_image = pygame.transform.rotate(self.image, -rotation)

        other_surface.blit(rotated_image, self.position)

    # Calculate the size of this physics body
    def get_size(self) -> pygame.Vector2:
        return pygame.Vector2(
            (self.poly.bb.right - self.poly.bb.left) + self.sprite_offset.x,
            (self.poly.bb.top - self.poly.bb.bottom) + self.sprite_offset.y,
        )
