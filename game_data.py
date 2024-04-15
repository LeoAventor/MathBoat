import random


class GAME_DATA:
    # Common fields
    current_streak = str()  # Single player, Profile
    current_single_player_difficulty = str()  # Single player, Profile
    current_attempts = str()  # Single player, Profile
    current_status = str()  # Single player, Practice

    # Single player fields
    first_number = str()
    operation_symbol = str()
    second_number = str()
    equality_symbol = str()
    result_number = str()
    correct_answer = str()

    # Single player fields
    # first_number = str()
    # operation_symbol = str()
    # second_number = str()
    # equality_symbol = str()
    # result_number = str()
    # correct_answer = str()

    # Profile fields
    current_win_count = str()
    current_lose_count = str()

    # Practice
    correct_answer_count = str()
    incorrect_answer_count = str()
    previous_correct_answer = str()

    def __init__(self):
        # Single player fields
        self.current_streak = str(0)
        self.current_single_player_difficulty = "easy"
        self.current_attempts = str(3)
        # Profile fields
        self.current_lose_count = str(0)
        self.current_win_count = str(0)
        # Practice fields
        self.correct_answer_count = str(0)
        self.incorrect_answer_count = str(0)
        self.previous_correct_answer = "None"
        # Common fields
        self.current_status = "Welcome"

    def map_puzzle_data_to_render_data(self, puzzle_data):
        # Mappings | Puzzle data -> Render data
        self.first_number = puzzle_data.first_number
        self.operation_symbol = puzzle_data.operation_symbol
        self.second_number = puzzle_data.second_number
        self.equality_symbol = puzzle_data.equality_symbol
        self.result_number = puzzle_data.result_number
        self.correct_answer = puzzle_data.correct_answer

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
