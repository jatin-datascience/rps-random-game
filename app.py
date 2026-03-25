from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0
history = []


def decide_winner(user, computer):
    if user == computer:
        return "draw"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/play", methods=["POST"])
def play():
    global user_score, computer_score

    data = request.get_json()
    user = data["choice"]

    computer = random.choice(choices)
    result = decide_winner(user, computer)

    if result == "user":
        user_score += 1
    elif result == "computer":
        computer_score += 1

    history.append((user, computer, result))

    return jsonify({
        "user": user,
        "computer": computer,
        "result": result,
        "user_score": user_score,
        "computer_score": computer_score
    })


@app.route("/reset", methods=["POST"])
def reset():
    global user_score, computer_score, history
    user_score = 0
    computer_score = 0
    history = []
    return jsonify({"message": "reset"})


if __name__ == "__main__":
    app.run(debug=True)