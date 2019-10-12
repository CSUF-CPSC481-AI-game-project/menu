import pygame

class Button():
    def __init__(self, main_settings, screen, msg, x, y):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = 250, 50
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 25)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = x
        self.rect.centery = y
        self.prep_msg(msg)
        self.image = pygame.image.load('images/button_image.jpg')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)