class GAME_DATA:
    # single player page data
    current_streak = str()
    current_difficulty = str()
    current_count = str()
    first_number = str()
    operation_symbol = str()
    second_number = str()
    equality_symbol = str()
    result_number = str()
    correct_answer = str()
    current_status = str()

    def __init__(self):
        self.current_streak = "0"
        self.current_difficulty = "insane"
        self.current_count = str(3)
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
        match self.current_difficulty:
            case "easy":
                self.current_difficulty = "medium"
            case "medium":
                self.current_difficulty = "hard"
            case "hard":
                self.current_difficulty = "insane"

    def dec_current_count(self):
        self.current_count = str(int(self.current_count) - 1)