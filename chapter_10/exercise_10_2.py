#Exercise 10.2
from pathlib import Path

path = Path('C:/Users/makvi/3D Objects/python_work/chapter_10/learning_python.txt')
contents = path.read_text()

lines = contents.splitlines()
message = contents.replace('Python', 'Rust')

for line in lines:
    print(f"{line}")

print(f"\n{message}")