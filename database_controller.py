from database_data import DATABASE_DATA
from user_data import USER_DATA


class DATABASE_CONTROLLER:
    database_data = object()

    def __init__(self):
        self.database_data = DATABASE_DATA()

    def load_user_data_from_database(self, username):
        collection = self.database_data.client.get_collection('Data')
        result = collection.find_one({'username': username})

        return result

    def load_users_from_database(self):
        collection = self.database_data.client.get_collection('Users')
        result = collection.find({})

        tmp_users = dict()
        for data in result:
            tmp_users[data['username']] = data['password']

        return tmp_users

    def save_user_to_database(self, user):
        users_collection = self.database_data.client.get_collection('Users')
        data_collection = self.database_data.client.get_collection('Data')

        if isinstance(user, USER_DATA):

            user_json = {
                "username": user.username,
                "password": user.password,
            }

            user_data_json = {
                "username": user.username,
                "user_win_count": user.user_win_count,
                "user_lose_count": user.user_lose_count,
                "user_current_streak": user.user_current_streak,
                "user_current_difficulty": user.user_current_difficulty,
                "user_current_attempts": user.user_current_attempts
            }

            users_collection.insert_one(user_json)
            data_collection.insert_one(user_data_json)

    def update_user_data_to_database(self, user):
        collection = self.database_data.client.get_collection('Data')

        if isinstance(user, USER_DATA):

            user_new_values_json = {"$set": {
                "user_win_count": user.user_win_count,
                "user_lose_count": user.user_lose_count,
                "user_current_streak": user.user_current_streak,
                "user_current_difficulty": user.user_current_difficulty,
                "user_current_attempts": user.user_current_attempts
            }}

            collection.update_one({'username': user.username}, user_new_values_json)

    # def load_usernames_from_file(self):
    #     if os.path.exists(self.database_data.filename):
    #         with open(self.database_data.filename, 'r') as input_file:
    #             json_dict = json.load(input_file)
    #             input_file.close()
    #
    #             tmp_user_list = dict()
    #             for user in json_dict['users']:
    #                 tmp_user_list[user['username']] = user['password']
    #
    #             return tmp_user_list
    #     else:
    #         return dict()

    # def load_user_form_file(self, username):
    #     with open(self.database_data.filename, 'r') as input_file:
    #         json_dict = json.load(input_file)
    #         input_file.close()
    #
    #     for user in json_dict['users']:
    #         if user['username'] == username:
    #             return user

    # def save_to_file(self, user):
    #     template = dict()
    #     if isinstance(user, USER_DATA):
    #         if os.path.exists(self.database_data.filename):
    #             with open(self.database_data.filename, 'r') as input_file:
    #                 json_dict = json.load(input_file)
    #                 input_file.close()
    #
    #             if user.username in self.load_usernames_from_file().keys():
    #                 for user_data in json_dict['users']:
    #                     if user_data['username'] == user.username:
    #                         user_data['user_current_streak'] = user.user_current_streak
    #                         user_data['user_current_difficulty'] = user.user_current_difficulty
    #                         user_data['user_current_attempts'] = user.user_current_attempts
    #                         user_data['user_win_count'] = user.user_win_count
    #                         user_data['user_lose_count'] = user.user_lose_count
    #             else:
    #                 json_dict['users'].append(user)
    #
    #             with open(self.database_data.filename, 'w') as output_file:
    #                 json_string = json.dumps(json_dict, cls=USER_ENCODER, indent=4)
    #                 output_file.write(json_string)
    #                 output_file.close()
    #         else:
    #             template['users'] = [user]
    #             json_string = json.dumps(template, cls=USER_ENCODER, indent=4)
    #             with open(self.database_data.filename, 'w') as output_file:
    #                 output_file.write(json_string)
    #                 output_file.close()
