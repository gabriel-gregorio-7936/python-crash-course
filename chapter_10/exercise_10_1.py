#Exercise 10.1
from pathlib import Path

path = Path('C:/Users/makvi/3D Objects/python_work/chapter_10/learning_python.txt')
contents = path.read_text()

lines = contents.splitlines()

for line in lines:
    print(f"{line}")

print(f"\n{contents}")