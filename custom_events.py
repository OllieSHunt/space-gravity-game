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
