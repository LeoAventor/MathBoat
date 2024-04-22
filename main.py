from flask import Flask, render_template, request, redirect, url_for

from game_controller import GAME_CONTROLLER
from user_controller import USER_CONTROLLER
from render_controller import RENDER_CONTROLLER
from language_controller import LANGUAGE_CONTROLLER


class APPLICATION_CONTROLLER:
    app = Flask(__name__)
    game_controller = object()
    user_controller = object()
    render_controller = object()
    language_controller = object()

    def __init__(self):
        # VARIABLES
        self.game_controller = GAME_CONTROLLER()
        self.user_controller = USER_CONTROLLER()
        self.render_controller = RENDER_CONTROLLER()
        self.language_controller = LANGUAGE_CONTROLLER()

        # ENDPOINTS
        self.app.add_url_rule("/", "index", self.index)
        self.app.add_url_rule("/home", "home", self.home, methods=['POST', 'GET'])
        self.app.add_url_rule("/login", "login", self.login, methods=['POST', 'GET'])
        self.app.add_url_rule("/sign_up", "sign_up", self.sign_up, methods=['POST', 'GET'])
        self.app.add_url_rule("/profile", "profile", self.profile)
        self.app.add_url_rule("/single_player", "single_player",
                              self.single_player, methods=['POST', 'GET'])
        self.app.add_url_rule("/practice", "practice", self.practice, methods=['POST', 'GET'])
        self.app.add_url_rule("/quests_task", "quests_task", self.quests_task, methods=['POST', 'GET'])
        self.app.add_url_rule("/quests_level","quests_level", self.quests_level, methods=['POST','GET'])
        #self.app.add_url_rule("/boat_animation","boat_animation", self.boat_animation, methods=['POST','GET'])

    @staticmethod
    def index():
        return render_template("index.html")

    def home(self):
        if self.user_controller.is_authorized:
            if request.method == 'POST':
                if request.form['language_button'] == 'lv':
                    self.language_controller.set_lv()
                elif request.form['language_button'] == 'en':
                    self.language_controller.set_en()

            return render_template('home.html',
                                   home=self.language_controller.language_data.home,
                                   race=self.language_controller.language_data.race,
                                   profile=self.language_controller.language_data.profile,
                                   single_player=self.language_controller.language_data.single_player,
                                   quests=self.language_controller.language_data.quests,
                                   practice=self.language_controller.language_data.practice,
                                   language=self.language_controller.language_data.language,
                                   english=self.language_controller.language_data.english,
                                   latvian=self.language_controller.language_data.latvian)
        else:
            return redirect(url_for('login'))

    def login(self):
        if request.method == 'POST':
            self.user_controller.set_input_data(request.form['username'], request.form['password'])
            self.user_controller.sign_in()
            self.user_controller.sync_game_data(self.game_controller.game_data)
            return redirect(url_for('home'))

        self.render_controller.update(self.user_controller.user_data)

        return render_template('login.html',
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
        return render_template('sign_up.html',
                               username=self.render_controller.render_data.username,
                               password=self.render_controller.render_data.password,
                               sign_up_confirmation_status=
                               self.render_controller.render_data.sign_up_confirmation_status)

    def profile(self):
        self.render_controller.update(self.user_controller.user_data)
        return render_template('profile.html',
                               user_win_count=self.render_controller.render_data.user_win_count,
                               user_lose_count=self.render_controller.render_data.user_lose_count,
                               user_current_difficulty=self.render_controller.render_data.user_current_difficulty,
                               user_current_streak=self.render_controller.render_data.user_current_streak,
                               user_current_attempts=self.render_controller.render_data.user_current_attempts,
                               records=self.language_controller.language_data.records,
                               win_count=self.language_controller.language_data.win_count,
                               lose_count=self.language_controller.language_data.lose_count,
                               current_state=self.language_controller.language_data.current_state,
                               current_difficulty=self.language_controller.language_data.current_difficulty,
                               current_streak=self.language_controller.language_data.current_streak,
                               current_attempts=self.language_controller.language_data.current_attempts)

    # @app.route("/multiplayer")
    # def multiplayer(self):
    #     return "Todo multiplayer"

    def single_player(self):
        if request.method == 'POST':
            if request.form['userInput'] != '':
                self.game_controller.check_result_for_single_player(user_input=request.form["userInput"])
                self.game_controller.sync_game_data(self.user_controller.user_data)

        self.render_controller.update(self.game_controller.game_data)

        return render_template('single_player.html',
                               current_streak=self.render_controller.render_data.current_streak,
                               current_difficulty=self.render_controller.render_data.current_single_player_difficulty,
                               current_attempts=self.render_controller.render_data.current_attempts,
                               first_number=self.render_controller.render_data.first_number,
                               operation_symbol=self.render_controller.render_data.operation_symbol,
                               second_number=self.render_controller.render_data.second_number,
                               equality_symbol=self.render_controller.render_data.equality_symbol,
                               result_number=self.render_controller.render_data.result_number,
                               current_status=self.render_controller.render_data.current_status)

    def practice(self):
        if request.method == 'POST':
            if request.form['userInput'] != '':
                self.game_controller.check_result_for_practice(user_input=request.form["userInput"])
                # self.game_controller.sync_game_data(self.user_controller.user_data)

        self.render_controller.update(self.game_controller.game_data, "practice")
        self.language_controller.set_current_status(self.render_controller.render_data.current_status)
        return render_template('practice.html',
                               correct_answer_count=self.render_controller.render_data.correct_answer_count,
                               incorrect_answer_count=self.render_controller.render_data.incorrect_answer_count,
                               previous_correct_answer=self.render_controller.render_data.previous_correct_answer,
                               first_number=self.render_controller.render_data.first_number,
                               operation_symbol=self.render_controller.render_data.operation_symbol,
                               second_number=self.render_controller.render_data.second_number,
                               equality_symbol=self.render_controller.render_data.equality_symbol,
                               result_number=self.render_controller.render_data.result_number,
                               #current_status=self.render_controller.render_data.current_status,

                               #correct_answer_count=self.language_controller.language_data.correct_answer_count,
                               #incorrect_answer_count=self.language_controller.language_data.incorrect_answer_count,
                               #previous_correct_answer=self.language_controller.language_data.previous_correct_answer,

                               submit=self.language_controller.language_data.submit,
                               current_status=self.language_controller.language_data.current_status,
                               home=self.language_controller.language_data.home)
    
    @staticmethod
    def quests_level():
        return render_template("quests_level.html")
    
    @staticmethod
    def quests_task():
        return render_template("quests_task.html")

    #@staticmethod
    #def quests_task():
       # return render_template("boat_animation.js")

if __name__ == "__main__":
    application = APPLICATION_CONTROLLER()
    application.app.run()
