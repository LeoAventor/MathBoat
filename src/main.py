import os
from flask import Flask, render_template, request, redirect, url_for

from src.controller.game_controller import GAME_CONTROLLER
from src.controller.user_controller import USER_CONTROLLER
from src.controller.render_controller import RENDER_CONTROLLER
from src.controller.language_controller import LANGUAGE_CONTROLLER


class APPLICATION_CONTROLLER:
    app = object()
    game_controller = object()
    user_controller = object()
    render_controller = object()
    language_controller = object()

    project_path = str()
    templates_path = str()
    static_path = str()

    def __init__(self):
        # VARIABLES
        self.game_controller = GAME_CONTROLLER()
        self.user_controller = USER_CONTROLLER()
        self.render_controller = RENDER_CONTROLLER()
        self.language_controller = LANGUAGE_CONTROLLER()

        self.project_path = os.path.dirname(__file__)
        self.templates_path = self.project_path + "\\..\\templates"
        self.static_path = self.project_path + "\\..\\static"
        self.app = Flask(__name__, template_folder=self.templates_path, static_folder=self.static_path)

        # ENDPOINTS
        self.app.add_url_rule("/", "index", self.index)
        self.app.add_url_rule("/home", "home", self.home, methods=['POST', 'GET'])
        self.app.add_url_rule("/login", "login", self.login, methods=['POST', 'GET'])
        self.app.add_url_rule("/sign_up", "sign_up", self.sign_up, methods=['POST', 'GET'])
        self.app.add_url_rule("/profile", "profile", self.profile)
        self.app.add_url_rule("/single_player", "single_player",
                              self.single_player, methods=['POST', 'GET'])
        self.app.add_url_rule("/practice", "practice", self.practice, methods=['POST', 'GET'])
        self.app.add_url_rule("/under_maintenance", "under_maintenance", self.under_maintenance)

    @staticmethod
    def get_html_file_path(file_name):
        return file_name + ".html"

    def index(self):
        return render_template(self.get_html_file_path("index"))

    def under_maintenance(self):
        if self.user_controller.is_authorized:
                if request.method == 'POST':
                    if request.form['language_button'] == 'lv':
                        self.language_controller.set_lv()
                    elif request.form['language_button'] == 'en':
                        self.language_controller.set_en()
        return render_template(self.get_html_file_path("under_maintenance"),
                               under_maintenance_txt=self.language_controller.language_data.under_maintenance_txt,
                               under_maintenance_info_txt=self.language_controller.language_data.under_maintenance_info_txt)


    def home(self):
        if self.user_controller.is_authorized:
            if request.method == 'POST':
                if request.form['language_button'] == 'lv':
                    self.language_controller.set_lv()
                elif request.form['language_button'] == 'en':
                    self.language_controller.set_en()

            return render_template(self.get_html_file_path("home"),
                                   home_txt=self.language_controller.language_data.home_txt,
                                   race_txt=self.language_controller.language_data.race_txt,
                                   profile_txt=self.language_controller.language_data.profile_txt,
                                   single_player_txt=self.language_controller.language_data.single_player_txt,
                                   quests_txt=self.language_controller.language_data.quests_txt,
                                   practice_txt=self.language_controller.language_data.practice_txt,
                                   language_txt=self.language_controller.language_data.language_txt,
                                   english_txt=self.language_controller.language_data.english_txt,
                                   latvian_txt=self.language_controller.language_data.latvian_txt)
        else:
            return redirect(url_for('login'))

    def login(self):
        if request.method == 'POST':
            self.user_controller.set_input_data(request.form['username'], request.form['password'])
            self.user_controller.sign_in()
            self.user_controller.sync_game_data(self.game_controller.game_data)
            return redirect(url_for('home'))

        self.render_controller.update(self.user_controller.user_data)

        return render_template(self.get_html_file_path("login"),
                               username=self.render_controller.render_data.username,
                               password=self.render_controller.render_data.password,
                               sign_in_confirmation_status=
                               self.render_controller.render_data.sign_in_confirmation_status)

    def sign_up(self):
        if request.method == 'POST':
            self.user_controller.set_input_data(request.form['username'], request.form['password'],
                                                request.form['confirm_password'])
            self.user_controller.sign_up()

        self.render_controller.update(self.user_controller.user_data)
        return render_template(self.get_html_file_path("sign_up"),
                               username=self.render_controller.render_data.username,
                               password=self.render_controller.render_data.password,
                               sign_up_confirmation_status=
                               self.render_controller.render_data.sign_up_confirmation_status)

    def profile(self):
        self.render_controller.update(self.user_controller.user_data)
        self.language_controller.set_current_status(self.render_controller.render_data.current_status)
        self.language_controller.set_user_current_difficulty(self.render_controller.render_data.user_current_difficulty)
        return render_template(self.get_html_file_path("profile"),
                               user_win_count=self.render_controller.render_data.user_win_count,
                               user_lose_count=self.render_controller.render_data.user_lose_count,
                               user_current_streak=self.render_controller.render_data.user_current_streak,
                               user_current_attempts=self.render_controller.render_data.user_current_attempts,
                               user_current_difficulty=
                               self.language_controller.language_data.user_current_difficulty,
                               records_txt=self.language_controller.language_data.records_txt,
                               win_count_txt=self.language_controller.language_data.win_count_txt,
                               lose_count_txt=self.language_controller.language_data.lose_count_txt,
                               current_state_txt=self.language_controller.language_data.current_state_txt,
                               current_difficulty_txt=self.language_controller.language_data.current_difficulty_txt,
                               current_streak_txt=self.language_controller.language_data.current_streak_txt,
                               current_attempts_txt=self.language_controller.language_data.current_attempts_txt,
                               profile_txt=self.language_controller.language_data.profile_txt,
                               home_txt=self.language_controller.language_data.home_txt)

    def single_player(self):
        if request.method == 'POST':
            if request.form['userInput'] != '':
                self.game_controller.check_result_for_single_player(user_input=request.form["userInput"])
                self.game_controller.sync_game_data(self.user_controller.user_data)

        self.render_controller.update(self.game_controller.game_data)
        self.language_controller.set_current_status(self.render_controller.render_data.current_status)
        return render_template(self.get_html_file_path("single_player"),
                               current_streak=self.render_controller.render_data.current_streak,
                               current_difficulty=self.render_controller.render_data.current_single_player_difficulty,
                               current_attempts=self.render_controller.render_data.current_attempts,
                               first_number=self.render_controller.render_data.first_number,
                               operation_symbol=self.render_controller.render_data.operation_symbol,
                               second_number=self.render_controller.render_data.second_number,
                               equality_symbol=self.render_controller.render_data.equality_symbol,
                               result_number=self.render_controller.render_data.result_number,
                               current_status=self.language_controller.language_data.current_status,
                               submit_txt=self.language_controller.language_data.submit_txt,
                               home_txt=self.language_controller.language_data.home_txt,
                               current_streak_txt=self.language_controller.language_data.current_streak_txt,
                               current_difficulty_txt=self.language_controller.language_data.current_difficulty_txt,
                               current_attempts_txt=self.language_controller.language_data.current_attempts_txt)

    def practice(self):
        if request.method == 'POST':
            if request.form['userInput'] != '':
                self.game_controller.check_result_for_practice(user_input=request.form["userInput"])

        self.render_controller.update(self.game_controller.game_data, "practice")
        self.language_controller.set_current_status(self.render_controller.render_data.current_status)
        return render_template(self.get_html_file_path("practice"),
                               correct_answer_count=self.render_controller.render_data.correct_answer_count,
                               incorrect_answer_count=self.render_controller.render_data.incorrect_answer_count,
                               previous_correct_answer=self.render_controller.render_data.previous_correct_answer,
                               first_number=self.render_controller.render_data.first_number,
                               operation_symbol=self.render_controller.render_data.operation_symbol,
                               second_number=self.render_controller.render_data.second_number,
                               equality_symbol=self.render_controller.render_data.equality_symbol,
                               result_number=self.render_controller.render_data.result_number,
                               correct_answer_count_txt=self.language_controller.language_data.correct_answer_count_txt,
                               incorrect_answer_count_txt=
                               self.language_controller.language_data.incorrect_answer_count_txt,
                               previous_correct_answer_txt=
                               self.language_controller.language_data.previous_correct_answer_txt,
                               submit_txt=self.language_controller.language_data.submit_txt,
                               current_status=self.language_controller.language_data.current_status,
                               home_txt=self.language_controller.language_data.home_txt)


if __name__ == "__main__":
    application = APPLICATION_CONTROLLER()
    application.app.run()

# TODO Quests Mode
# TODO Multiplayer Mode
