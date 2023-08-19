numbers_x = [75, 65, 35, 75, 30]

print(f"Given list: {numbers_x}")

def list(numbers_x):
    if numbers_x[0] == numbers_x[len(numbers_x) - 1]:
        print("Result is True")
    else:
        print("Result is False")

list(numbers_x)