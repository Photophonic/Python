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
            # to call a method  within a class, use self.X to call this instance of the object
            self._check_events()
            # Update the ship values
            self.ship.udpate()
            # call method to update screen values
            self._update_screen()

            # tick method takes the framerate as an argument
            self.clock.tick(60)

    # create a method to contain the events loop for easier management
    def _check_events(self):
        # watch for KBM movemebts
        # pygame.event.get() picks up keyboard events
        # need to specify what type of events to pickup
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # check what key is pressed
            elif event.type == pygame.KEYDOWN:
                # is the key RIGHT?
                if event.key == pygame.K_RIGHT:
                    # update the value to True & tell ship class it is moving
                    self.ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    # update the value to True & tell ship class it is moving
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
    # create a method to contain screen related variables

    def _update_screen(self):
        # change the color to the value in init(), uses the settings object
        self.screen.fill(self.settings.bg_color)

        # draw the ship onto the screen space
        self.ship.blitme()

        # Make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run game.
    ai = AlienInvasion()
    ai.run_game()
