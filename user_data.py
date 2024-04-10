class USER_DATA:
    username = str()
    password = str()
    confirmation_status = str()

    def __init__(self):
        self.username = "Username"
        self.password = "Password"
        self.confirmation_status = "Please register new user!"

    @staticmethod
    def check_password(input_password):
        if len(input_password) < 8:
            return False

        return True
