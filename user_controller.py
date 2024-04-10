from user_data import USER_DATA


class USER_CONTROLLER:
    user_data = object()

    def __init__(self):
        self.user_data = USER_DATA()

    def create_user(self, input_username, input_password, input_confirm_password):
        if input_password == input_confirm_password:
            # TODO check if exists username
            if self.user_data.check_password(input_password):
                self.user_data.username = input_username
                self.user_data.password = input_password

                # TODO save user
                # fin = open("users.txt", "w")
            else:
                self.user_data.confirmation_status = "Please enter correct password!"
        else:
            self.user_data.confirmation_status = "Please enter same passwords!"
