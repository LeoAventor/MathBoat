from database_data import DATABASE_DATA
from user_data import USER_DATA
from user_encoder import USER_ENCODER
import json
import os


class DATABASE_CONTROLLER:
    database_data = object()

    def __init__(self):
        self.database_data = DATABASE_DATA()

    def load_users(self):
        tmp_users_list = dict()
        with open(self.database_data.filename2, 'r') as file:
            lines = file.readlines()
            for line in lines:
                tmp_data = line.split(',')
                tmp_users_list[tmp_data[0]] = tmp_data[1].replace("\n", "")

        return tmp_users_list

    def save_user(self, user):
        with open(self.database_data.filename2, 'a') as file:
            file.write(user.get_user_as_single_string())

    def save_to_file(self, user):
        template = dict()
        if isinstance(user, USER_DATA):
            if os.path.exists(self.database_data.filename):
                with open(self.database_data.filename, 'r') as input_file:
                    json_dict = json.load(input_file)
                    input_file.close()

                for user_data in json_dict['users']:
                    if user_data['username'] == user.username:
                        user_data['user_current_streak'] = user.user_current_streak

                with open(self.database_data.filename, 'w') as output_file:
                    json_string = json.dumps(json_dict, indent=4)
                    output_file.write(json_string)
                    output_file.close()
            else:
                template['users'] = [user]
                json_string = json.dumps(template, cls=USER_ENCODER, indent=4)
                with open(self.database_data.filename, 'w') as output_file:
                    output_file.write(json_string)
                    output_file.close()



