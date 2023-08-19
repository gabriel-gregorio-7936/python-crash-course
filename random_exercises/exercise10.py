list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
list3 = []
a = 0

for i in range(0, len(list1)):
    if list1[i] % 2 != 0:
        list3.append(list1[i])

for j in range(0, len(list2)):
    if list2[j] % 2 == 0:
        list3.append(list2[j])

print(f"result list: {list3}")
