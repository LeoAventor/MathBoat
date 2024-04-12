from puzzle_controller import PUZZLE_CONTROLLER
from database_controller import DATABASE_CONTROLLER
from game_data import GAME_DATA
from user_data import USER_DATA


class GAME_CONTROLLER:
    game_data = object()
    puzzle_controller = object()
    database_controller = object()

    def __init__(self):
        self.puzzle_controller = PUZZLE_CONTROLLER()
        self.database_controller = DATABASE_CONTROLLER()
        self.game_data = GAME_DATA()

        self.sync_difficulty()
        self.get_new_puzzle()

    def check_result(self, user_input):
        user_input = str(user_input)
        if user_input != "":
            if self.game_data.correct_answer == user_input:
                self.game_data.current_status = "correct"
                self.game_data.inc_current_streak()

                if self.game_data.current_streak == str(4) and self.game_data.current_difficulty != "insane":
                    self.game_data.inc_current_difficulty()
                    self.sync_difficulty()
                    self.game_data.current_streak = str(0)

                if self.game_data.current_streak == str(20):
                    self.game_data.current_status = "Winner"
                    self.game_data.inc_win_count()
                    self.reset_game()
            else:
                self.game_data.current_status = "incorrect"
                self.game_data.current_streak = str(0)
                self.game_data.dec_current_count()

                if self.game_data.current_attempts == str(0):
                    self.game_data.current_status = "Game Over"
                    self.game_data.inc_lose_count()
                    self.reset_game()

        self.get_new_puzzle()

    def sync_difficulty(self):
        self.puzzle_controller.puzzle_data.difficulty = self.game_data.current_difficulty
        self.puzzle_controller.puzzle_data.update_max_value()

    def reset_game(self):
        self.game_data.current_difficulty = "easy"
        self.sync_difficulty()
        self.game_data.current_attempts = str(3)
        self.game_data.current_streak = str(0)
        self.get_new_puzzle()

    def get_new_puzzle(self):
        self.puzzle_controller.generate_new_math_puzzle()
        self.game_data.map_puzzle_data_to_render_data(self.puzzle_controller.puzzle_data)

    def save_game_date(self, user):
        if isinstance(user, USER_DATA):
            user.user_current_attempts = self.game_data.current_attempts
            user.user_current_streak = self.game_data.current_streak
            user.user_current_difficulty = self.game_data.current_difficulty
            user.user_win_count = self.game_data.current_win_count
            user.user_lose_count = self.game_data.current_lose_count
            self.database_controller.save_to_file(user)
