print('How many cats I own')
numCats = input()

try:
    if int(numCats) >= 4:
        print ('That\'s a lot of cats')
    elif int(numCats) < 0:
        print('nice try')
    else:
        print('That is not that many cats.')
except ValueError:
    print('please enter a number')
