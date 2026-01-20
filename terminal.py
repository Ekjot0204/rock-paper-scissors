import random

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

user_score = 0
computer_score = 0

print("🎮 Rock Paper Scissors Game 🎮")

while True:
    user = input("Enter rock, paper, or scissors: ").lower()

    if user not in choices:
        print("❌ Wrong choice. Try again.\n")
        continue

    computer = get_computer_choice()
    result = decide_winner(user, computer)

    print(f"\nYou chose: {user.capitalize()} {emoji[user]}")
    print(f"Computer chose: {computer.capitalize()} {emoji[computer]}")

    if result == "draw":
        print("🤝 It's a DRAW!")
    elif result == "win":
        print("🎉 YOU WIN!")
        user_score += 1
    else:
        print("💥 YOU LOSE!")
        computer_score += 1

    print(f"📊 Score → You: {user_score} | Computer: {computer_score}\n")

    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        print("Thank you for playing!")
        break
