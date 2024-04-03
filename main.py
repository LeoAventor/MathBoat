from flask import Flask, render_template, redirect, url_for, request
from game_controller import GAME_CONTROLLER


class APPLICATION_CONTROLLER:
    app = Flask(__name__)
    game_controller = object()

    def __init__(self):
        # VARIABLES
        self.game_controller = GAME_CONTROLLER()

        # ENDPOINTS
        self.app.add_url_rule("/", "home", self.home)
        self.app.add_url_rule("/profile", "profile", self.profile)
        self.app.add_url_rule("/single_player", "single_player", self.single_player, methods=['POST', 'GET'])

    @staticmethod
    def home():
        return render_template('home.html')

    @staticmethod
    def profile():
        return render_template('profile.html', bestStreak=10)

    @app.route("/multiplayer")
    def multiplayer(self):
        return "Todo multiplayer"

    def single_player(self):
        # todo get_current_info()
        # todo update_current_info()
        # todo generate_new_math_puzzle()
        # todo check_result()

        if request.method == 'POST':
            if request.form['userInput'] != '':
                self.game_controller.check_result(user_input=request.form["userInput"])

        # todo check_result()
        return render_template('single_player.html',
                               currentStreak=self.game_controller.game_data.current_streak,
                               currentLevel=self.game_controller.game_data.current_difficulty,
                               currentCount=self.game_controller.game_data.current_count,
                               firstNumber=self.game_controller.game_data.first_number,
                               signSymbol=self.game_controller.game_data.operation_symbol,
                               secondNumber=self.game_controller.game_data.second_number,
                               equalitySymbol=self.game_controller.game_data.equality_symbol,
                               resultNumber=self.game_controller.game_data.result_number,
                               correctStatus=self.game_controller.game_data.current_status)

    @app.route("/practice_mode")
    def practice_mode(self):
        return render_template('practice_mode.html')


if __name__ == "__main__":
    application = APPLICATION_CONTROLLER()
    application.app.run()
