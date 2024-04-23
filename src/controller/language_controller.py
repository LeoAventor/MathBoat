from src.data.language_data import LANGUAGE_DATA
from src.properties import PROPERTIES

import os


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
        with open(os.path.dirname(__file__) + '\\..\\..\\languages\\' + self.current_language + '.properties', 'r',
                  encoding="utf8") as file:
            lines = file.readlines()
            for line in lines:
                fields = str(line).split('=', 1)
                fields[1].replace('\n', '')
                match fields[0]:
                    case 'menu_txt':
                        self.language_data.menu_txt = fields[1]
                    case 'race_txt':
                        self.language_data.race_txt = fields[1]
                    case 'profile_txt':
                        self.language_data.profile_txt = fields[1]
                    case 'single_player_txt':
                        self.language_data.single_player_txt = fields[1]
                    case 'quests_txt':
                        self.language_data.quests_txt = fields[1]
                    case 'practice_txt':
                        self.language_data.practice_txt = fields[1]
                    case 'language_txt':
                        self.language_data.language_txt = fields[1]
                    case 'english_txt':
                        self.language_data.english_txt = fields[1]
                    case 'latvian_txt':
                        self.language_data.latvian_txt = fields[1]
                    case 'records_txt':
                        self.language_data.records_txt = fields[1]
                    case 'win_count_txt':
                        self.language_data.win_count_txt = fields[1]
                    case 'lose_count_txt':
                        self.language_data.lose_count_txt = fields[1]
                    case 'current_state_txt':
                        self.language_data.current_state_txt = fields[1]
                    case 'current_difficulty_txt':
                        self.language_data.current_difficulty_txt = fields[1]
                    case 'current_streak_txt':
                        self.language_data.current_streak_txt = fields[1]
                    case 'current_attempts_txt':
                        self.language_data.current_attempts_txt = fields[1]
                    case 'correct_answer_count_txt':
                        self.language_data.correct_answer_count_txt = fields[1]
                    case 'incorrect_answer_count_txt':
                        self.language_data.incorrect_answer_count_txt = fields[1]
                    case 'previous_correct_answer_txt':
                        self.language_data.previous_correct_answer_txt = fields[1]
                    case 'submit_txt':
                        self.language_data.submit_txt = fields[1]
                    case 'home_txt':
                        self.language_data.home_txt = fields[1]
                    case 'select_quest_txt':
                        self.language_data.select_quest_txt = fields[1]
                    case 'quest_txt':
                        self.language_data.quest_txt = fields[1]
                    case 'next_txt':
                        self.language_data.next_txt = fields[1]

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
            match current_status:
                case "correct":
                    self.language_data.current_status = 'Pareizi'
                # TODO other status messages
        else:
            self.language_data.current_status = current_status
                
    def set_user_current_difficulty(self, user_current_difficulty):
        if self.current_language == 'lv':
            match user_current_difficulty:
                case "easy":
                    self.language_data.user_current_difficulty = 'viegls'
                case "medium":
                    self.language_data.user_current_difficulty = 'vidējs'
                case "hard":
                    self.language_data.user_current_difficulty = 'grūts'
                case "insane":
                    self.language_data.user_current_difficulty = 'ļoti_grūts'
        else:
            self.language_data.user_current_difficulty = user_current_difficulty

    def set_previous_correct_answer(self, previous_correct_answer):
        if self.current_language == 'lv':
            match previous_correct_answer:
                case "none":
                    self.language_data.previous_correct_answer = "Nav"
                case "motivation1":
                    self.language_data.motivation = "Labs darbs!"
        else:
            match previous_correct_answer:
                case "none":
                    self.language_data.previous_correct_answer = "None"
                case "motivation1":
                    self.language_data.motivation = "Good Job!"
                # TODO add motivations texts
