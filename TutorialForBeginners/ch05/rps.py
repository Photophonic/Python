import sys, random
from enum import Enum


# create a class for enum
class RPS(Enum):
    # use caps for constants
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# ways to use RPS class we made for Enum
# print(RPS(2)) #Paper
# print(RPS.ROCK) #Rock
# print(RPS['ROCK']) #Rock
# print(RPS.ROCK.value) #1
# sys.exit()


print("")
# press control + z to wrap the line (MAC)
# cast input to an int so comparison will work as intended
player_choice = input("Enter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

player = int(player_choice)

if player < 1 or player > 3:
    # to display a message and exit the program...
    sys.exit("You must enter 1, 2, or 3. ")

# randomly choose an item from this list
comp_choice = random.choice("123")
computer = int(comp_choice)

print("")
# print("You chose " + player_choice + ".")
print("You chose " + str(RPS(player)).replace('RPS.', '').title() + ".")
# print("Computer chose " + comp_choice + ".")
print("Computer chose " + str(RPS(computer)).replace('RPS.', '').title() + ".")
print("")

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
