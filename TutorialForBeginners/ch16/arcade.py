import sys
# import the main modules from the two games
from rps import rps
from guess_num import guess_number

# define main function for choice program
def play_game(name="PlayerOne"):
    # create variable to set state of game
    welcome_back = False

    # create loop to prompt for a game selection
    while True:
        if welcome_back == True:
            print(f"\nWelcome back to the arcade {name}!")

        # get player input
        playerchoice = input("\nPlease choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n\nOr press \"x\" to exit the arcade\n\n ")

        # validate response is valid
        if playerchoice not in ["1","2","x"]:
            print(f"{name}, please enter 1, 2, or x.")
            # call itself to restart the game
            return play_game(name)
        
        # set game state to True after initial selection
        welcome_back = True

        if playerchoice == "1":
            # create a variable to contain rps module and name
            rock_paper_scissor = rps(name)
            # call the RPS game
            rock_paper_scissor()
        elif playerchoice == "2":
            guess_my_number = guess_number(name)
            guess_my_number()
        else:
            print("\nSee you next time!")
            # exit game
            sys.exit(f"Bye {name}")

# to accomodate CLI input, import argparse to simplify setup
if __name__ == "__main__":
    import argparse

    # create a variable to hold the arguments. This is all boilerplate code
    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        '-n', '--name', metavar='name',
        required=True, help='The name of the person playing the game.'
    )

    # parse arguments
    args = parser.parse_args()

    print(f"\n{args.name}, welcome to the arcade!")
    # use the parsed data
    arcade = play_game(args.name)
    
 