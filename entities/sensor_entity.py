import pygame
import pymunk

from entities.physics_entity import PhysicsEntity

# Like a PhysicsEntity but wihtout the physics.
class SensorEntity(PhysicsEntity):
    def __init__(self, space: pymunk.Space, collision_box: pygame.Rect, start_pos: pygame.Vector2):
        # Call constructor of parent class
        PhysicsEntity.__init__(self,
                               space=space,
                               start_pos=start_pos,
                               collision_box=collision_box,
                               density=1,
                               friction=1,
                               body_type=pymunk.Body.STATIC
                           )

        # Modify the polygon from the PhysicsEntity to be a sensor
        self.poly.sensor = True

        self.is_active = False

    # Inherated from the Entity class
    def update(self):
        # Get the pymunk Space that this entity is in
        space = self.poly.space

        # Check for collisions
        if len(space.shape_query(self.poly)) > 0:
            self.sensor_active()

            # Is this the first frame of collision?
            if not self.is_active:
                self.is_active = True
                self.sensor_just_activated()
        else:
            self.sensor_not_active()

            # Is this the first frame of no collisions?
            if self.is_active:
                self.is_active = False
                self.sensor_just_deactivated()

    # Overwirte this meathod to do something when an entity collides with this
    # sensor.
    def sensor_active(self):
        pass

    # Overwirte this meathod to do something when no entities are coliding with
    # this sensor.
    def sensor_not_active(self):
        pass

    # Overwirte this meathod to do something on the first frame when an entity
    # collides with this sensor.
    def sensor_just_activated(self):
        pass

    # Overwirte this meathod to do something on the first frame when no
    # entities are coliding with this sensor.
    def sensor_just_deactivated(self):
        pass
