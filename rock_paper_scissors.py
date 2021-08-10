import random

computer_choice = random.randint(1,3)

if computer_choice == 1:
    computer_choice = "rock"
elif computer_choice == 2:
    computer_choice = "paper"
elif computer_choice == 3:
    computer_choice = "scissors"

print(computer_choice)

user_choice = input("rock, paper, or scissors?\n")

if computer_choice == user_choice:
    print("Tie")
elif (computer_choice == "rock" and user_choice == "paper") or (computer_choice == "paper" and user_choice == "scissors") or (computer_choice == "scissors" and user_choice == "rock"):
    print("You win")
elif (computer_choice == "paper" and user_choice == "rock") or (computer_choice == "scissors" and user_choice == "paper") or (computer_choice == "rock" and user_choice == "scissors"):
    print("You lose")