import random
choices=["rock","paper","scissor"]
user_score=0
computer_score=0
history=[]
def get_computer_choice():
    return random.choice(choices)

def get_user_choice():
    while True:
        user=input("Enter rock,Paper , Scissor : ").lower()
        if user in choices:
            return user
        else:
            print("YOU enter a Invalid text")

def decide_winner(user,computer):
    if user == computer:
        return "draw"
    elif  (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"



def play_game():
    global user_score , computer_score
    user = get_user_choice()
    computer = get_computer_choice()
    print(f"Your choice is : {user}")
    print(f"Computer choice is : {computer}")
    result = decide_winner(user,computer)
    if result == "draw":
        print("🤝 It's a draw!")
    elif result == "user":
        print("✅ You win this round!")
        user_score += 1
    else:
        print("❌ Computer wins this round!")
        computer_score += 1
    history.append((user, computer, result))
    

# Function to save history to file
def save_history():
    with open("rps_history.txt", "a") as file:
        for entry in history:
            file.write(f"User: {entry[0]}, Computer: {entry[1]}, Result: {entry[2]}\n")
    print("📁 History saved to file.")

def view_stats():
    print("\n📊 Match History:")
    for i, entry in enumerate(history, 1):
        print(f"{i}. You: {entry[0]}, Computer: {entry[1]}, Result: {entry[2]}")


# Main menu
def main():
    while True:
        print("\n🎮 RPS R.A.N.D.O.M")
        print("1. Play Game")
        print("2. View Stats")
        print("3. Save History")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            play_game()
        elif choice == "2":
            view_stats()
        elif choice == "3":
            save_history()
        elif choice == "4":
            print("👋 Exiting game. Goodbye!")
            break
        else:
            print("❌ Invalid choice!")
main()
