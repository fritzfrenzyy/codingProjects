"""Do I really have to do this"""

import random

computers_guess = random.randint(1,100)
play_again = "y"

def do_guess_round():
    """man"""
    computers_guess = random.randint(1,100)
    play_again = "y"
    while play_again == "y":
        players_guess = input("What is your guess? ")
        if computers_guess == int(players_guess):
            print("Correct!")
            play_again = input("Play again? (y/n) ")
            if play_again == "y":
                print("Okay!")
                do_guess_round()
            elif play_again == "n":
                print("Okay!")
                break
            else:
                print("thats not an answer get out")
                break
        elif computers_guess > int(players_guess):
            print("Too low")
        else:
            print("Too high")
do_guess_round()