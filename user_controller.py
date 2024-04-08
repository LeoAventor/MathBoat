from user_data import USER_DATA


class USER_CONTROLLER:
    user_data = object()

    def __init__(self):
        self.user_data = USER_DATA()

    def create_user(self, input_username, input_password):
        self.user_data.username = input_username
        self.user_data.password = input_password
