import sys, random

# create initial function with in parameter for player name
def guess_number(name = 'PlayerOne'):
    game_count = 0
    player_wins = 0

    # start game
    def play_guess_number():
        # gain access to the higher level variables for tracking   
        nonlocal name
        nonlocal player_wins

        # prompt for player input, using name in arg
        player_choice = input(f"\n{name}, guess which number I am thinkig of.... 1, 2, or 3.\n\n")

        # basic validation for input using a list
        if player_choice not in ["1","2","3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            # call itself to restart the game
            return play_guess_number()

        # select a number between 1 and 3 using random.choice.
        computer_choice = random.choice("123")

        # print out the the two values
        print(f"{name}, you chose {player_choice}")
        print(f"I was thinking of {computer_choice}\n")

        # convert both to int to compare and find winner
        player = int(player_choice)
        computer = int(computer_choice)

        # decide the winnder in new function with passed in args
        def decide_winner(player, computer):
            # gain access to name and win count
            nonlocal name
            nonlocal player_wins

            if player == computer:
                # if player guess is the same as comp then they win
                player_wins += 1
                return (f"{name}, you win!")
            else:
                return (f"Sorry {name}, computer wins this round.")
        
        # create a variable to call the function and store the results of the inner returns
        game_result = decide_winner(player, computer)
            
        # print the result stored in game_result 
        print (game_result)

        # update nonlocal var game_count
        nonlocal game_count
        game_count += 1

        # Print current status
        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        # find percentage by dividing wins vs count, use f format to set the result to two decimal and show %
        print(f"\nYour winning percentage: {player_wins/game_count:.2%}")

        # prompt to play again?
        print(f"\nPlay again, {name}?")        

        # use a While loop to keep the game going
        while True:
            playagain = input('\nY for Yes or \nQ to Quit\n')
             # is input y or q???
            if playagain.lower() not in ["y", "q"]:
                # start the loop over if not
                continue
            else:
                # exit the loop
                break

        # if the input is y then restart the game by calling itself
        if playagain.lower()== 'y':
            # call itself to start the game againb
            return play_guess_number()
        else:
            print(f"Thanks for playing {name}\n")
            # if this is the file being run (main), then exit 
            if __name__ == "__main__":
                sys.exit(f"Bye")
            else:   
                # if not, return to the calling process
                return
            
    # to complete the closure, return the game to the calling function 
    return play_guess_number


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

    # use the parsed data
    guess_my_number = guess_number(args.name)
    
    # call the function to start the game
    guess_my_number()