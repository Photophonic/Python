from pathlib import Path
import json

path = Path('Python/ch10/username.json')
contents = path.read_text()
username = json.loads(contents)

print(f'Welcome back {username}')
