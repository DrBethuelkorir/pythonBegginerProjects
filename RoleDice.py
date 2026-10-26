import random

x = input("Do you want to play? (Y/N): ").lower()

if x == "y":
    howmanytimes = int(input("How many times do you want to play?: "))

    for i in range(howmanytimes):
        rand1 = random.randint(1, 6)
        rand2 = random.randint(1, 6)
        print(f"Roll {i + 1}: ({rand1}, {rand2})")

    print("Game Over")

elif x == "n":
    print("Thanks for playing")

else:
    print("Invalid choice")