import random

options = ("rock" , "paper" , "scissors")
running = True

while running == True:
    player = None
    Computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice(rock , paper , scissors):")

    print(f"Player: {player}")
    print(f"Computer: {Computer}")

    if player == Computer:
        print("It's a Tie!")
    elif player == "rock" and Computer == "scissors":
        print("You are Winner")
    elif player == "paper" and Computer == "rock":
        print("You are Winner!")
    elif player == "scissors" and Computer =="paper":
        print("You are Winner!")
    else:
        print("You Lose!")
    if not input("Play again? (y/n): ").lower()== "y":
        running = False
print("Thanks for Playing!")