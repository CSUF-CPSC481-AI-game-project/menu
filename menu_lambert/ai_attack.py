import pygame
import sys

from settings import *
import game_functions as gf
from game_stats import GameStats
from button import Button


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    main_settings = Settings(screen)
    pygame.display.set_caption("AI Attack")

    play_button = Button(main_settings, screen, 'PLAY',  main_settings.screen_width / 2, 300)
    instruction_button = Button(main_settings, screen, 'INSTRUCTION',  main_settings.screen_width / 2, 400)
    option_button = Button(main_settings, screen, 'OPTION',  main_settings.screen_width / 2, 500)
    exit_button = Button(main_settings, screen, 'EXIT',  main_settings.screen_width / 2, 600)
    button = [play_button, instruction_button, option_button, exit_button]

    #main_menu = Main_menu(main_settings, screen)
    #stats = GameStats(main_settings)
    while True:
        gf.check_events()
        # if stats.game_active:
        gf.update_screen(main_settings, screen, button)

run_game()