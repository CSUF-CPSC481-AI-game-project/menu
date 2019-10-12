import pygame


class Settings():
    def __init__(self, screen):
        self.screen_width, self.screen_height = screen.get_size()
        self.backgroundImage = pygame.image.load('images/menu_bg.jpg')
        self.backgroundImage = pygame.transform.scale(self.backgroundImage, (self.screen_width, self.screen_height))


