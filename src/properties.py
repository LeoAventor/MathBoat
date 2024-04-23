import os


class PROPERTIES:
    connection_string_to_database = str()
    sign_up_confirmation_status = str()
    sign_in_confirmation_status = str()
    is_authorized = bool()
    streak_to_level_up = str()
    streak_to_win_game = str()
    initial_difficulty = str()
    initial_attempts = str()
    easy_max_value = int()
    medium_max_value = int()
    hard_max_value = int()
    insane_max_value = int()
    initial_language = str()

    def __init__(self):
        with open(os.path.dirname(__file__) + '\\..\\resource\\config.properties', 'r') as file:
            lines = file.readlines()
            for line in lines:
                tmp_data = line.split('=', 1)
                match tmp_data[0]:
                    # case 'users_data_file_name':
                    #     self.filename = tmp_data[1].replace("\n", '')
                    case 'connection_string_to_database':
                        self.connection_string_to_database = tmp_data[1].replace("\n", "")
                    case 'sign_up_confirmation_status':
                        self.sign_up_confirmation_status = tmp_data[1].replace("\n", "")
                    case 'sign_in_confirmation_status':
                        self.sign_in_confirmation_status = tmp_data[1].replace("\n", "")
                    case 'is_authorized':
                        self.is_authorized = tmp_data[1].replace("\n", "") == 'True'
                    case 'streak_to_level_up':
                        self.streak_to_level_up = tmp_data[1].replace("\n", "")
                    case 'streak_to_win_game':
                        self.streak_to_win_game = tmp_data[1].replace("\n", "")
                    case 'initial_difficulty':
                        self.initial_difficulty = tmp_data[1].replace("\n", "")
                    case 'initial_attempts':
                        self.initial_attempts = tmp_data[1].replace("\n", "")
                    case 'easy_max_value':
                        self.easy_max_value = int(tmp_data[1].replace("\n", ""))
                    case 'medium_max_value':
                        self.medium_max_value = int(tmp_data[1].replace("\n", ""))
                    case 'hard_max_value':
                        self.hard_max_value = int(tmp_data[1].replace("\n", ""))
                    case 'insane_max_value':
                        self.insane_max_value = int(tmp_data[1].replace("\n", ""))
                    case 'initial_language':
                        self.initial_language = tmp_data[1].replace("\n", "")
