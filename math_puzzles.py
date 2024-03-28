from random import randint


class PUZZLE_CONTROLLER:
    # Constants
    PUZZLE_DATA_KEYS = ["firstNumber", "signSymbol", "secondNumber", "equalitySymbol", "resultNumber"]
    MATH_SIGNS = ["+", "-", "*", "/"]
    EQUALITY_SIGNS = []
    EASY_MODE = 20
    MEDIUM_MODE = 30
    HARD_MODE = 40

    # Variables
    puzzle_data = dict()

    def __init__(self):
        for i in self.PUZZLE_DATA_KEYS:
            self.puzzle_data[i] = "init"

    def generate_new_math_puzzle(self, exercise=1, difficulty="easy"):
        self.generate_math_puzzle(difficulty)

        match exercise:
            case 1:
                self.puzzle_data["correctAnswer"], self.puzzle_data["resultNumber"] = \
                    self.puzzle_data["resultNumber"], "?"
            case 2:
                self.puzzle_data["correctAnswer"], self.puzzle_data["secondNumber"] = \
                    self.puzzle_data["secondNumber"], "?"
            case 3:
                self.puzzle_data["correctAnswer"], self.puzzle_data["signSymbol"] = \
                    self.puzzle_data["signSymbol"], "?"
            case 4:
                self.puzzle_data["correctAnswer"], self.puzzle_data["equalitySymbol"] = \
                    self.puzzle_data["equalitySymbol"], "?"

    def generate_math_puzzle(self, difficulty):
        match difficulty:
            case "easy":
                mode = self.EASY_MODE
            case _:
                mode = self.EASY_MODE

        first_number = randint(1, mode)
        second_number = randint(1, mode)
        result_number = 0

        math_sign = self.MATH_SIGNS[randint(0, 3)]
        equality_sign = "="

        match math_sign:
            case "+":
                result_number = first_number + second_number
            case "-":
                result_number = first_number - second_number
            case "*":
                result_number = first_number * second_number
            case "/":
                while first_number % second_number != 0:
                    second_number = randint(1, 20)

                result_number = first_number // second_number

        self.puzzle_data["firstNumber"] = str(first_number)
        self.puzzle_data["signSymbol"] = math_sign
        self.puzzle_data["secondNumber"] = str(second_number)
        self.puzzle_data["equalitySymbol"] = equality_sign
        self.puzzle_data["resultNumber"] = str(result_number)
