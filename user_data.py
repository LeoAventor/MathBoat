class USER_DATA:
    username = str()
    password = str()
    sign_up_confirmation_status = str()
    sign_in_confirmation_status = str()

    def __init__(self):
        self.username = "Username"
        self.password = "Password"
        self.sign_up_confirmation_status = "Please register new user!"
        self.sign_in_confirmation_status = "Welcome, please enter your credentials"

    @staticmethod
    def check_password(input_password):
        if len(input_password) < 8:
            return False
        return True

    def get_user_as_single_string(self):
        return self.username + ',' + self.password
