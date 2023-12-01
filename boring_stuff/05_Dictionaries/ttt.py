# create dictionary consisting of the 9 grid slots
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'med-L': ' ', 'med-M': ' ', 'med-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' ',
            }

# create function with input value "board"
# this will print out the grid and the dictionary values
# matching the key "top-L" or "med-M" ect...


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['med-L'] + '|' + board['med-M'] + '|' + board['med-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


# define variable of first player 'X'
turn = 'X'

# loop 9 times, total number of grid spots.
# does not take into account if someone wins or already marked
for i in range(9):
    # print the existing board based on values in theBoard dict.
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')

    # prompt for a location
    move = input()
    # update the value in the K/V pair to X or O based in input
    theBoard[move] = turn

    # check who's turn it is and update to the other.
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

# print out the final board
printBoard(theBoard)
