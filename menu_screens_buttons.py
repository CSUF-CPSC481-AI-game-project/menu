import sys

import pygame
import pygame as pygame

Green = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
PEACH = (249,149,123)
BABYBLUE = (77,172,240)
DKGRAY = (102,102,102)
BLACK = (0,0,0)

pygame.init()

display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))



bg_image = pygame.image.load('background.jpg').convert()
screen.blit(bg_image, [0, 0])
# pygame.display.flip()

font = pygame.font.SysFont('Calibri',40,True,False)
smallFont = pygame.font.SysFont('Calibri',15,True,False)

title = font.render("AI ATTACKS!", True, BLACK)
screen.blit(title,[300, 50])

clock = pygame.time.Clock()


class Button:
    def __init__(self, x, y, width, height, color, surface):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.surface = surface
    def is_pressed(self):
        mouse_position = pygame.mouse.get_pos()
        mouse_x = mouse_position[0]
        mouse_y = mouse_position[1]
        if mouse_x > self.x:
            if mouse_x < self.x + self.width:
                if mouse_y > self.y:
                    if mouse_y < self.y + self.height:

                        mouse_click = pygame.mouse.get_pressed()
                        left_click = mouse_click[0]
                        if left_click:
                            self.color = (0,0,0)
                            return True
        self.color = (230,230,230)
        return False

    def draw_button(self):
        pygame.draw.rect(self.surface, self.color, (self.x, self.y,  self.width, self.height))
        pygame.display.flip()




# 800 x 600
startButton = Button(200, 250, 400, 80, PEACH, screen)
startButton.draw_button()
startText = font.render("Play", True, BLACK)
screen.blit(startText,[225,270])

storyButton = Button(200, 350, 400, 80, BABYBLUE, screen)
storyButton.draw_button()
storyText = font.render("Story", True, BLACK)
screen.blit(storyText,[325, 350])

optionsButton = Button(650, 500, 80, 40, DKGRAY, screen)
optionsButton.draw_button()
optionsText = smallFont.render("Options", True, WHITE)
screen.blit(optionsText,[655,510])

GRAY = (153,153,153)
backButton = Button(50, 50, 150, 80, GRAY, screen)
backText = font.render("Go back", True, BLACK)


playText = font.render("GAME SCREEN", True, WHITE)
storyScreen = font.render("STORY SCREEN", True, WHITE)
optionsScreen = font.render("OPTIONS SCREEN, TOO LAZY TO WRITE A STORY", True, WHITE)


def game_loop():

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                gameExit = True

            if startButton.is_pressed():
                screen.fill(BLACK)
                screen.blit(playText, [250, 100])
                backButton.draw_button()
                screen.blit(backText, [10, 10])
                print("PRESSED B1")

            if storyButton.is_pressed():
                screen.fill(BLACK)
                screen.blit(storyScreen, [250,100])
            if optionsButton.is_pressed():
                screen.fill(BLACK)
                screen.blit(optionsScreen, [150,100])


        pygame.display.flip()
        clock.tick(60)


game_loop()
pygame.quit()
sys.exit()



