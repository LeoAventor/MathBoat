from puzzle_controler import PUZZLE_CONTROLLER
from render_data import RENDER_DATA


class LOGIC_CONTROLLER:
    puzzle = PUZZLE_CONTROLLER()
    render_data = RENDER_DATA()

    def __init__(self):
        self.get_new_puzzle(1, "easy")

    def check_result(self, user_input):
        self.render_data.current_status = "correct" if (self.render_data.correct_answer
                                                        == str(user_input)) else "incorrect"
        # TODO Generate new puzzle
        # TODO Change Score

    def get_new_puzzle(self, exercise, difficulity):
        self.puzzle.generate_new_math_puzzle(exercise=exercise, difficulty=difficulity)
        self.render_data.map_puzzle_data_to_render_data(self.puzzle.puzzle_data)
