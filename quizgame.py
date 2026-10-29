answer = input("Do you want to play?(yes/no) ")
if answer.lower() != "yes":
    quit()
print("Okey lets play!")
score = 0

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does RAM stands for? ")
if answer.lower() == "random acess memory":
    print("correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does ROM stands for? ")
if answer.lower() == "read only memory":
    print("correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does PSU stands for? ")
if answer.lower() == "power supply unit":
    print("correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does KDF stands for? ")
if answer.lower() == "kenya defence forces":
    print("correct")
    score += 1
else:
    print("Incorrect")


percent = ((score * 100 )/ 5)
print(f"You score {score}" )
print(f"Your percentage score is {percent}%")
