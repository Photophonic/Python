# sys contains the elements needed to quit the game
import sys

# pygame contains elements required to make a game
import pygame

# import the settings for use in this package
from settings import Settings

# import the ship class from file
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Def to initilize the game"""
        pygame.init()

        # define the games internal frame clock from pygame
        self.clock = pygame.time.Clock()

        # create instance of the settings class and assing to variable
        self.settings = Settings()

        # call pygame to create the window size for the game
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        # caption on the screen
        pygame.display.set_caption("Alien Invasion")

        # Set background color -> now part of settings.py
        # self.bg_color = (230, 230, 230)

        # create a new instance of ship, this method requiers an in
        # argument, so we pass it an instance of AlineInvation (AI)
        # this will give it access to the game's resources
        self.ship = Ship(self)

    def run_game(self):
        """run game"""
        while True:

            # watch for KBM movemebts
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # change the color to the value in init(), uses the settings object
            self.screen.fill(self.settings.bg_color)

            # draw the ship onto the screen space
            self.ship.blitme()

            # Make the most recently drawn screen visible
            pygame.display.flip()

            # tick method takes the framerate as an argument
            self.clock.tick(60)


if __name__ == '__main__':
    # Make a game instance and run game.
    ai = AlienInvasion()
    ai.run_game()
