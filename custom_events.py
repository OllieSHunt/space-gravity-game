import pygame

# This event will add a list of entities to the world.
# 
# This event should always be created with an attribute called "entities".
#
# Example:
# my_event = pygame.event.Event(SPAWN_ENTITIES_EVENT, {"entities": [
#     MyNewEntity(...),
#     MyNewEntity(...),
#     MyNewEntity(...),
# ]})
# pygame.event.post(my_event)
SPAWN_ENTITIES_EVENT = pygame.event.custom_type()

# This event atempts to remove an entity from the world
#
# This event should always be created with an attribute called "entities"
#
# Example:
# my_event = pygame.event.Event(DELETE_ENTITIES_EVENT, {"entities": [my_entity]})
# pygame.event.post(my_event)
DELETE_ENTITIES_EVENT = pygame.event.custom_type()

# Clear every entity and load a new scene
#
# This event should always be created with an attribute called "level_callback"
# that should be function that takes one argument which is a pymunk Space.
#
# In other words, "level_callback" must be this type: Callable[[pymunk.Space], list[Entity]]
#
# Example:
# my_event = pygame.event.Event(LOAD_LEVEL_EVENT, {"level_callback": level_1})
# pygame.event.post(my_event)
LOAD_LEVEL_EVENT = pygame.event.custom_type()


# This event restarts the current level
RESTART_LEVEL_EVENT = pygame.event.custom_type()

# Add points to the score counter
#
# This event should always be created with an attribute called "score".
#
# Example:
# my_event = pygame.event.Event(INCREACE_SCORE_EVENT, {"score": 10})
# pygame.event.post(my_event)
INCREACE_SCORE_EVENT = pygame.event.custom_type()
