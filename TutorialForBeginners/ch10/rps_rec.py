import sys, random
from enum import Enum

# create a class for enum
def play_rps():
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
    print("\nYou chose " + str(RPS(player)).replace('RPS.', '').title() + ".")
    # print("Computer chose " + comp_choice + ".")
    print("Computer chose " + str(RPS(computer)).replace('RPS.', '').title() + ".")

    # 1 - rock, 2 - paper, 3 - scissors
    if player == 1 and computer == 3:
        print("You win!")
    elif player == 2 and computer == 1:
        print("You win!!")
    elif player == 3 and computer == 2:
        print("You win!!!")
    elif player == computer:
        print("Tie???")
    else:
        print("Computer wins boooo")

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
        print("Thanks for playing")
        sys.exit("Game over")

# start the game
play_rps()
