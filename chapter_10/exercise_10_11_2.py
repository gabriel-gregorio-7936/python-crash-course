from pathlib import Path
import json

path = Path('C:/Users/makvi/3D Objects/python_work/chapter_10/favorite_number.json')
contents = path.read_text()

favorite_number = json.loads(contents)

print(f"I know your favorite number! It is {favorite_number}")