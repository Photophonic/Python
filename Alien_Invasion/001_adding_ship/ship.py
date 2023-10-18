import pygame


class Ship:
    """Class to contain ship information"""

    # passing in self and variables from Alien game fro screen
    def __init__(self, ai_game):
        """Init the ship object"""
        self.screen = ai_game.screen
        # access screens rectangle attribute to place ship
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image from file
        self.image = pygame.image.load('Python/Alien_Invasion/images/ship.bmp')
        # set self's rect size from loaded image rec size
        self.rect = self.image.get_rect()

        # 0,0 = top left corner of the display area
        # Set the ships starting default location
        # this sets it to the middle of the main screen
        self.rect.midbottom = self.screen_rect.midbottom

    # create a method tp call blit and feed values
    def blitme(self):
        """Draw the ship's current location"""
        self.screen.blit(self.image, self.rect)
