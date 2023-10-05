from pathlib import Path

import json

# create a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

path = Path('Python/ch10/numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)
