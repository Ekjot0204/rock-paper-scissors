import random
from flask import Flask, request, render_template

app = Flask(__name__)

user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

emoji = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️"
}

def get_computer_choice():
    return random.choice(choices)

def decide_winner(user, computer):
    if user == computer:
        return "draw"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "win"
    else:
        return "lose"

@app.route("/", methods=["GET", "POST"])
def game():
    global user_score, computer_score
    user = computer = result = ""

    if request.method == "POST":

        if "reset" in request.form:
            user_score = 0
            computer_score = 0
            user = computer = result = ""

        else:
            user = request.form["choice"]
            computer = get_computer_choice()
            outcome = decide_winner(user, computer)

            if outcome == "win":
                user_score += 1
                result = "WIN"
            elif outcome == "lose":
                computer_score += 1
                result = "LOSE"
            else:
                result = "DRAW"

        return render_template(
            "index.html",
            user=user,
            computer=computer,
            result=result,
            emoji=emoji,
            user_score=user_score,
            computer_score=computer_score
        )    
    if __name__ == "__main__":
        app.run(debug=True)

