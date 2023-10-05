from pathlib import Path

import json
# define path to file
path = Path('Python/ch10/numbers.json')
# create variable and read the contents of the file
contents = path.read_text()
# this takes the JSON format file and conteverts it
# to a python object
numbers = json.loads(contents)
# view the output of the numbers variable
print(numbers)
