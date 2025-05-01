import pygame
import pymunk
import pymunk.pygame_util

# Import other files from this project
import config
import entitiy_bundles
import utils
from custom_events import *
from entities.player import Player
from entities.score_counter import ScoreCounter
from entities.life_counter import LifeCounter

# Setup stuff
pygame.init()
screen = pygame.display.set_mode((700, 500), pygame.RESIZABLE)
main_surface = pygame.Surface((config.CANVAS_SIZE_X, config.CANVAS_SIZE_Y))
clock = pygame.time.Clock()
space = utils.new_pymunk_space()

# Load fonts
config.font = pygame.font.Font('assets/DisposableDroidBB.ttf', 12)

# This list will keep track of all things in the game. e.g. the player, etc...
#
# NOTE: Please only put objects in this list that inherit from the Entity class
#       defined in the entity.py file
entities = []

# A callback to the funcion that sets up the current level
current_level = entitiy_bundles.level_1

# Spawn entities required for level 1
pygame.event.post(pygame.event.Event(RESTART_LEVEL_EVENT))

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

        elif event.type == DELETE_ENTITIES_EVENT:
            # Delete a list of entities
            for doomed_entity in event.dict.get("entities"):
                entities.remove(doomed_entity)

                # Remove physics body IF the entity has one
                try:
                    body = doomed_entity.body
                except AttributeError:
                    continue

                # Remove each shape associated with the body
                for shape in body.shapes:
                    space.remove(shape)
                space.remove(body)

        elif event.type == LOAD_LEVEL_EVENT:
            level_callback = event.dict.get("level_callback")

            # Reset everything
            entities.clear()
            space = utils.new_pymunk_space()

            # Call new level callback to spawn entities
            pygame.event.post(pygame.event.Event(SPAWN_ENTITIES_EVENT, {"entities": level_callback(space)}))

            # Set the current level
            current_level = level_callback

        elif event.type == RESTART_LEVEL_EVENT:
            # Send a LOAD_LEVEL_EVENT for the current level
            load_level_event = pygame.event.Event(LOAD_LEVEL_EVENT, {"level_callback": current_level})
            pygame.event.post(load_level_event)

        elif event.type == INCREACE_SCORE_EVENT:
            utils.find_first_of_type(entities, ScoreCounter).score += event.dict.get("score")

        elif event.type == PLAYER_MINUS_LIFE:
            # Remove a life 
            life_counter = utils.find_first_of_type(entities, LifeCounter)
            life_counter.lives -= 1

            if life_counter.lives <= 0:
                load_level_event = pygame.event.Event(LOAD_LEVEL_EVENT, {"level_callback": entitiy_bundles.level_1})
                pygame.event.post(load_level_event)

        elif event.type == pygame.KEYDOWN:
            # Toggle debug mode
            if event.key == pygame.K_BACKQUOTE:
                debug_mode = not debug_mode

            # Enable additional keybinds when in debug mode
            if debug_mode:
                if event.key == pygame.K_0:
                    # Teleport to the mouse cursor
                    pos = utils.screen_to_world(pygame.mouse.get_pos(), screen)
                    print(pos)
                    player = utils.find_first_of_type(entities, Player)
                    if player != None:
                        player.body.position = pymunk.Vec2d(pos.x, pos.y)

                # Keys 1-9 take you to a specific level
                elif event.key == pygame.K_1:
                    pygame.event.post(pygame.event.Event(LOAD_LEVEL_EVENT, {"level_callback": entitiy_bundles.level_1}))
                elif event.key == pygame.K_2:
                    pygame.event.post(pygame.event.Event(LOAD_LEVEL_EVENT, {"level_callback": entitiy_bundles.level_2}))
                elif event.key == pygame.K_3:
                    pygame.event.post(pygame.event.Event(LOAD_LEVEL_EVENT, {"level_callback": entitiy_bundles.level_3}))
                elif event.key == pygame.K_4:
                    pygame.event.post(pygame.event.Event(LOAD_LEVEL_EVENT, {"level_callback": entitiy_bundles.level_4}))
                elif event.key == pygame.K_5:
                    pygame.event.post(pygame.event.Event(LOAD_LEVEL_EVENT, {"level_callback": entitiy_bundles.timed_level}))
                elif event.key == pygame.K_6:
                    pygame.event.post(pygame.event.Event(LOAD_LEVEL_EVENT, {"level_callback": entitiy_bundles.level_5}))

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
    scale_multiplyer = utils.get_screen_to_world_multiplyer(screen)
    
    scaled_main_surface = pygame.transform.scale(
        main_surface,
        (config.CANVAS_SIZE_X * scale_multiplyer, config.CANVAS_SIZE_Y * scale_multiplyer)
    )

    # blit() puts the main_surface onto the centre of the screen
    screen.blit(
        scaled_main_surface,
        (
            (screen.get_size()[0] / 2) - (scaled_main_surface.get_size()[0] / 2),
            (screen.get_size()[1] / 2) - (scaled_main_surface.get_size()[1] / 2),
        )
    )

    # flip() draws to the screen
    pygame.display.flip()

    # limit FPS
    clock.tick(config.FPS_TARGET)

pygame.quit()
