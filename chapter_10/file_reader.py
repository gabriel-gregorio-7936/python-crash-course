from pathlib import Path

path = Path('C:/Users/makvi/3D Objects/python_work/chapter_10/pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print(line)