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
        with open('languages\\' + self.current_language + '.properties') as file:
            lines = file.readlines()
            for line in lines:
                field = line.split('=', 1)
                field[1].replace('\n', '')
                match field[0]:
                    case 'profile':
                        self.language_data.profile = field[1]
                    case 'single_player':
                        self.language_data.profile = field[1]
                    case 'quests':
                        self.language_data.quests = field[1]

    def change_language(self, language):
        self.current_language = language
        self.set_language()

    def set_lv(self):
        self.current_language = 'lv'
        self.set_language()

    def set_en(self):
        self.current_language = 'en'
        self.set_language()
