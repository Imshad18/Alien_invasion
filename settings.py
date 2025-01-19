class Settings:
    """here we store all settings of our game"""
    def __init__(self):
        """starting the game's setting"""
        #screen setting
        self.screen_width = 600
        self.screen_height = 600
        self.bg_colour = (50,150,200)

        #ship settings
        self.ship_speed = 10

        #Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width  = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)

