class GAME_DATA:
    # single_player page data
    # profile       page data
    current_streak = str()
    current_difficulty = str()
    current_attempts = str()

    # single player page data
    first_number = str()
    operation_symbol = str()
    second_number = str()
    equality_symbol = str()
    result_number = str()
    correct_answer = str()
    current_status = str()

    # profile page data
    current_win_count = str()
    current_lose_count = str()

    def __init__(self):
        self.current_streak = str(0)
        self.current_difficulty = "easy"
        self.current_attempts = str(3)
        self.current_status = "Welcome"
        self.current_lose_count = str(0)
        self.current_win_count = str(0)

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
        match self.current_difficulty:
            case "easy":
                self.current_difficulty = "medium"
            case "medium":
                self.current_difficulty = "hard"
            case "hard":
                self.current_difficulty = "insane"

    def dec_current_count(self):
        self.current_attempts = str(int(self.current_attempts) - 1)

    def inc_win_count(self):
        self.current_win_count = str(int(self.current_win_count) + 1)

    def inc_lose_count(self):
        self.current_lose_count = str(int(self.current_lose_count) + 1)
