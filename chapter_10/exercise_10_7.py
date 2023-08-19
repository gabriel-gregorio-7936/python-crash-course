print("Enter two numbers and I will add them.")

while True:
    num1 = input("Enter the first number: ")
    if num1 == 'q':
        break

    num2 = input("Enter the second number: ")
    if num2 == 'q':
        break
    
    try:
        num1 = int(num1)
        num2 = int(num2)    
    except ValueError:
        print("You need to enter a number!")
    else:
        num = num1 + num2
        print(f"The result is {num}")