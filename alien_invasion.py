import sys

import pygame

from settings import Settings
from ship import Ship
class AlienInvasion:
    """Main class to manage the game assets"""
    def __init__(self):
        """initialize the game and create the resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

        #set background colour
        #self.bg_colour = (0,200,200)   so left this accidently and not removing because we did this in settings module

    def run_game(self):
        """start the main loop for the game"""
        while True:
            #watch the keyboard and mouse events
            self._check_events()

            #redraw the screen with background colour
            self.screen.fill(self.settings.bg_colour)

            #Make the most recently drawn screen visible.
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """respond to keyboard input and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """updates images on the screen and flip to the new screen"""
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()

        pygame.display.flip()




if __name__ == '__main__':
    #Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()