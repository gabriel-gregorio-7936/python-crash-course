str = input("Type your string: ")

print(f"Orginal String is {str}")
print("Printing only even index chars")
for i in range(0,len(str),2):
    print(str[i])