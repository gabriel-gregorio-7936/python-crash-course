from random import shuffle

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']
list_2 = list[:]
my_ticket = []

shuffle(list_2)

for n in range(0, 5):
    print(list_2.pop())