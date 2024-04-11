from user_data import USER_DATA
from database_controller import DATABASE_CONTROLLER


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

    def __init__(self):
        self.user_data = USER_DATA()
        self.database_controller = DATABASE_CONTROLLER()

        self.is_authorized = False
        self.database_controller.load_users()
        self.users_list = self.database_controller.users_list

    def sign_in(self):
        if self.input_username in self.users_list.keys():
            if self.input_password == self.users_list[self.input_username]:
                self.is_authorized = True
            else:
                self.user_data.sign_in_confirmation_status = "Wrong password!"
        else:
            self.user_data.sign_up_confirmation_status = "Username does not exist!"

    def sign_up(self):
        if self.input_password == self.input_confirm_password:
            if self.input_username not in self.users_list.keys():
                if self.user_data.check_password(self.input_password):
                    self.update_current_user()
                    self.database_controller.save_user(self.user_data)
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

    def set_input_data(self, input_username, input_password, input_confirm_password=""):
        self.input_username = input_username
        self.input_password = input_password
        self.input_confirm_password = input_confirm_password
