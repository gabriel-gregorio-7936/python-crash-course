print("Enter two numbers and I will add them.")

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
except ValueError:
    print("You need to enter a number!")
else:
    num = num1 + num2
    print(f"The result is {num}")