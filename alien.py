import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top right of the screen
        self.rect.x = ai_game.settings.scr_sz[0] - 2 * self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

    def update(self):
        """Move the alien to the top."""
        self.y -= self.settings.alien_speed
        self.rect.y = self.y
