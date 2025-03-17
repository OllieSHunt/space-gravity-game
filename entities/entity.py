import pygame

# This class represents anything in the world like space invaders, or the
# player. You can inherit it from another class to create a new type of
# entity.
class Entity(pygame.sprite.Sprite):
    # This is run when the class is first created
    def __init__(self, start_pos: pygame.Vector2 = pygame.Vector2(0, 0)):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Load the sprite from file
        self.image = self.load_sprite()

        # Find the images rect and set its position
        self.rect = self.image.get_rect()
        self.rect.x = start_pos.x
        self.rect.y = start_pos.y

    # Draw this entity to another surface
    def draw(self, other_surface: pygame.Surface):
        other_surface.blit(self.image, self.rect)

    # Overwrite when inheriting to change the entity's position, etc...
    #
    # Arguments:
    # entities = a list of all other entities in the game
    # events   = a list of all events (e.g. button presses)
    # space    = pymunk.Space
    def update(self, entities, events, space):
        pass

    # Overwrite this to define a sprite for this type of entity
    #
    # This function should return a pygame Surface
    def load_sprite(self):
        # Load a .png file
        # return pygame.image.load('assets/place-holder.png').convert()

        # Create an sprite from a shape
        square = pygame.Surface((8, 8))
        square.fill("white")
        return square.convert()
