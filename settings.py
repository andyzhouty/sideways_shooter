class Settings:
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.scr_sz = (800, 600)
        self.bg_color = (255, 255, 255)

        # Rocket settings
        self.rocket_speed = 1.2

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_left_speed = 10
        # fleet_direction of 1 : up; -1: down
        self.fleet_direction = 1
