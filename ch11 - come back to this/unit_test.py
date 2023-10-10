from name_function import get_formatted_name

# Create a test case for the name_function


def test_name_function():
    formatted_name = get_formatted_name('bob', 'dole')
    assert formatted_name == 'Bob Dole'
