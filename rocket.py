import pygame


class Rocket:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load('images/rocket2.bmp')
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.moving_down = False
        self.moving_up = False
        self.y = float(self.rect.y)
        self.rocket_speed = game.settings.rocket_speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.rocket_speed
        elif self.moving_up and self.rect.top > 0:
            self.y -= self.rocket_speed

        self.rect.y = self.y
