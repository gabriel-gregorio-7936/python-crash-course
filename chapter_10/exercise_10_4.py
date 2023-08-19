#Exercise 10.4
from pathlib import Path

name = input('Write your name please: ')
name = name.title()

path = Path('C:/Users/makvi/3D Objects/python_work/chapter_10/guest.txt')
path.write_text(name)