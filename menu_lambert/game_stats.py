class GameStats():
    def __init__(self, main_settings):
        self.main_settings = main_settings
        self.game_active = False
        self.play_again = True
        self.game_over = False
        self.show_instruction = False
        self.show_option = False

    def reset_stats(self):
        self.game_active = False
        self.play_again = True
        self.game_over = False
        self.show_instruction = False
        self.show_option = False
