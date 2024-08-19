print("Imported my_module.py")

test = "Test String"


def find_index(to_search, target):
    """Find the index of a value in a sequence"""
    for index, value in enumerate(to_search):
        print(index, value)
        if value == target:
            print("Match found")
            return index

    print("no match found")
    return -1
