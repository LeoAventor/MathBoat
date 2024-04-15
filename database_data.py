class DATABASE_DATA:
    filename = str()
    filename2 = 'users.txt'
    # cryption_password = str()

    def __init__(self):
        with open('config.properties', 'r') as file:
            lines = file.readlines()
            for line in lines:
                tmp_data = line.split('=')
                match tmp_data[0]:
                    case 'users_data_file_name':
                        self.filename = tmp_data[1].replace("\n", '')
