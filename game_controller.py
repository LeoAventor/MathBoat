from puzzle_controler import PUZZLE_CONTROLLER
from game_data import GAME_DATA


class GAME_CONTROLLER:
    game_data = object()
    puzzle_controller = object()

    def __init__(self):
        self.game_data = GAME_DATA()
        self.puzzle_controller = PUZZLE_CONTROLLER()

        self.puzzle_controller.puzzle_data.difficulty = self.game_data.current_difficulty
        self.puzzle_controller.puzzle_data.update_max_value()
        self.get_new_puzzle()

    def check_result(self, user_input):
        user_input = str(user_input)
        if user_input != "":
            if self.game_data.correct_answer == user_input:
                self.game_data.current_status = "correct"
                self.game_data.inc_current_streak()

                if self.game_data.current_streak == str(4) and self.game_data.current_difficulty != "insane":
                    self.game_data.inc_current_difficulty()
                    self.puzzle_controller.puzzle_data.difficulty = self.game_data.current_difficulty
                    self.puzzle_controller.puzzle_data.update_max_value()
                    self.game_data.current_streak = str(0)

                    # TODO if win ?
            else:
                self.game_data.current_status = "incorrect"
                self.game_data.current_streak = str(0)
                self.game_data.dec_current_count()

                # TODO if current_count == 0 -> reset_game()

        self.get_new_puzzle()

    def get_new_puzzle(self):
        self.puzzle_controller.generate_new_math_puzzle()
        self.game_data.map_puzzle_data_to_render_data(self.puzzle_controller.puzzle_data)
