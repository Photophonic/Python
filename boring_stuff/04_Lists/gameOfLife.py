import random
import time
import copy

WIDTH = 20
HEIGHT = 10

# create a list of values for the cells
nextCells = []

for x in range(WIDTH):
    # create a new column
    column = []
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            # add a living cell
            column.append('#')
        else:
            # add a dead cell
            column.append(' ')
    # nextCells is a list of colun lists
    nextCells.append(column)

# main program loop
while True:
    #  modified to better see the steps
    # separate each step with new lines
    print('start')
    # deep copy will copy lists contained instide of lists
    currentCells = copy.deepcopy(nextCells)

    # print currentCells onto the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            # print the # or ' '
            print(currentCells[x][y], end='')
        # Print a new line at the end of the row
        print()

    # Calculate the next step's cell based on current step
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # get neighbor coordinates
            # % WIDTH ensures leftCoord is always between 0 and WIDTH -1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCOORD = (y + 1) % HEIGHT

            # Count living neighbors
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                # Top cell is alive
                numNeighbors += 1
            if currentCells[x][aboveCoord] == '#':
                # Top cell is alive
                numNeighbors += 1
            if currentCells[rightCoord][aboveCoord] == '#':
                # Top cell is alive
                numNeighbors += 1
            if currentCells[leftCoord][y] == '#':
                # Top cell is alive
                numNeighbors += 1
            if currentCells[rightCoord][y] == '#':
                # Top cell is alive
                numNeighbors += 1
            if currentCells[leftCoord][belowCOORD] == '#':
                # Top cell is alive
                numNeighbors += 1
            if currentCells[x][belowCOORD] == '#':
                # Top cell is alive
                numNeighbors += 1
            if currentCells[rightCoord][belowCOORD] == '#':
                # Top cell is alive
                numNeighbors += 1

            # set cells based on rules
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                nextCells[x][y] = '#'
            else:
                nextCells[x][y] = ' '

    time.sleep(1)

    print('end')
    print('\n')
