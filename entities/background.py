import pygame
import random

from entities.entity import Entity
import config

# A background image that can optionaly scroll
class StarBackground(Entity):
    def __init__(self, ship_moving=False):
        self.set_ship_moving(ship_moving)

        self.largest_star_size = pygame.Vector2(8, 8)
        self.background_color = pygame.Color(20, 16, 19)

        self.load_star_images()
        self.stars = []

        Entity.__init__(self, (0, 0))

        self.spawn_inital_stars()

    # Inherated from the Entity class
    def update(self):
        # Deside weather to spawn a new star
        if random.randint(0, self.star_spawn_chance) == 0:
            x = -self.largest_star_size.x
            y = random.randint(-int(self.largest_star_size.y), self.image.get_height())
            speed = random.uniform(self.min_star_speed, self.max_star_speed)
            image = random.choice(self.star_images)

            # Spawn a new star
            self.stars.append(Star(x, y, speed, image))

    # Inherated from the Entity class
    def draw(self, other_surface: pygame.Surface):
        self.image.fill(self.background_color)

        # Move and draw each star
        #
        # The reason star movement is also done in the draw funcion instead of
        # the update funcion is for efficiency. I would have to itterate over
        # all stars twice otherwise.
        for star in self.stars:
            # Move the star
            star.x += star.speed

            # TODO: Delete stars that go off the screen

            # Draw the star
            self.image.blit(star.image, (star.x, star.y))

        other_surface.blit(self.image, (0, 0))

    # Makes the stars move faster or slower depending on wheather the ship is
    # moving or not.
    def set_ship_moving(self, is_moving: bool):
        if is_moving:
            self.star_spawn_chance = 10 # Lower = higher chance
            self.min_star_speed = 2
            self.max_star_speed = 4
        else:
            self.star_spawn_chance = 60 # Lower = higher chance
            self.min_star_speed = 0.03
            self.max_star_speed = 0.06

    # Spawns some inital stars
    def spawn_inital_stars(self):
        for x in range(0, self.image.get_width()):
            # Deside weather to spawn a new star
            if random.randint(0, int(self.star_spawn_chance * (self.max_star_speed - self.min_star_speed))) == 0:
                y = random.randint(-int(self.largest_star_size.y), self.image.get_height())
                speed = random.uniform(self.min_star_speed, self.max_star_speed)
                image = random.choice(self.star_images)

                # Spawn a new star
                self.stars.append(Star(x, y, speed, image))

    # Inherated from the Entity class
    def load_sprite(self) -> pygame.Surface:
        return pygame.Surface((config.CANVAS_SIZE_X, config.CANVAS_SIZE_Y))

    # Gets a list of all the star sprites
    def load_star_images(self):
        self.star_images = [
            pygame.image.load("assets/stars/star1.png"),
            pygame.image.load("assets/stars/star2.png"),
            pygame.image.load("assets/stars/star3.png"),
            pygame.image.load("assets/stars/star4.png"),
            pygame.image.load("assets/stars/star5.png"),
            pygame.image.load("assets/stars/star6.png"),
        ]

# A star that is part of a StarBackground
class Star:
    def __init__(self, x: int, y: int, speed: float, image: pygame.Surface):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = image
