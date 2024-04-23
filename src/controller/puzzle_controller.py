from random import randint
from src.data.puzzle_data import PUZZLE_DATA


class PUZZLE_CONTROLLER:
    # Variables
    puzzle_data = object()

    def __init__(self):
        self.puzzle_data = PUZZLE_DATA()

    def generate_new_math_puzzle(self):
        self.generate_math_puzzle()

        match self.puzzle_data.difficulty:
            case "easy":
                self.puzzle_data.correct_answer = self.puzzle_data.result_number
                self.puzzle_data.result_number = "?"
            case "medium":
                match randint(0, 1):
                    case 0:
                        self.puzzle_data.correct_answer = self.puzzle_data.result_number
                        self.puzzle_data.result_number = "?"
                    case 1:
                        self.puzzle_data.correct_answer = self.puzzle_data.second_number
                        self.puzzle_data.second_number = "?"
            case "hard":
                match randint(0, 1):
                    case 0:
                        self.puzzle_data.correct_answer = self.puzzle_data.result_number
                        self.puzzle_data.result_number = "?"
                    case 1:
                        self.puzzle_data.correct_answer = self.puzzle_data.second_number
                        self.puzzle_data.second_number = "?"
            case "insane":
                match randint(0, 1):
                    case 0:
                        self.puzzle_data.correct_answer = self.puzzle_data.operation_symbol
                        self.puzzle_data.operation_symbol = "?"
                    case 1:
                        match randint(0, 1):
                            case 0:
                                self.puzzle_data.correct_answer = "="
                            case 1:
                                temporary_result = self.puzzle_data.result_number
                                self.puzzle_data.generate_new_fake_result(temporary_result)
                                self.puzzle_data.correct_answer = "<" if (temporary_result
                                                                          < self.puzzle_data.result_number) else ">"
                        self.puzzle_data.equality_symbol = "?"

        self.puzzle_data.convert_to_str()

    def generate_math_puzzle(self):
        self.puzzle_data.generate_new_first_number()
        self.puzzle_data.generate_new_second_number()
        self.puzzle_data.generate_new_operation_symbol()

        match self.puzzle_data.operation_symbol:
            case "+":
                self.addition()
            case "-":
                self.subtraction()
            case "*":
                self.multiplication()
            case "/":
                self.division()

        self.puzzle_data.equality_symbol = "="

    def addition(self):
        self.puzzle_data.result_number = self.puzzle_data.first_number + self.puzzle_data.second_number

    def subtraction(self):
        self.generate_subtraction_data()
        self.puzzle_data.result_number = self.puzzle_data.first_number - self.puzzle_data.second_number
    
    def multiplication(self):
        self.puzzle_data.result_number = self.puzzle_data.first_number * self.puzzle_data.second_number

    def division(self):
        self.generate_division_data()
        self.puzzle_data.result_number = self.puzzle_data.first_number // self.puzzle_data.second_number

    def generate_subtraction_data(self):
        while self.puzzle_data.second_number > self.puzzle_data.first_number:
            self.puzzle_data.generate_new_second_number()

    def generate_division_data(self):
        while self.puzzle_data.first_number % self.puzzle_data.second_number != 0:
            self.puzzle_data.generate_new_second_number()
