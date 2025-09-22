import random

print("ROCK PAPER SCISSORS")
print("1) Rock")
print("2) Paper")
print("3) Scissors")

player = int(input("Pick a number: "))
computer = random.randint(1,3)

print("Rock...")
print("Paper...")
print("Scissors...")
print("SHOOT!")

if computer == 1 and player == 2:
    print("Computer chose ROCK! You chose PAPER! You win!")
elif computer == 1 and player == 3:
    print("Computer chose ROCK! You chose SCISSORS! You lose!")
elif computer == 2 and player == 1:
    print("Computer chose PAPER! You chose ROCK! You lose!")
elif computer == 2 and player == 3:
    print("Computer chose PAPER! You chose SCISSORS! You win!")
elif computer == 3 and player == 1:
    print("Computer chose SCISSORS! You chose ROCK! You win!")
elif computer == 3 and player == 2:
    print("Computer chose SCISSORS! You chose PAPER! You lose!")
elif computer == 1 and player == 1:
    print("Computer chose ROCK! You chose ROCK! You tied!")
elif computer == 2 and player == 2:
    print("Computer chose PAPER! You chose PAPER! You tied!")
elif computer == 3 and player == 3:
    print("Computer chose SCISSORS! You chose SCISSORS! You tied!")
else:
    print("Choose an actual number")