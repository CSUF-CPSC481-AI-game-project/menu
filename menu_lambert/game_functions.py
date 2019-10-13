import sys
import pygame


def check_events(button, stats):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event)
       # elif event.type == pygame.KEYUP:
            #continue
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_click_button(button, stats, mouse_x, mouse_y)


def check_click_button(button, stats, mouse_x, mouse_y):
    for button in button:
        if button.rect.collidepoint(mouse_x, mouse_y):
            if button.msg == 'PLAY':
                stats.game_active = True
            elif button.msg == 'INSTRUCTION':
                stats.show_instruction = True
            elif button.msg == 'OPTION':
                stats.show_option = True
            elif button.msg == 'EXIT':
                sys.exit()


def check_keydown_event(event):
    if event.key == pygame.K_ESCAPE:
        sys.exit()


def update_screen(main_settings, screen, button, stats):
    if not stats.game_active and not stats.show_instruction and not stats.show_option:
        screen.blit(main_settings.backgroundImage, (0, 0))
        init_menu(screen, main_settings, button)
    if stats.show_instruction and not stats.game_active and not stats.show_option:
        show_instruction_screen(screen, main_settings, button)

    if stats.game_active:
        show_game_screen(screen, main_settings)

    pygame.display.flip()

def show_game_screen(screen, main_settings):
    screen.blit(main_settings.backgroundImage, (0, 0))


def show_instruction_screen(screen, main_settings, button):
    screen.blit(main_settings.backgroundImage, (0, 0))
    image = pygame.image.load('images/instruction.jpg')
    image = pygame.transform.scale(image, (800, 400))
    image_rect = image.get_rect()
    image_rect.centerx = main_settings.screen_width / 2
    image_rect.centery = 200
    screen.blit(image, image_rect)

    for button in button:
        if button.msg == 'PLAY':
            button.draw_button((image_rect.centerx, 500))
        if button.msg == 'EXIT':
            button.draw_button((image_rect.centerx, 600))


def init_menu(screen, main_settings, button):
    font_large = pygame.font.SysFont(None, 60)
    titleText = font_large.render('AI ATTACK', True, (255, 255, 255), screen)
    titleText_rect = titleText.get_rect()
    titleText_rect.center = (main_settings.screen_width / 2, 200)
    screen.blit(titleText, titleText_rect)
    for button in button:
        button.draw_button()