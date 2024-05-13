import sys, random
from enum import Enum

# define global variable (will be removed later)
# game_count = 0

def rps():
    # create variables for the parent function
    game_count = 0
    player_wins = 0
    python_wins = 0

    # create closure function 
    def play_rps():
        # access the variables in the parent function
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            # use caps for constants
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        # press control + z to wrap the line (MAC)
        # cast input to an int so comparison will work as intended
        player_choice = input("\nEnter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")
        
        if player_choice not in  ["1","2","3"]:
            print("You must enter 1, 2, or 3.")
            # call itself to restart the game
            return play_rps()
        
        player = int(player_choice)

        # randomly choose an item from this list
        comp_choice = random.choice("123")
        computer = int(comp_choice)

        # option Z on MAC to wrap
        # print("You chose " + player_choice + ".")
        print(f"\nYou chose {str(RPS(player)).replace('RPS.', '').title()} .")
        # print("Computer chose " + comp_choice + ".")
        print(f"Computer chose {str(RPS(computer)).replace('RPS.', '').title()}.")

        # define local function and pass in input values
        def decide_winner(player, computer): 
            # because this is a nested function, they need to be passed down one more level 

            nonlocal player_wins
            nonlocal python_wins
            # return results based on the in values
            # 1 - rock, 2 - paper, 3 - scissors
            if player == 1 and computer == 3:
                player_wins += 1
                return("You win!")
            elif player == 2 and computer == 1:
                player_wins += 1
                return("You win!!")
            elif player == 3 and computer == 2:
                player_wins += 1
                return("You win!!!")
            elif player == computer:
                return("Tie???")
            else:
                python_wins += 1
                return("Computer wins boooo")

        # create variable to house the resultes from function
        game_result = decide_winner(player, computer)

        print(game_result)

        # update the global game count variable
        nonlocal game_count
        game_count += 1
        
        # remember to convert int to str()
        # this will allow to track how many games are played
        print(f"\nGame count: {game_count}")
        print(f"\nPlayer wints: {player_wins}")
        print(f"\nComputer wints: {python_wins}")

        # ask to play again
        print("\nPlay again? ")   

        # evaluate if input is y or q. Loop if not
        while True:
            playagain = input("\nY for yes or \nQ for quit\n")
            # is input y or q???
            if playagain.lower() not in ["y", "q"]:
                # start the loop over if not
                continue
            else:
                # exit the loop
                break
        # if the input is y then restart the game by calling itself
        if playagain.lower()== 'y':
            return play_rps()
        else:
            # if q then exit the game with sys.exit()
            print(f"Thanks for playing, you played {str(game_count)} games of RPS")
            sys.exit("Game over")
    
    # Return the play_rps function to the parent function rps
    return play_rps
# start the game
# play_rps()
rps()

# create the variable to hold the function
play = rps()

# play the game
play()