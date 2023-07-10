#import the random function
import random

print('Hello, what is your name?')

#store input as a variable
name = input()

print(name + ' I am thinking of a number between 1 and 10...')

#generate the random number with the random.randint(x,y) function
secretNumber = random.randint(1,10)

#use a for loop with a designated range to control the 6 loops
for i in range(1,7):
    print ('take a guess')
    guess = int(input())

    if guess < secretNumber:
        print ('Too low')
    elif guess > secretNumber:
        print('Too high')
    else:
        break #correct guess

if guess == secretNumber:
    print('Good job, you guessed '+ str(secretNumber) + ' in ' + str(i) + ' guesses.')
else:
    print ('Nice try. the number was '+ str(secretNumber))
    



