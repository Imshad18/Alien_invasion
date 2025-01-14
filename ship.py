import pygame

class Ship:
    """class to manage the ship"""
    def __init__(self, ai_game):
        """getting the ship started and its initial position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #load the ships image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #start new ship at the bottom centre of screen
        self.rect.midbottom = self.screen_rect.midbottom
        #Movement flag: start with a ship that is not moving
        self.moving_right = False

    def update(self):
        """update the ship's position based on movemnets flag"""
        if self.moving_right:
            self.rect.x+=1

    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image,self.rect)