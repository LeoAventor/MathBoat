from render_data import RENDER_DATA
from game_data import GAME_DATA
from user_data import USER_DATA


class RENDER_CONTROLLER:
    render_data = object()

    def __init__(self):
        self.render_data = RENDER_DATA()

    def update(self, input_class):
        if isinstance(input_class, GAME_DATA):
            self.render_data.current_streak = input_class.current_streak
            self.render_data.current_difficulty = input_class.current_difficulty
            self.render_data.current_count = input_class.current_count
            self.render_data.first_number = input_class.first_number
            self.render_data.operation_symbol = input_class.operation_symbol
            self.render_data.second_number = input_class.second_number
            self.render_data.equality_symbol = input_class.equality_symbol
            self.render_data.result_number = input_class.result_number
            self.render_data.correct_answer = input_class.correct_answer
            self.render_data.current_status = input_class.current_status
        elif isinstance(input_class, USER_DATA):
            self.render_data.username = input_class.username
            self.render_data.password = input_class.password
            self.render_data.confirmation_status = input_class.confirmation_status

