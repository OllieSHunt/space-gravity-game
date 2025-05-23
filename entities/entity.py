import pygame

# This class represents anything in the world like NPCs, or the
# player. You can inherit it from another class to create a new type of
# entity.
class Entity(pygame.sprite.Sprite):
    def __init__(self, start_pos: pygame.Vector2 = pygame.Vector2(0, 0)):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Load the sprite from file
        self.image = self.load_sprite()

        self.position = start_pos

    # Draw this entity to another surface
    def draw(self, other_surface: pygame.Surface):
        other_surface.blit(self.image, self.position)

    # Overwrite when inheriting this class to do any stuff that needs doing
    # each frame.
    def update(self):
        pass

    # Overwirte this when inheriting this class if your entity needs to recive
    # any events.
    def handle_events(self, events):
        pass

    # Overwrite this to define a sprite for this type of entity
    #
    # This function should return a pygame Surface
    def load_sprite(self) -> pygame.Surface:
        # Load a .png file
        # return pygame.image.load('assets/place-holder.png').convert_alpha()

        # Create an sprite from a shape
        square = pygame.Surface((8, 8))
        square.fill("white")
        return square.convert_alpha()
