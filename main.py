import pygame
import pymunk
import pymunk.pygame_util

# Import other files from this project
import config
import entitiy_bundles
from custom_events import *

# Setup stuff
pygame.init()
screen = pygame.display.set_mode((700, 500), pygame.RESIZABLE)
main_surface = pygame.Surface((config.CANVAS_SIZE_X, config.CANVAS_SIZE_Y))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0, config.GRAVITY_STRENGTH)

# This list will keep track of all things in the game. e.g. the player, etc...
#
# NOTE: Please only put objects in this list that inherit from the Entity class
#       defined in the entity.py file
entities = []

# Spawn entities required for level 1
pygame.event.post(pygame.event.Event(SPAWN_ENTITIES_EVENT, {"entities": entitiy_bundles.level_1(space)}))

# Debug mode enables the rendering of hitboxes and stuff
debug_mode = False

running = True
while running:
    # Iterate over all events
    events = []
    for event in pygame.event.get():
        # Collect all events into a list ready to pass to each entity's
        # update function
        events.append(event)
        
        # Handle events that are relevent to the whole program
        if event.type == pygame.QUIT:
            running = False

        elif event.type == SPAWN_ENTITIES_EVENT:
            # Spawn all new entities
            for new_entity in event.dict.get("entities"):
                entities.append(new_entity)

        elif event.type == pygame.KEYDOWN:
            # Toggle debug mode
            if event.key == pygame.K_BACKQUOTE:
                debug_mode = not debug_mode

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("darkgrey")
    main_surface.fill("black")

    # Render and update each entity
    for entity in entities:
        entity.handle_events(events)
        entity.update()
        entity.draw(main_surface)

    # Update physics
    space.step(1 / config.FPS_TARGET)

    # Draw physics bodies
    if debug_mode:
        space.debug_draw(pymunk.pygame_util.DrawOptions(main_surface))
    
    # Scale the game screen
    scale_multiplyer = screen.get_size()[1] / config.CANVAS_SIZE_Y
    
    scaled_main_surface = pygame.transform.scale(
        main_surface,
        (config.CANVAS_SIZE_X * scale_multiplyer, config.CANVAS_SIZE_Y * scale_multiplyer)
    )

    # blit() puts the main_surface onto the centre of the screen
    screen.blit(
        scaled_main_surface,
        ((screen.get_size()[0] / 2) - (scaled_main_surface.get_size()[0] / 2), 0)
    )


    # flip() draws to the screen
    pygame.display.flip()

    # limit FPS
    clock.tick(config.FPS_TARGET)

pygame.quit()
