import random

from puzzle_controller import PUZZLE_CONTROLLER
from database_controller import DATABASE_CONTROLLER
from game_data import GAME_DATA
from user_data import USER_DATA
from properties import PROPERTIES


class GAME_CONTROLLER:
    game_data = object()
    puzzle_controller = object()
    database_controller = object()
    properties = object()

    def __init__(self):
        self.puzzle_controller = PUZZLE_CONTROLLER()
        self.database_controller = DATABASE_CONTROLLER()
        self.game_data = GAME_DATA()
        self.properties = PROPERTIES()

        self.sync_difficulty_for_single_player()
        self.get_new_puzzle_for_single_player()

        self.sync_difficulty_for_practice()
        self.get_new_puzzle_for_practice()

    def check_result_for_single_player(self, user_input):
        user_input = str(user_input)
        if user_input != "":
            if self.game_data.sp_correct_answer == user_input:
                self.game_data.current_status = "correct"
                self.game_data.inc_current_streak()

                if (self.game_data.current_streak == self.properties.streak_to_level_up and
                        self.game_data.current_single_player_difficulty != "insane"):
                    self.game_data.inc_current_difficulty()
                    self.sync_difficulty_for_single_player()
                    self.game_data.current_streak = str(0)

                if self.game_data.current_streak == self.properties.streak_to_win_game:
                    self.game_data.current_status = "Winner"
                    self.game_data.inc_win_count()
                    self.reset_game()
            else:
                self.game_data.current_status = "incorrect"
                self.game_data.current_streak = str(0)
                self.game_data.dec_current_count()

                if self.game_data.current_attempts == str(0):
                    self.game_data.current_status = "Game Over"
                    self.game_data.inc_lose_count()
                    self.reset_game()

        self.sync_difficulty_for_single_player()
        self.get_new_puzzle_for_single_player()

    def check_result_for_practice(self, user_input):
        user_input = str(user_input)
        if user_input != "":
            if self.game_data.p_correct_answer == user_input:
                self.game_data.current_status = "correct"
                self.game_data.inc_correct_answer_count()
                self.game_data.get_motivation_previous_correct_answer()
                # TODO Save to profile data
            else:
                self.game_data.current_status = "incorrect"
                self.game_data.inc_incorrect_answer_count()
                self.game_data.previous_correct_answer = self.game_data.p_correct_answer
                # TODO Save to profile data
        self.sync_difficulty_for_practice()
        self.get_new_puzzle_for_practice()

    def sync_difficulty_for_single_player(self):
        self.puzzle_controller.puzzle_data.difficulty = self.game_data.current_single_player_difficulty
        self.puzzle_controller.puzzle_data.update_max_value()

    def sync_difficulty_for_practice(self):
        self.puzzle_controller.puzzle_data.difficulty = ['easy', 'medium', 'hard', 'insane'][random.randint(0, 3)]
        self.puzzle_controller.puzzle_data.update_max_value()

    def reset_game(self):
        # self.game_data.current_single_player_difficulty = "easy"
        # self.game_data.current_attempts = str(3)
        self.game_data.current_streak = str(0)
        self.game_data.set_initial_values()
        self.sync_difficulty_for_single_player()
        self.get_new_puzzle_for_single_player()

    def get_new_puzzle_for_single_player(self):
        self.puzzle_controller.generate_new_math_puzzle()
        self.game_data.sync_puzzle_data_to_game_data_for_single_player(self.puzzle_controller.puzzle_data)

    def get_new_puzzle_for_practice(self):
        self.puzzle_controller.generate_new_math_puzzle()
        self.game_data.sync_puzzle_data_to_game_data_for_practice(self.puzzle_controller.puzzle_data)

    def sync_game_data(self, user):
        if isinstance(user, USER_DATA):
            user.user_current_attempts = self.game_data.current_attempts
            user.user_current_streak = self.game_data.current_streak
            user.user_current_difficulty = self.game_data.current_single_player_difficulty
            user.user_win_count = self.game_data.current_win_count
            user.user_lose_count = self.game_data.current_lose_count
            # self.database_controller.save_to_file(user)
            self.database_controller.update_user_data_to_database(user)
