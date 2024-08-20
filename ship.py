import pygame

class Ship():

    def __init__(self, screen) -> None:
        """Initialize the ship and set its starting position."""
        self.screen = screen

        # Load the ship imagen and get its rect.
        self.image = pygame.image.load('img/spaceship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship at ist current location"""
        self.screen.blit(self.image, self.rect)