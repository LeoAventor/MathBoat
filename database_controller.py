from database_data import DATABASE_DATA
from user_data import USER_DATA
from user_encoder import USER_ENCODER
import pymongo
import json
import bson
import os


class DATABASE_CONTROLLER:
    database_data = object()

    def __init__(self):
        self.database_data = DATABASE_DATA()

    # def load_users_from_database(self):
    #     client = pymongo.MongoClient(self.database_data.connection_string)
    #     db = client.get_database('Mafia')
    #     collection = db.get_collection('Test')
    #     result = collection.find_one()
    #     print(result)

    def load_usernames_from_file(self):
        if os.path.exists(self.database_data.filename):
            with open(self.database_data.filename, 'r') as input_file:
                json_dict = json.load(input_file)
                input_file.close()

                tmp_user_list = dict()
                for user in json_dict['users']:
                    tmp_user_list[user['username']] = user['password']

                return tmp_user_list
        else:
            return dict()

    def load_user_form_file(self, username):
        with open(self.database_data.filename, 'r') as input_file:
            json_dict = json.load(input_file)
            input_file.close()

        for user in json_dict['users']:
            if user['username'] == username:
                return user

    def save_to_file(self, user):
        template = dict()
        if isinstance(user, USER_DATA):
            if os.path.exists(self.database_data.filename):
                with open(self.database_data.filename, 'r') as input_file:
                    json_dict = json.load(input_file)
                    input_file.close()

                if user.username in self.load_usernames_from_file().keys():
                    for user_data in json_dict['users']:
                        if user_data['username'] == user.username:
                            user_data['user_current_streak'] = user.user_current_streak
                            user_data['user_current_difficulty'] = user.user_current_difficulty
                            user_data['user_current_attempts'] = user.user_current_attempts
                            user_data['user_win_count'] = user.user_win_count
                            user_data['user_lose_count'] = user.user_lose_count
                else:
                    json_dict['users'].append(user)

                with open(self.database_data.filename, 'w') as output_file:
                    json_string = json.dumps(json_dict, cls=USER_ENCODER, indent=4)
                    output_file.write(json_string)
                    output_file.close()
            else:
                template['users'] = [user]
                json_string = json.dumps(template, cls=USER_ENCODER, indent=4)
                with open(self.database_data.filename, 'w') as output_file:
                    output_file.write(json_string)
                    output_file.close()

