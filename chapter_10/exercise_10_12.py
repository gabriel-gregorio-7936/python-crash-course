#Exercise 10.12
from pathlib import Path
import json

path = Path('C:/Users/makvi/3D Objects/python_work/chapter_10/favorite_number.json')
if path.exists():
    contents = path.read_text()
    favorite_number = json.loads(contents)
    print(f"I know your favorite number! It is {favorite_number}")
else:
    favorite_number = input("What's your favorite number? ")
    favorite_number = int(favorite_number)
    contents = json.dumps(favorite_number)
    path.write_text(contents)