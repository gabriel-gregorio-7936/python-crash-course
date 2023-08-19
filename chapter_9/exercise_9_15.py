from random import shuffle

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']
list_2 = list[:]
my_ticket = [2, 6, 'a', 8, 'd']
winning_ticket = []

shuffle(list_2)
number = 0
count = 0

print(len(list_2))

while my_ticket:
    for n in range(0, 5):
        choice = list_2.pop()
        winning_ticket.append(choice)
    
    count = count + 1
    
    list_2 = []
    list_2 = list[:]

    for i in my_ticket:
        if i in winning_ticket:
            number = number + 1
            
            if number == 5:
                print(f"My ticket is {my_ticket}")
                print(f"The winnig ticket is {winning_ticket}")
                print(count)
                break
        
    number = 0

