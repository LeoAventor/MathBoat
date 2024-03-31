from math_puzzles import PUZZLE_CONTROLLER


class LOGIC_CONTROLLER:
    SINGLE_PLAYER_KEYS = ["currentStreak", "currentLevel", "currentCount", "firstNumber", "signSymbol", "secondNumber",
                          "equalitySymbol", "resultNumber", "correctStatus"]

    puzzle = PUZZLE_CONTROLLER()
    render_data = dict()

    def __init__(self):
        for i in self.SINGLE_PLAYER_KEYS:
            self.render_data[i] = "?"
        
        else:
            if i =="currentStreak":
                self.render_data[i] = 0
            if i =="currentCount":
                self.render_data[i] = 0
             

    def check_result(self, user_input):
        expected_result = self.puzzle.puzzle_data["resultNumber"]
        user_input = int(user_input)

        if user_input == expected_result:
            self.render_data["correctStatus"] = "Correct"
            self.render_data["currentStreak"] += 1
            self.render_data["currentLevel"] += 1
            self.render_data["currentCount"] = 1


        else:
            self.render_data["correctStatus"] = "Incorrect"
            self.render_data["currentStreak"] = 0
            self.render_data["currentCount"] += 1
            



    def set_initial_data(self):
        self.puzzle.generate_new_math_puzzle(exercise=1)
        for i in self.puzzle.puzzle_data.keys():
            self.render_data[i] = self.puzzle.puzzle_data[i]
