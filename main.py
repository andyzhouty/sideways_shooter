import pygame
import sys
from rocket import Rocket
from settings import Settings
from bullet import Bullet
from alien import Alien


class Game:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.scr_sz)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.rocket = Rocket(self)
        pygame.display.set_caption("Sideways Shooter")

        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self.rocket.update()
            self._update_aliens()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit(0)
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    def _update_bullets(self):
        self.bullets.update()

        screen_rect = self.screen.get_rect()
        for bullet in self.bullets.copy():
            if bullet.rect.left > screen_rect.right:
                self.bullets.remove(bullet)
        # print(len(self.bullets))

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_y = self.settings.scr_sz[1] - (alien_height)
        number_aliens_y = available_space_y // (2 * alien_height)

        rocket_width = self.rocket.rect.width
        available_space_x = (self.settings.scr_sz[0] -
                             (4 * alien_width) - rocket_width)
        number_lines = available_space_x // (2 * alien_width)

        for line_number in range(number_lines):
            for alien_number in range(number_aliens_y):
                self._create_alien(alien_number, line_number)

    def _create_alien(self, alien_number, line_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.y = alien_height + 2 * alien_height * alien_number
        alien.rect.y = alien.y
        alien.rect.x = self.settings.scr_sz[0] - \
            (alien.rect.width + 2 * alien.rect.width * line_number)
        self.aliens.add(alien)

    def _update_aliens(self):
        """Updates the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.fleet_left_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Updates images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Make the mose recently drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run_game()
