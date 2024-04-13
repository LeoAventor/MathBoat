from flask import Flask, render_template, request, redirect, url_for

from game_controller import GAME_CONTROLLER
from user_controller import USER_CONTROLLER
from render_controller import RENDER_CONTROLLER


class APPLICATION_CONTROLLER:
    app = Flask(__name__)
    game_controller = object()
    user_controller = object()
    render_controller = object()

    def __init__(self):
        # VARIABLES
        self.game_controller = GAME_CONTROLLER()
        self.user_controller = USER_CONTROLLER()
        self.render_controller = RENDER_CONTROLLER()

        # ENDPOINTS
        self.app.add_url_rule("/", "index", self.index)
        self.app.add_url_rule("/home", "home", self.home)
        self.app.add_url_rule("/login", "login", self.login, methods=['POST', 'GET'])
        self.app.add_url_rule("/sign_up", "sign_up", self.sign_up, methods=['POST', 'GET'])
        self.app.add_url_rule("/profile", "profile", self.profile)
        self.app.add_url_rule("/single_player", "single_player",
                              self.single_player, methods=['POST', 'GET'])

    @staticmethod
    def index():
        return render_template("index.html")

    def home(self):
        if self.user_controller.is_authorized:
            return render_template('home.html')
        else:
            return redirect(url_for('login'))

    def login(self):

        if request.method == 'POST':
            self.user_controller.set_input_data(request.form['username'], request.form['password'])
            self.user_controller.sign_in()
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
                               user_current_attempts=self.render_controller.render_data.user_current_attempts)

    # @app.route("/multiplayer")
    # def multiplayer(self):
    #     return "Todo multiplayer"

    def single_player(self):
        # todo get_current_info()
        # todo update_current_info()

        if request.method == 'POST':
            if request.form['userInput'] != '':
                self.game_controller.check_result(user_input=request.form["userInput"])
                self.game_controller.save_game_date(self.user_controller.user_data)

        self.render_controller.update(self.game_controller.game_data)
        return render_template('single_player.html',
                               current_streak=self.render_controller.render_data.current_streak,
                               current_difficulty=self.render_controller.render_data.current_difficulty,
                               current_attempts=self.render_controller.render_data.current_attempts,
                               first_number=self.render_controller.render_data.first_number,
                               operation_symbol=self.render_controller.render_data.operation_symbol,
                               second_number=self.render_controller.render_data.second_number,
                               equality_symbol=self.render_controller.render_data.equality_symbol,
                               result_number=self.render_controller.render_data.result_number,
                               current_status=self.render_controller.render_data.current_status)

    # @app.route("/practice_mode")
    # def practice_mode(self):
    #     return render_template('practice_mode.html')


if __name__ == "__main__":
    application = APPLICATION_CONTROLLER()
    application.app.run()
