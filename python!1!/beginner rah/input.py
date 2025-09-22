# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

name = input("What is your name? ")
age = input("How old are you? ")

age = int(age)


print(f"Hello, {name}")
print(f"You are {age}")
print(f"HAPPY BIRTHDAY!")
age = age + 1
print(f"You are now {age}")