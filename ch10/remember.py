# remember user input
from pathlib import Path
import json

username = input('Enter your username: \n')

path = Path('Python/ch10/username.json')
contents = json.dumps(username)
path.write_text(contents)
