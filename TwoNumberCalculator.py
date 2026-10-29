num1 = float(input("Enter the first number: "))
operator = input("What do you want to do(*, /, +, -): ")
num2 = float(input("Enter the second number: "))


if operator == "*":
    total = num1 * num2
    print(f"The multiplication of {num1} by {num2} is {total}")
elif operator == "/":
    if num2 == 0:
        print("A number canot be divided by zero")
    else:
        total = num1 / num2
        print(f"The division of {num1} by {num2} is {total}")
elif operator == "-":
    total = num1 - num2
    print(f"The subtraction of {num2} from {num1} is {total}")
elif operator == "+":
    total = num1 + num2
    print(f"The addition of {num1} and {num2} is {total}")
else:
    print("invalid oparation") 