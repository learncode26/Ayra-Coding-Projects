# print("ROCK,PAPER,SCISSORS!!!🪨📄✂️")
# player = input("Choose rock, paper, or scissors: ").lower()
# computer = "rock"

# print("Computer chose:", computer)

# if player == computer:
#     print("It's a tie!")

# if player == "rock" and computer == "scissors":
#     print("You win!")

# if player == "paper" and computer == "rock":
#     print("You win!")

# if player == "scissors" and computer == "paper":
#     print("You win!")

# if player == "rock" and computer == "paper":
#     print("Computer wins!")

# if player == "paper" and computer == "scissors":
#     print("Computer wins!")

# if player == "scissors" and computer == "rock":
#     print("Computer wins!")

# player = input("Choose rock, paper, or scissors: ").lower()
# computer = "paper"

# print("Computer chose:", computer)

# if player == computer:
#     print("It's a tie!")

# if player == "rock" and computer == "scissors":
#     print("You win!")

# if player == "paper" and computer == "rock":
#     print("You win!")

# if player == "scissors" and computer == "paper":
#     print("You win!")

# if player == "rock" and computer == "paper":
#     print("Computer wins!")

# if player == "paper" and computer == "scissors":
#     print("Computer wins!")

# if player == "scissors" and computer == "rock":
#     print("Computer wins!")

# player = input("Choose rock, paper, or scissors: ").lower()
# computer = "paper"

# print("Computer chose:", computer)

# if player == computer:
#     print("It's a tie!")

# if player == "rock" and computer == "scissors":
#     print("You win!")

# if player == "paper" and computer == "rock":
#     print("You win!")

# if player == "scissors" and computer == "paper":
#     print("You win!")

# if player == "rock" and computer == "paper":
#     print("Computer wins!")

# if player == "paper" and computer == "scissors":
#     print("Computer wins!")

# if player == "scissors" and computer == "rock":
#     print("Computer wins!")

import random

print("ROCK, PAPER, SCISSORS!!! 🪨📄✂️")
print("Type 'quit' to stop playing.")

choices = ["rock", "paper", "scissors"]

while True:
    player = input("\nChoose rock, paper, or scissors: ").lower()

    if player == "quit":
        print("Thanks for playing!!! Bye!👋")
        break

    if player not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue

    # Computer chooses the move that beats the player
    if player == "rock":
        computer = "paper"
    elif player == "paper":
        computer = "scissors"
    else:
        computer = "rock"

    print("Computer chose:", computer)
    print("Computer wins! 🤖")
rc