import pygame

# This event will add a list of entities to the world.
# 
# This event should always be created with an attribute called "entities".
#
# Example:
# my_event = pygame.event.Event(SPAWN_ENTITY_EVENT, {"entities": [
#     MyNewEntity(...),
#     MyNewEntity(...),
#     MyNewEntity(...),
# ]})
# pygame.event.post(my_event)
SPAWN_ENTITIES_EVENT = pygame.event.custom_type()

# Clear every entity and load a new scene
#
# This event should always be created with an attribute called "level_callback"
# that should be function that takes one argument which is a pymunk Space.
#
# Example:
# my_event = pygame.event.Event(LOAD_LEVEL, {"level_callback": level_1})
# pygame.event.post(my_event)
LOAD_LEVEL = pygame.event.custom_type()
