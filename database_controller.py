from database_data import DATABASE_DATA
from user_data import USER_DATA


class DATABASE_CONTROLLER:
    database_data = object()
    users_list = dict()

    def __init__(self):
        self.database_data = DATABASE_DATA()

    def load_users(self):
        with open(self.database_data.filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                tmp_data = line.split(',')
                self.users_list[tmp_data[0]] = tmp_data[1].replace("\n", "")

    def save_user(self, user):
        with open(self.database_data.filename, 'a') as file:
            file.write(user.get_user_as_single_string())
