class RENDER_DATA:
    # single player page data
    current_streak = str()
    current_level = str()
    current_count = str()
    first_number = str()
    sign_symbol = str()
    second_number = str()
    equality_symbol = str()
    result_number = str()
    correct_answer = str()
    current_status = str()

    def __init__(self):
        self.current_count = str(3)
        self.current_status = "Welcome"

    def map_puzzle_data_to_render_data(self, puzzle_data):
        # Mappings | Puzzle data -> Render data
        self.first_number = puzzle_data.first_number
        self.sign_symbol = puzzle_data.sign_symbol
        self.second_number = puzzle_data.second_number
        self.equality_symbol = puzzle_data.equality_symbol
        self.result_number = puzzle_data.result_number
        self.correct_answer = puzzle_data.correct_answer
