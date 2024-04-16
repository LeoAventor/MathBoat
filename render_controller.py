from render_data import RENDER_DATA
from game_data import GAME_DATA
from user_data import USER_DATA


class RENDER_CONTROLLER:
    render_data = object()

    def __init__(self):
        self.render_data = RENDER_DATA()

    def update(self, input_class, game_mode="single_player"):
        if isinstance(input_class, GAME_DATA):
            self.render_data.current_streak = input_class.current_streak
            self.render_data.current_single_player_difficulty = input_class.current_single_player_difficulty
            self.render_data.current_attempts = input_class.current_attempts

            if game_mode == "single_player":
                self.render_data.first_number = input_class.sp_first_number
                self.render_data.operation_symbol = input_class.sp_operation_symbol
                self.render_data.second_number = input_class.sp_second_number
                self.render_data.equality_symbol = input_class.sp_equality_symbol
                self.render_data.result_number = input_class.sp_result_number
                self.render_data.correct_answer = input_class.sp_correct_answer
            elif game_mode == "practice":
                self.render_data.first_number = input_class.p_first_number
                self.render_data.operation_symbol = input_class.p_operation_symbol
                self.render_data.second_number = input_class.p_second_number
                self.render_data.equality_symbol = input_class.p_equality_symbol
                self.render_data.result_number = input_class.p_result_number
                self.render_data.correct_answer = input_class.p_correct_answer

            self.render_data.current_status = input_class.current_status
            self.render_data.correct_answer_count = input_class.correct_answer_count
            self.render_data.incorrect_answer_count = input_class.incorrect_answer_count
            self.render_data.previous_correct_answer = input_class.previous_correct_answer
        elif isinstance(input_class, USER_DATA):
            self.render_data.username = input_class.username
            self.render_data.password = input_class.password
            self.render_data.user_win_count = input_class.user_win_count
            self.render_data.user_lose_count = input_class.user_lose_count
            self.render_data.user_current_attempts = input_class.user_current_attempts
            self.render_data.user_current_streak = input_class.user_current_streak
            self.render_data.user_current_difficulty = input_class.user_current_difficulty
            self.render_data.sign_up_confirmation_status = input_class.sign_up_confirmation_status
            self.render_data.sign_in_confirmation_status = input_class.sign_in_confirmation_status

