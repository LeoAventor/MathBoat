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
        self.first_number = randint(1, to)

    def generate_new_math_sign(self):
        self.sign_symbol = ["+", "-", "*", "/"][randint(0, 3)]

    def convert_to_str(self):
        self.first_number = str(self.first_number)

class RENDER_DATA:
    current_streak = 0
    current_level = 1
    current_count = 3  
   
    def generate_new_current_streak(self, to):
        self.current_streak = randint(0, to)

    def generate_new_current_level(self, to):
        self.current_level = randint(1, to)

    def generate_new_current_count(self):
        self.current_count = randint(3,0)

