import pygame

# Import other files from this project
import config

# Setup stuff
pygame.init()
#screen = pygame.display.set_mode((config.CANVAS_SIZE_X, config.CANVAS_SIZE_Y), pygame.RESIZABLE)
screen = pygame.display.set_mode((config.CANVAS_SIZE_X, config.CANVAS_SIZE_Y))
clock = pygame.time.Clock()

running = True
while running:
    # Iterate over all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE

    # flip() draws to the screen
    pygame.display.flip()

    # Clear the screen ready for the next frame
    screen.fill("darkgray")

    # limit FPS
    clock.tick(config.FPS_TARGET)

pygame.quit()