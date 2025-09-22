card = int(input("Would you like to sign up for a credit card? 1 for yes, 2 for no: "))

if card == 1:
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You are now signed up!")
    elif age <= 0:
        print("Getting that bag in the womb? I think not. GET OUT")
    else:
        print("GET OUT")
else:
    print("GET OUT")

