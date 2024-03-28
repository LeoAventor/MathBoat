from math_puzzles import PUZZLE_CONTROLLER


class LOGIC_CONTROLLER:
    SINGLE_PLAYER_KEYS = ["currentStreak", "currentLevel", "currentCount", "firstNumber", "signSymbol", "secondNumber",
                          "equalitySymbol", "resultNumber", "correctStatus"]

    puzzle = PUZZLE_CONTROLLER()
    render_data = dict()

    def __init__(self):
        for i in self.SINGLE_PLAYER_KEYS:
            self.render_data[i] = "?"

    def check_result(self, user_input):
        print(user_input)
        print(self.render_data)
        print(self.puzzle.puzzle_data)

    def set_initial_data(self):
        self.puzzle.generate_new_math_puzzle(exercise=1)
        for i in self.puzzle.puzzle_data.keys():
            self.render_data[i] = self.puzzle.puzzle_data[i]
