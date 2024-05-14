def hello(name, lang):
    greetings = {
        'English':"Hello",
        'Spanish':"Hola",
        'German':"Hallo",
    }
    # call the msg function then pass in arguments to select proper greeting from the dictionary then the name
    msg = (f"{greetings[lang]} {name}")
    print(msg)

if __name__ == "__main__":
    # Parser for command-line options
    import argparse

    # define a parse
    parser = argparse.ArgumentParser(
        description="Provides a personal greeting."
    )

    parser.add_argument(
        # provide flags for CLI items
        # read docs for better understanding 
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to greet"
    )

    # parser version accepting lang argument
    parser.add_argument(
        "-l", "--lang", metavar="language",
        required=True, choices=["English","Spanish","German"],
        help = "Language of the greeting"
    )

    # call the method on the parser object
    args = parser.parse_args()

    # call the lang version of the funcion and hello function
    hello(args.name,args.lang)

    # to run this from CLI, type python3 cli.py -n "NAME"