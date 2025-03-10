import pygame

# Import other files from this project
import config
from entities.player import Player

# Setup stuff
pygame.init()
#screen = pygame.display.set_mode((config.CANVAS_SIZE_X, config.CANVAS_SIZE_Y), pygame.RESIZABLE)
screen = pygame.display.set_mode((config.CANVAS_SIZE_X, config.CANVAS_SIZE_Y))
clock = pygame.time.Clock()

# This list will keep track of all things in the game. e.g. the player, etc...
#
# NOTE: Please only put objects in this list that inherit from the Entity class
#       defined in the entity.py file
entities = [
    Player()
]

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

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # Render and update each entity
    for entity in entities:
        entity.update(entities, events)
        entity.draw(screen)

    # flip() draws to the screen
    pygame.display.flip()

    # Clear the screen ready for the next frame
    screen.fill("darkgray")

    # limit FPS
    clock.tick(config.FPS_TARGET)

pygame.quit()