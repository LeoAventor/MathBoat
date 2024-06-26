from random import randint
from src.properties import PROPERTIES


class PUZZLE_DATA:
    properties = object()

    # Puzzle data
    first_number = int()
    operation_symbol = str()
    second_number = int()
    equality_symbol = str()
    result_number = int()
    correct_answer = int()

    # Local logic variables
    max_value = int()
    difficulty = str()

    def __init__(self):
        self.properties = PROPERTIES()

        self.equality_symbol = "="
        self.update_max_value()

    def generate_new_first_number(self):
        self.first_number = randint(2, self.max_value)

    def generate_new_second_number(self):
        self.second_number = randint(2, self.max_value)

    def generate_new_fake_result(self, number):
        self.result_number = randint(number // 2, number * 2) + 1

    def update_max_value(self):
        match self.difficulty:
            case "easy":
                self.max_value = self.properties.easy_max_value
            case "medium":
                self.max_value = self.properties.medium_max_value
            case "hard":
                self.max_value = self.properties.hard_max_value
            case "insane":
                self.max_value = self.properties.insane_max_value

    def generate_new_operation_symbol(self):
        match self.difficulty:
            case "easy":
                self.operation_symbol = ["+", "-"][randint(0, 1)]
            case "medium":
                self.operation_symbol = ["+", "-"][randint(0, 1)]
            case "hard":
                self.operation_symbol = ["*", "/"][randint(0, 1)]
            case "insane":
                self.operation_symbol = ["+", "-", "*", "/"][randint(0, 3)]

    def convert_to_str(self):
        self.first_number = str(self.first_number)
        self.second_number = str(self.second_number)
        self.result_number = str(self.result_number)
        self.correct_answer = str(self.correct_answer)
