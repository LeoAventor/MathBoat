import random

from properties import PROPERTIES


class GAME_DATA:
    properties = object()

    # Common fields
    current_streak = str()  # Single player, Profile
    current_single_player_difficulty = str()  # Single player, Profile
    current_attempts = str()  # Single player, Profile
    current_status = str()  # Single player, Practice

    # Single player fields
    sp_first_number = str()
    sp_operation_symbol = str()
    sp_second_number = str()
    sp_equality_symbol = str()
    sp_result_number = str()
    sp_correct_answer = str()

    # Practice fields
    p_first_number = str()
    p_operation_symbol = str()
    p_second_number = str()
    p_equality_symbol = str()
    p_result_number = str()
    p_correct_answer = str()

    # Profile fields
    current_win_count = str()
    current_lose_count = str()

    # Practice
    correct_answer_count = str()
    incorrect_answer_count = str()
    previous_correct_answer = str()

    def __init__(self):
        self.properties = PROPERTIES()

        # Single player fields
        self.current_streak = str(0)
        self.set_initial_values()
        # Profile fields
        self.current_lose_count = str(0)
        self.current_win_count = str(0)
        # Practice fields
        self.correct_answer_count = str(0)
        self.incorrect_answer_count = str(0)
        self.previous_correct_answer = "None"
        # Common fields
        self.current_status = "Welcome"

    def set_initial_values(self):
        self.current_single_player_difficulty = self.properties.initial_difficulty
        self.current_attempts = self.properties.initial_attempts

    def sync_puzzle_data_to_game_data_for_single_player(self, puzzle_data):
        # Mapping | Puzzle data -> Game data | Single player
        self.sp_first_number = puzzle_data.first_number
        self.sp_operation_symbol = puzzle_data.operation_symbol
        self.sp_second_number = puzzle_data.second_number
        self.sp_equality_symbol = puzzle_data.equality_symbol
        self.sp_result_number = puzzle_data.result_number
        self.sp_correct_answer = puzzle_data.correct_answer

    def sync_puzzle_data_to_game_data_for_practice(self, puzzle_data):
        # Mapping | Puzzle data -> Game data | Practice
        self.p_first_number = puzzle_data.first_number
        self.p_operation_symbol = puzzle_data.operation_symbol
        self.p_second_number = puzzle_data.second_number
        self.p_equality_symbol = puzzle_data.equality_symbol
        self.p_result_number = puzzle_data.result_number
        self.p_correct_answer = puzzle_data.correct_answer

    def inc_current_streak(self):
        self.current_streak = str(int(self.current_streak) + 1)

    def inc_current_difficulty(self):
        match self.current_single_player_difficulty:
            case "easy":
                self.current_single_player_difficulty = "medium"
            case "medium":
                self.current_single_player_difficulty = "hard"
            case "hard":
                self.current_single_player_difficulty = "insane"

    def dec_current_count(self):
        self.current_attempts = str(int(self.current_attempts) - 1)

    def inc_win_count(self):
        self.current_win_count = str(int(self.current_win_count) + 1)

    def inc_lose_count(self):
        self.current_lose_count = str(int(self.current_lose_count) + 1)

    def inc_correct_answer_count(self):
        self.correct_answer_count = str(int(self.correct_answer_count) + 1)

    def inc_incorrect_answer_count(self):
        self.incorrect_answer_count = str(int(self.incorrect_answer_count) + 1)

    def get_motivation_previous_correct_answer(self):
        motivations = ["Good Job!", "Nice work.", "You got it!"]
        self.previous_correct_answer = motivations[random.randint(0, len(motivations)-1)]
