from user_data import USER_DATA


class USER_CONTROLLER:
    user_data = object()

    def __init__(self):
        self.user_data = USER_DATA()
    
    def user_exists(self, username):
                with open("users.txt","r") as file:
                    users = file.readlines()
                    for user in users:
                        if username in user:
                            return True
                return False

    

    def save_user(self, username, password):
         with open ("users.txt", "a") as file:
              file.write(f"{username},{password}\n")

    def create_user(self, input_username, input_password, input_confirm_password):
        if input_password == input_confirm_password:
            if not self.user_exists(input_username):
                if self.user_data.check_password(input_password):
                    self.user_data.username = input_username
                    self.user_data.password = input_password
                    self.save_user(input_username, input_password)
                    self.user_data.confirmation_status = "User created successfully"
                else:
                    self.user_data.confirmation_status = "Password must contain atleast 8 digits"
            else:
                self.user_data.confirmation_status = "Username already exists"
        else:
            self.user_data.confirmation_status = "Passwords do not match!"

#controller = USER_CONTROLLER()
#controller.create_user("new_user", "secure_password123", "secure_password123")