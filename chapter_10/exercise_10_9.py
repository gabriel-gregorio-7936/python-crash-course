#Exercise 10.9
from pathlib import Path

path1 = Path('C:/Users/makvi/3D Objects/python_work/chapter_10/cats.txt')
path2 = Path('C:/Users/makvi/3D Objects/python_work/chapter_10/dogs.txt')

try:
    contents1 = path1.read_text()
    contents2 = path2.read_text()
except FileNotFoundError:
    pass
else:
    print(contents1)
    print(contents2)