number = int(input("Enter your number here: "))
string = str(number)

print(f"Original number {number}")

if len(string) % 2 == 0:
    print("No. Given number is not palindrome number")
else:
    if string[0] == string[len(string) - 1]:
        print("Yes. Given number is palindrome number")
    else:
        print("HO. Given number is not palindrome number")