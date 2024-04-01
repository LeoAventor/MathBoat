from flask import Flask, render_template, redirect, url_for, request
from logic_controller import LOGIC_CONTROLLER


class WEB_CONTROLLER:
    app = Flask(__name__)

    logic = LOGIC_CONTROLLER()

    def __init__(self):
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
                self.logic.check_result(user_input=request.form["userInput"])

        # todo check_result()
        return render_template('single_player.html',
                               currentStreak=self.logic.render_data.current_streak,
                               currentLevel=self.logic.render_data.current_level,
                               currentCount=self.logic.render_data.current_count,
                               firstNumber=self.logic.render_data.first_number,
                               signSymbol=self.logic.render_data.sign_symbol,
                               secondNumber=self.logic.render_data.second_number,
                               equalitySymbol=self.logic.render_data.equality_symbol,
                               resultNumber=self.logic.render_data.result_number,
                               correctStatus=self.logic.render_data.current_status)

    @app.route("/practice_mode")
    def practice_mode(self):
        return render_template('practice_mode.html')


if __name__ == "__main__":
    application = WEB_CONTROLLER()
    application.app.run()
