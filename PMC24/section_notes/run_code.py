import webbrowser

# replace the spaces to + for the search
user_term = input("Enter a search term: ").replace(" ", "+")
# pass search string into search
webbrowser.open(f"https://bing.com?q={user_term}")
