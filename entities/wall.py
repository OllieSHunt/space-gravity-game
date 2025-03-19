import pygame
import pymunk

from entities.physics_entity import PhysicsEntity

class Wall(PhysicsEntity):
    def __init__(self, space: pymunk.Space, rect: pygame.Rect):
        collision_box = pygame.Rect((0, 0), (rect.width, rect.height))

        # Call constructor of parent class
        PhysicsEntity.__init__(self,
                               space=space,
                               start_pos=pygame.Vector2(rect.x, rect.y),
                               collision_box=collision_box,
                               density=1,
                               friction=1,
                               body_type=pymunk.Body.STATIC
                           )
        
    # Inherated from the Entity class
    def load_sprite(self):
        # Create the sprite based of the size of the physics body
        square = pygame.Surface(self.get_size())
        square.fill("lightgrey")
        return square.convert_alpha()
