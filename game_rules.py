from math_puzzles import PUZZLE_CONTROLLER


class LOGIC_CONTROLLER:
    SINGLE_PLAYER_KEYS = ["currentStreak", "currentLevel", "currentCount", "firstNumber", "signSymbol", "secondNumber",
                          "equalitySymbol", "resultNumber", "correctStatus"]

    puzzle = PUZZLE_CONTROLLER()
    render_data = dict()

    def __init__(self):
        for i in self.SINGLE_PLAYER_KEYS:
            self.render_data[i] = "?"

        self.render_data["currentStreak"] = 0
        self.render_data["currentLevel"] = 0
        self.render_data["currentCount"] = 3

    def check_result(self, user_input):
        print(user_input, self.puzzle.puzzle_data["correctAnswer"])
        if user_input == "":
            self.render_data["correctStatus"] = "Please enter answer!"
        elif user_input == self.puzzle.puzzle_data["correctAnswer"]:
            self.render_data["correctStatus"] = "Correct"
            self.render_data["currentStreak"] += 1
        else:
            if self.render_data["currentCount"] == 1:
                self.render_data["correctStatus"] = "Game Over!"
                self.render_data["currentStreak"] = 0
                self.render_data["currentLevel"] = 0
                self.render_data["currentCount"] = 3
            else:
                self.render_data["correctStatus"] = "Incorrect"
                self.render_data["currentStreak"] = 0
                self.render_data["currentCount"] -= 1

    def set_initial_data(self):
        self.get_new_puzzle(1,"easy")

    def get_new_puzzle(self, exercise, difficulity):
        self.puzzle.generate_new_math_puzzle(exercise=exercise, difficulty=difficulity)
        for i in self.puzzle.puzzle_data.keys():
            self.render_data[i] = self.puzzle.puzzle_data[i]
            #
            self.render_data.re = self.puzzle.puzzle_data.result_number
