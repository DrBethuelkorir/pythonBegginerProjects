import random

guess = random.randint(1, 100)
while True:
    try:
        userChoice = int(input("Enter number between 1 to 100: "))
        if userChoice < 1 or userChoice > 100:
                print("invalid choice")
        elif userChoice > guess:
                print("Your number higher")
        elif userChoice < guess:
                print("Your number Lower")
        elif userChoice == guess:
                print("Congratulation, You guessed the number")
                break
    except ValueError:
        print("Use a valid number")
    
    