#Exercise 10.5
from pathlib import Path

names = []
name = ""
string = ""
path = Path('C:/Users/makvi/3D Objects/python_work/chapter_10/guest_book.txt')

while path:
    name = input("Please, write your name: ")

    if name != 'q':    
        names.append(name.title())
    elif name == 'q':
        break

for person in names:
    string = string + person + "\n"

path.write_text(string)