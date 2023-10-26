# defining the function
import random


def hello():
    # issue commands in the function
    print('Hi')
    print('Hello')
    print('Word')


# call the function with ()
# each call will execute the code contained within
hello()
hello()
hello()

# passing arguments into a function
# define a function, add arguments


def hello_there(name):
    # argument is passed into the contained code
    print(f'Hi there {name}')


# call the function and provide an in argument
hello_there('Steve')
# displays Hi there Steve
hello_there('Bob Dole')


# Return statements in a function
def get_answer(anserNumber):
    if anserNumber == 1:
        return "It's certain!"
    elif anserNumber == 2:
        return "Sure, it's pretty good"
    elif anserNumber == 3:
        return "It could happen"
    elif anserNumber == 4:
        return "I mean, I guess???"
    elif anserNumber == 5:
        return "meeeeeeh"
    elif anserNumber == 6:
        return "Don't bother"
    else:
        return "Go do something else."


# get a random number in a range with randint
r = random.randint(1, 9)
# create variable that calls the function
# uses the random int as the in argument
fortune = get_answer(r)
# print out the returned value
print(r, fortune)


# none value = NULL
spam = print('Hello')
# print function returns None behind the scenes
print(None == spam)

# you can add keyword functions to print
# use of sep=", " will place a comma between the items
print('cat', 'dog', 'bird', 'mouse', sep=", ")

# global variables can be modified from within a function
# use global statement to define


def spam():
    # this will update the variable at the global level
    global eggs
    eggs = 'spam'


eggs = 'global'
spam()
# will print spam, not 'global'
print(eggs)


def spam():
    # this will update the variable at the global level
    global eggs
    eggs = 'spam'  # global


def bacon():
    eggs = 'bacon'  # local
    print(eggs)


def ham():
    print(eggs)  # this is global


print('******')
eggs = 42
spam()
bacon()
ham()
print(eggs)


# exception handling in python
def spam(divideByZero):
    # use try/except for error checking
    # similar to EXCEPTION in PL/
    try:
        return 42/divideByZero
    except:
        return ("Zero Divide")


print(spam(3))
print(spam(10))
# will error since 0 divide. Need to catch this
print(spam(0))
print(spam(42))

# can also set the exception in the execution


def spam(zeroDivide):
    return 42/zeroDivide


try:
    print(spam(41))
    print(spam(0))
    print(spam(3))
except:
    print('Zero divide nice try.')


indent = 6
print('!!' * indent, end='')
print('******')
