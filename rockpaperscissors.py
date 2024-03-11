import random

def play__game(num_games):
    game_num = 1
    while(game_num <= num_games):
        choices=["rock","paper","scissors"]
        validresponse = False
        while(validresponse == False):
            player = input("Choose rock, paper, scissors:").lower()
            if player == "rock" or player == "paper" or player ==  "scissors": 
                validresponse = True
            print("Fuck you.")
        computer = random.choice(choices)

        print(f"You chose {player}, computer chose {computer}.")

        if player == computer:
            print("It's a tie!!")
        elif player == "rock":
            if computer == "scissors":
                print("You win!!")
            else:
                print("Computer win!!")
        elif player == "paper":
            if computer == "rock":
                print("You win!!")
            else:
                print("Computer wins!!")
        elif player == "scissors":
            if computer == "paper":
                print("You win!!")
            else:
                print("Computer wins!!")
        game_num = game_num + 1
play__game(2)