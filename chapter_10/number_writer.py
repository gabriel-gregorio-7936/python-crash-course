from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

path = Path('C:/Users/makvi/3D Objects/python_work/chapter_10/numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)