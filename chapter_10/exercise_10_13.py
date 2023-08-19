from pathlib import Path
import json

def greet_user():
    """Greet the user by name."""
    path = Path('C:/Users/makvi/3D Objects/python_work/chapter_10/username_information.json')
    username_info = {

    }
    
    if path.exists():
        contents = path.read_text()
        contents = {contents}
        username = json.loads(contents['name'])
        favorite_place = json.loads(contents['place'])
        favorite_colour = json.loads(contents['colour'])
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        favorite_place = input("What is your favorite place? ")
        favorite_colour = input("What is your favorite colour? ")
        username_info['name'] = username
        username_info['place'] = favorite_place
        username_info['colour'] = favorite_colour
        contents = json.dumps(username_info)

        path.write_text(contents)

        print(f"We'll remember you when you come back, {username} and your preferences!")

greet_user()