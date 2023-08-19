#Exercise 10.11 part 1
from pathlib import Path
import json

favorite_number = input("What's your favorite number? ")
favorite_number = int(favorite_number)

path = Path('C:/Users/makvi/3D Objects/python_work/chapter_10/favorite_number.json')
contents = json.dumps(favorite_number)
path.write_text(contents)