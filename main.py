from flask import Flask, render_template, redirect, url_for, request
from game_rules import LOGIC_CONTROLLER


class WEB_CONTROLLER:
    app = Flask(__name__)

    logic = LOGIC_CONTROLLER()

    is_initial = False
    render_data = set()

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

        if not self.is_initial:
            self.is_initial = True
            self.logic.set_initial_data()
            self.render_data = self.logic.render_data

        if request.method == 'POST':
            self.logic.check_result(user_input=request.form["userInput"])

        # todo check_result()

        return render_template('single_player.html',
                               currentStreak=self.render_data["currentStreak"],
                               currentLevel=self.render_data["currentLevel"],
                               currentCount=self.render_data["currentCount"],
                               firstNumber=self.render_data["firstNumber"],
                               signSymbol=self.render_data["signSymbol"],
                               secondNumber=self.render_data["secondNumber"],
                               equalitySymbol=self.render_data["equalitySymbol"],
                               resultNumber=self.render_data["resultNumber"],
                               correctStatus=self.render_data["correctStatus"])

    @app.route("/practice_mode")
    def practice_mode(self):
        return render_template('practice_mode.html')


if __name__ == "__main__":
    application = WEB_CONTROLLER()
    application.app.run()
