import os
import pygame

# This class can be used to handle the playing of animations
#
# - This class expects a folder of sprite sheets.
# - Each sprite sheet must contain one animation.
# - Sprites in the sprite sheets must be aranged horrizontaly.
# - All sprites accross all sprite sheets must be the same width apart
class AnimationPlayer:
    # Constructor.
    #
    # Arguments:
    # path         = the path a folder full of sprite sheets
    # sprite_width = the width of each sprite in the sprite sheets
    # playing      = the animation to start playing strate away
    def __init__(self, folder: str, sprite_width: int, playing=None, frame_delay=100):
        self.sprite_width = sprite_width
        self.playing = playing
        self.frame = 0
        self.last_frame_advance = pygame.time.get_ticks()
        self.frame_delay = frame_delay

        # Where all the sprite sheets are sotred
        # {"name": Surface}
        self.sprite_sheets = dict()

        # Load all the sprite sheets
        for file_name in os.listdir(folder):
            file_path = os.path.join(folder, file_name)
            anim_name, file_extension = os.path.splitext(file_name)

            # If this is a .png file AND it actualy is a file (not a directory)
            if os.path.isfile(file_path) and file_extension == ".png":
                # Load the sprite sheet
                sprite_sheet = pygame.image.load(file_path).convert_alpha()

                # Add it to the dict
                self.sprite_sheets[anim_name] = sprite_sheet

    # Advances the animation by one frame
    def next(self):
        self.frame += 1
        self.last_frame_advance = pygame.time.get_ticks()

    # Advance to the next frame, but only if a the correct amount of time has
    # passed.
    #
    # Returns True if the animation player was advanced to the next frame,
    # False otherwise.
    def next_if_ready(self) -> bool:
        time = pygame.time.get_ticks()
        elapsed = time - self.last_frame_advance

        if elapsed >= self.frame_delay:
            self.next()
            return True
        else:
            return False

    # Get the current frame
    def get_frame(self) -> pygame.Surface:
        if self.playing == None or self.playing == "":
            raise Exception("You forgot to start an animation")

        # Get the sprite sheet
        sprite_sheet = self.sprite_sheets.get(self.playing)

        if sprite_sheet == None:
            raise Exception("Could not find animation '" + str(self.playing) + "'.")

        # Get the width of the sprite sheet and work out how many sprites are in it
        width = sprite_sheet.get_width()
        total_sprites = width / self.sprite_width

        if not total_sprites.is_integer():
            raise Exception("Sprite sheet width not divisible by " + str(self.sprite_width))

        # Reset the animatino if it finishes
        if self.frame >= total_sprites:
            self.frame = 0

        # Extract the current frame from the sprite sheet
        return sprite_sheet.subsurface((self.frame * self.sprite_width,
                                         0,
                                         self.sprite_width,
                                         self.sprite_width,
                                        ))

    # Switch whih animation is currently playing
    #
    # The animation names are desided by the file name of the sprite sheet
    def swith_animation(self, animation: str):
        self.frame = 0
        self.playing = animation
