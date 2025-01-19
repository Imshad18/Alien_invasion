import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class to manage the bullets"""
    def __init__(self, ai_game):
        """bullet object at ship's starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Create a bullet rect at (0,0) then set at correct psotion
        self.rect = pygame.Rect(0,0, self.settings.screen_width,self.settings.screen_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #store the bullets position as float
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet upwards"""
        #update the exact position of the bullet
        self.y -= self.settings.bullet_speed
        #update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
