given_list = [10, 20, 33, 46, 55]

print("Given list is:", given_list)
print("Divisible by 5")

for i in range(0,len(given_list)):
    f = given_list[i]
    if f % 5 == 0:
        print(given_list[i])