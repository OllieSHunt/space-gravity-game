import math
import pygame
import pymunk

from entities.entity import Entity

class PhysicsEntity(Entity):
    # This is run when the class is first created
    #
    # For what the "body_type" paramiter is, see this link:
    # https://www.pymunk.org/en/latest/pymunk.html#pymunk.Body
    def __init__(self, space: pymunk.Space, rect: pygame.Rect, mass: float, friction: float, body_type: int):
        # Create physics body and polygon
        self.body = pymunk.Body(body_type=body_type)
        self.body.position = (rect.x + (rect.width / 2), rect.y + (rect.height / 2))
        self.poly = pymunk.Poly.create_box(self.body, size=(rect.width, rect.height))
        self.poly.mass = mass
        self.poly.friction = friction

        # Add body and poly to the pymunk Space
        space.add(self.body, self.poly)

        # Call constructor of parent class
        Entity.__init__(self, pygame.Vector2(rect.x, rect.y))

    def draw(self, other_surface: pygame.Surface):
        # Moves the pygame sprite to the same location as the pymunk physics body
        self.update_sprite_pos()

        # Rotate the pygame sprite
        # https://www.geeksforgeeks.org/radians-to-degrees/
        rotation = (180 / math.pi) * self.body.angle # ratians -> degrees
        rotated_image = pygame.transform.rotate(self.image, -rotation)

        other_surface.blit(rotated_image, self.position)

    # Moves the pygame sprite to the same location as the pymunk physics body
    def update_sprite_pos(self):
        self.position = self.body.position - (self.get_size() / 2)

    # Calculate the size of this physics body
    def get_size(self) -> pygame.Vector2:
        return pygame.Vector2(
            self.poly.bb.right - self.poly.bb.left,
            self.poly.bb.top - self.poly.bb.bottom,
        )
