import pygame
from collections.abc import Callable

from custom_events import *
from entities.entity import Entity

# This class will call a callback OR send an event after a set amount of time.
class TimerEntity(Entity):
    def __init__(self, end_trigger: Callable | pygame.event.Event, delay: float, repeating: bool=False):
        self.end_trigger = end_trigger
        self.delay = delay
        self.is_repeating = repeating
        self.last_timer_tick = pygame.time.get_ticks()

        Entity.__init__(self, (0, 0))

    # Inherated from the Entity class
    def update(self):
        time = pygame.time.get_ticks()
        elapsed = time - self.last_timer_tick

        # Check if enough time has passed
        if elapsed >= self.delay:
            # Do we need to emmit an event or call a callback?
            if isinstance(self.end_trigger, pygame.event.Event):
                pygame.event.post(self.end_trigger)
            else:
                self.end_trigger()

            # Do we need to restart the timer or delete it?
            if self.is_repeating:
                self.last_timer_tick = time
            else:
                delete_event = pygame.event.Event(DELETE_ENTITIES_EVENT, {"entities": [self]})
                pygame.event.post(delete_event)

    # Inherated from the Entity class
    def load_sprite(self) -> pygame.Surface:
        # This is a timer entity, it should not have a sprite
        return pygame.Surface((0, 0))
