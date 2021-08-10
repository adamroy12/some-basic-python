computer_choice = "paper"

user_choice = input("rock, paper, or scissors?\n")

if computer_choice == user_choice:
    print("Tie")
elif (computer_choice == "rock" and user_choice == "paper") or (computer_choice == "paper" and user_choice == "scissors") or (computer_choice == "scissors" and user_choice == "rock"):
    print("You win")
elif (computer_choice == "paper" and user_choice == "rock") or (computer_choice == "scissors" and user_choice == "paper") or (computer_choice == "rock" and user_choice == "scissors"):
    print("You lose")