class GameStats():
    def __init__(self, main_settings):
        self.main_settings = main_settings
        self.reset_stats()
        self.game_active = False
        self.play_again = True
        self.game_over = False
