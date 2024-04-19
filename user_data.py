from properties import PROPERTIES


class USER_DATA:
    properties = object()

    username = str()
    password = str()
    user_win_count = str()
    user_lose_count = str()
    user_current_streak = str()
    user_current_difficulty = str()
    user_current_attempts = str()
    sign_up_confirmation_status = str()
    sign_in_confirmation_status = str()

    def __init__(self):
        self.properties = PROPERTIES()
        # self.username = "Username"
        # self.password = "Password"
        self.sign_up_confirmation_status = self.properties.sign_up_confirmation_status
        self.sign_in_confirmation_status = self.properties.sign_in_confirmation_status

    @staticmethod
    def check_password(input_password):
        if len(input_password) < 8:
            return False
        return True

    # def get_user_as_single_string(self):
    #     return self.username + ',' + self.password
