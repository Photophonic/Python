# grid = []

# for y in range(6):
#     innerList = []
#     for x in range(9):
#         innerList.append(x)
#     grid.append(innerList)

# print(*grid, sep="\n")

# actual answer to rotate the image 90 right
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# outer loop
for i in range(6):
    # inner loop
    for a in range(9):

        # determin if iteration is less than range
        if a < 8:
            # get the row (a) and current position (i)
            print(grid[a][i], end="")
            # grabs first item of each row, then second....
            # use of end="" print on the same line
        else:
            # get the element from the list
            # but do not print on the same line
            print(grid[a][i])


#

grid = []

for y in range(9):
    innerList = []
    for x in range(6):
        innerList.append(x)
    grid.append(innerList)


print(*grid, sep="\n")

# outer loop
for i in range(6):
    # inner loop
    for a in range(9):

        # determin if iteration is less than range
        if a < 8:

            # get the row (a) and current position (i)
            print(grid[a][i], end="")
            # grabs first item of each row, then second....
            # use of end="" print on the same line
        else:
            # get the element from the list
            # but do not print on the same line
            print(grid[a][i])
