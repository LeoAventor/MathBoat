from user_data import USER_DATA
from game_data import GAME_DATA
from database_controller import DATABASE_CONTROLLER
from properties import PROPERTIES


class USER_CONTROLLER:
    # Local use variables
    input_username = str()
    input_password = str()
    input_confirm_password = str()
    users_list = dict()
    is_authorized = bool()

    # Class instances
    user_data = object()
    database_controller = object()
    properties = object()

    def __init__(self):
        self.user_data = USER_DATA()
        self.database_controller = DATABASE_CONTROLLER()
        self.properties = PROPERTIES()

        self.is_authorized = self.properties.is_authorized

    def sign_in(self):
        # self.users_list = self.database_controller.load_usernames_from_file()
        self.users_list = self.database_controller.load_users_from_database()
        if self.input_username in self.users_list.keys():
            if self.input_password == self.users_list[self.input_username]:
                self.is_authorized = True
                self.load_user()
            else:
                self.user_data.sign_in_confirmation_status = "Wrong password!"
        else:
            self.user_data.sign_up_confirmation_status = "Username does not exist!"

    def sign_up(self):
        # self.users_list = self.database_controller.load_usernames_from_file()
        self.users_list = self.database_controller.load_users_from_database()
        if self.input_password == self.input_confirm_password:
            if self.input_username not in self.users_list.keys():
                if self.user_data.check_password(self.input_password):
                    self.update_current_user()
                    self.database_controller.save_user_to_database(self.user_data)
                    self.user_data.sign_up_confirmation_status = "User created successfully"
                else:
                    self.user_data.sign_up_confirmation_status = "Password must contain at least 8 digit's"
            else:
                self.user_data.sign_up_confirmation_status = "Username already exists"
        else:
            self.user_data.sign_up_confirmation_status = "Password's do not match!"

    def update_current_user(self):
        self.user_data.username = self.input_username
        self.user_data.password = self.input_password
        self.user_data.user_current_streak = str(0)
        self.user_data.user_lose_count = str(0)
        self.user_data.user_win_count = str(0)
        self.user_data.user_current_attempts = str(3)
        self.user_data.user_current_difficulty = 'easy'

    def set_input_data(self, input_username, input_password, input_confirm_password=""):
        self.input_username = input_username
        self.input_password = input_password
        self.input_confirm_password = input_confirm_password

    def load_user(self):
        # tmp_user = self.database_controller.load_user_form_file(self.input_username)
        tmp_user = self.database_controller.load_user_data_from_database(self.input_username)
        self.user_data.username = tmp_user['username']
        # self.user_data.password = tmp_user['password']
        self.user_data.user_lose_count = tmp_user['user_lose_count']
        self.user_data.user_win_count = tmp_user['user_win_count']
        self.user_data.user_current_streak = tmp_user['user_current_streak']
        self.user_data.user_current_attempts = tmp_user['user_current_attempts']
        self.user_data.user_current_difficulty = tmp_user['user_current_difficulty']

    def sync_game_data(self, game):
        if isinstance(game, GAME_DATA):
            game.current_attempts = self.user_data.user_current_attempts
            game.current_streak = self.user_data.user_current_streak
            game.current_single_player_difficulty = self.user_data.user_current_difficulty
            game.current_win_count = self.user_data.user_win_count
            game.current_lose_count = self.user_data.user_lose_count
