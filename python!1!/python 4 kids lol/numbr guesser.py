import random

computers_guess = random.randint(1,100)
while True:
    players_guess = input("What is your guess? ")
    if computers_guess == int(players_guess):
        print("Correct!")
        break
    elif computers_guess > int(players_guess):
        print("Too low")
    else:
        print("Too high")