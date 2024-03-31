from random import randint
from puzzle_data import PUZZLE_DATA


class PUZZLE_CONTROLLER:
    # Constants
    EQUALITY_SIGNS = []
    EASY_MODE = 20
    MEDIUM_MODE = 30
    HARD_MODE = 40

    # Variables
    puzzle_data = PUZZLE_DATA()

    def generate_new_math_puzzle(self, exercise=1, difficulty="easy"):
        self.generate_math_puzzle(difficulty)

        match exercise:
            case 1:
                self.puzzle_data.correct_answer = self.puzzle_data.result_number
                self.puzzle_data.result_number = "?"
            case 2:
                self.puzzle_data.correct_answer = self.puzzle_data.second_number
                self.puzzle_data.result_number = "?"
            case 3:
                self.puzzle_data.correct_answer = self.puzzle_data.sign_symbol
                self.puzzle_data.sign_symbol = "?"
            case 4:
                self.puzzle_data.correct_answer = self.puzzle_data.equality_symbol
                self.puzzle_data.equality_symbol = "?"

    def generate_math_puzzle(self, difficulty):
        match difficulty:
            case "easy":
                mode = self.EASY_MODE
            case _:
                mode = self.EASY_MODE

        self.puzzle_data.generate_new_first_number(mode)
        self.puzzle_data.generate_new_second_number(mode)
        self.puzzle_data.generate_new_math_sign()

        match self.puzzle_data.sign_symbol:
            case "+":
                self.addition()
            case "-":
                self.subtraction()
            case "*":
                result_number = first_number * second_number
            case "/":
                self.division(mode)

        self.puzzle_data.convert_to_str()

    def addition(self):
        self.puzzle_data.result_number = self.puzzle_data.first_number + self.puzzle_data.second_number

    def subtraction(self):
        self.puzzle_data.result_number = self.puzzle_data.first_number - self.puzzle_data.second_number

    #multiplicatio

    def division(self, mode):
        self.generate_division_data(mode)
        self.puzzle_data.result_number = self.puzzle_data.first_number // self.puzzle_data.second_number

    def generate_division_data(self, mode):
        while self.puzzle_data.first_number % self.puzzle_data.second_number != 0:
            self.puzzle_data.generate_new_second_number(mode)
