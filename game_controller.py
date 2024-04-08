from puzzle_controller import PUZZLE_CONTROLLER
from game_data import GAME_DATA


class GAME_CONTROLLER:
    game_data = object()
    puzzle_controller = object()

    def __init__(self):
        self.game_data = GAME_DATA()
        self.puzzle_controller = PUZZLE_CONTROLLER()

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
                    self.reset_game()
            else:
                self.game_data.current_status = "incorrect"
                self.game_data.current_streak = str(0)
                self.game_data.dec_current_count()

                if self.game_data.current_count == str(0):
                    self.game_data.current_status = "Game Over"
                    self.reset_game()

        self.get_new_puzzle()

    def sync_difficulty(self):
        self.puzzle_controller.puzzle_data.difficulty = self.game_data.current_difficulty
        self.puzzle_controller.puzzle_data.update_max_value()

    def reset_game(self):
        self.game_data.current_difficulty = "easy"
        self.sync_difficulty()
        self.game_data.current_count = str(3)
        self.game_data.current_streak = str(0)
        self.get_new_puzzle()

    def get_new_puzzle(self):
        self.puzzle_controller.generate_new_math_puzzle()
        self.game_data.map_puzzle_data_to_render_data(self.puzzle_controller.puzzle_data)
