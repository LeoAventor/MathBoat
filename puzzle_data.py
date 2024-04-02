from random import randint


class PUZZLE_DATA:
    first_number = 0 
    sign_symbol = "+"
    second_number = 0
    equality_symbol = "="
    result_number = 0
    correct_answer = 0

    def generate_new_first_number(self, to):
        self.first_number = randint(0, to)

    def generate_new_second_number(self, to):
        self.second_number = randint(1, to)

    def generate_new_math_sign(self):
        self.sign_symbol = ["+", "-", "*", "/"][randint(0, 3)]

    def convert_to_str(self):
        self.first_number = str(self.first_number)
        self.second_number = str(self.second_number)
        self.result_number = str(self.result_number)
        self.correct_answer = str(self.correct_answer)
