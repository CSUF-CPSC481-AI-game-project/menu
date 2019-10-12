import sys
import pygame


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event)
       # elif event.type == pygame.KEYUP:
            #continue
        elif event.type == pygame.MOUSEBUTTONDOWN:
           check_mouse_click


def check_keydown_event(event):
    if event.key == pygame.K_ESCAPE:
        sys.exit()


def update_screen(main_settings, screen, button):
    screen.blit(main_settings.backgroundImage, (0, 0))
    init_menu(screen, main_settings, button)
    pygame.display.flip()

def init_menu(screen, main_settings, button):
    font_large = pygame.font.SysFont(None, 60)
    titleText = font_large.render('AI ATTACK', True, (255, 255, 255), screen)
    titleText_rect = titleText.get_rect()
    titleText_rect.center = (main_settings.screen_width / 2, 200)
    screen.blit(titleText, titleText_rect)
    for button in button:
        button.draw_button()