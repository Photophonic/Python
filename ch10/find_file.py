from pathlib import Path

path = Path('Python/ch10/alice.txt')

# This will error because the file does not exist
# contents = path.read_text()


# To error check this.
try:
    contents = path.read_text(encoding='utf-8')
except:
    print(f'File {path} was not found ')
# if found then do the following line splits
else:
    lines = contents.splitlines()
    num_words = len(lines)
    print(f'There are {num_words} words in {path}')
