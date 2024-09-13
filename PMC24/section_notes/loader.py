# https://docs.python.org/3/library/functions.html#zip
# section_notes\files

contents = ["test data 11", "test data 22", "test data 33"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

# loop over both lists. Zip function Iterate over several iterables in parallel, producing tuples with an item from each one.
for content, filename in zip(contents, filenames):
    # open the file based on the filename and path, "a" = append will create a new file if not there
    file = open(f"section_notes/files/{filename}", "w")
    # write content
    file.write(content)
    # close the file
    file.write(f"also{content}")
    file.close()
