import pygame
import pymunk

from entities.entity import Entity

class PhysicsEntity(Entity):
    # This is run when the class is first created
    #
    # For what the "body_type" paramiter is, see this link:
    # https://www.pymunk.org/en/latest/pymunk.html#pymunk.Body
    def __init__(self, space: pymunk.Space, rect: pygame.Rect, mass: float, friction: float, body_type: int):
        self.rect = rect

        # Call constructor of parent class
        Entity.__init__(self, pygame.Vector2(rect.x, rect.y))

        # Create physics body and polygon
        self.body = pymunk.Body(body_type=body_type)
        self.body.position = (self.rect.x + (self.rect.width / 2), self.rect.y + (self.rect.height / 2))
        self.poly = pymunk.Poly.create_box(self.body, size=(self.rect.width, self.rect.height))
        self.poly.mass = mass
        self.poly.friction = friction

        # Add body and poly to the pymunk Space
        space.add(self.body, self.poly)

    def draw(self, other_surface: pygame.Surface):
        self.update_sprite_pos()
        super().draw(other_surface)

    # Moves the pygame sprite to the same location as the pymunk physics body
    def update_sprite_pos(self):
        self.rect.x = self.body.position.x - (self.rect.width / 2)
        self.rect.y = self.body.position.y - (self.rect.height / 2)
