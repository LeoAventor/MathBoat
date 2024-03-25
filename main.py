from flask import Flask, render_template, redirect, url_for
from math_puzzles import generate_new_math_puzzle
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/profile")
def profile():
    return render_template('profile.html', bestStreak=10)


@app.route("/multiplayer")
def multiplayer():
    return "Todo multiplayer"


@app.route("/singleplayer")
def single_player():
    # todo get_current_info()
    # todo update_current_info()
    # todo generate_new_math_puzzle()
    # todo check_reuslt()
    math_puzzle_data = generate_new_math_puzzle()
    return render_template('singleplayer.html',
                           firstNumber=math_puzzle_data["firstNumber"], signSymbol=math_puzzle_data["signSymbol"],
                           secondNumber="?", equalitySymbol=math_puzzle_data["equalitySymbol"],
                           resultNumber=math_puzzle_data["resultNumber"])

    #return render_template('singleplayer.html',
                           #firstNumber=math_puzzle_data["firstNumber"], signSymbol= "math_sign",
                           #secondNumber="math_puzzle_data["secondNumber"]", equalitySymbol=math_puzzle_data["equalitySymbol"],
                           #resultNumber=math_puzzle_data["resultNumber"])



    #return render_template('singleplayer.html',
                           #firstNumber=math_puzzle_data["firstNumber"], signSymbol=math_puzzle_data["signSymbol"],
                           #secondNumber="math_puzzle_data["secondNumber"]", equalitySymbol=math_puzzle_data["equalitySymbol"],
                           #resultNumber="result_number"

    #return render_template('singleplayer.html',
                           #firstNumber=math_puzzle_data["firstNumber"], signSymbol=math_puzzle_data["signSymbol"],
                           #secondNumber="math_puzzle_data["secondNumber"]", equalitySymbol="<>",
                           #resultNumber=math_puzzle_data["resultNumber"])









@app.route("/practicemode")
def practice_mode():
    return render_template('practicemode.html')





if __name__ == "__main__":
    app.run(debug=True)