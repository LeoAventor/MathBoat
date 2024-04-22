from language_data import LANGUAGE_DATA
from properties import PROPERTIES


class LANGUAGE_CONTROLLER:
    properties = object()
    language_data = object()
    current_language = str()

    def __init__(self):
        self.properties = PROPERTIES()
        self.language_data = LANGUAGE_DATA()
        self.current_language = self.properties.initial_language
        self.set_language()

    def set_language(self):
        with open('languages\\' + self.current_language + '.properties', 'r', encoding="utf8") as file:
            lines = file.readlines()
            for line in lines:
                field = str(line).split('=', 1)
                field[1].replace('\n', '')
                match field[0]:
                    case 'menu':
                        self.language_data.menu = field[1]
                    case 'race':
                        self.language_data.race = field[1]
                    case 'profile':
                        self.language_data.profile = field[1]
                    case 'single_player':
                        self.language_data.single_player = field[1]
                    case 'quests':
                        self.language_data.quests = field[1]
                    case 'practice':
                        self.language_data.practice = field[1]
                    case 'language':
                        self.language_data.language = field[1]
                    case 'english':
                        self.language_data.english = field[1]
                    case 'latvian':
                        self.language_data.latvian = field[1]
                    case 'records':
                        self.language_data.records = field[1]
                    case 'win_count_txt':
                        self.language_data.win_count_txt = field[1]
                    case 'lose_count_txt':
                        self.language_data.lose_count_txt = field[1]
                    case 'current_state':
                        self.language_data.current_state = field[1]
                    case 'current_difficulty':
                        self.language_data.current_difficulty = field[1]
                    case 'current_streak':
                        self.language_data.current_streak = field[1]
                    case 'current_attempts':
                        self.language_data.current_attempts = field[1]
                    case 'correct_answer_count_txt':
                        self.language_data.correct_answer_count_txt = field[1]
                    case 'incorrect_answer_count_txt':
                        self.language_data.incorrect_answer_count_txt = field[1]
                    case 'previous_correct_answer_txt':
                        self.language_data.previous_correct_answer_txt = field[1]
                    case 'submit':
                        self.language_data.submit = field[1]
                    # case 'current_status':
                    #     self.language_data.current_status = field[1]
                    case 'home':
                        self.language_data.home = field[1]
                    case 'select_quest':
                        self.language_data.select_quest = field[1]
                    case 'quest':
                        self.language_data.quest = field[1]
                    case 'next':
                        self.language_data.next = field[1]

    def change_language(self, language):
        self.current_language = language
        self.set_language()

    def set_lv(self):
        self.current_language = 'lv'
        self.set_language()

    def set_en(self):
        self.current_language = 'en'
        self.set_language()

    def set_current_status(self, current_status):
        if self.current_language == 'lv':
            match self.language_data.current_status:
                case "correct":
                    self.language_data.current_status = 'Pareizi'
                
    def user_current_difficulty(self, user_current_difficulty):
            if self.current_language == 'lv':
                match self.language_data.user_current_difficulty:
                    case "easy":
                        self.language_data.user_current_difficulty = 'viegls'
                    case "medium":
                        self.language_data.user_current_difficulty = 'vidējs'
                    case "hard":
                        self.language_data.user_current_difficulty = 'grūts'
                    case "insane":
                        self.language_data.user_current_difficulty = 'ļoti_grūts'

                   