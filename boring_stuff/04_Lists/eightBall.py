# magic eight ball
import random

message = [
    'Certainly',
    'Sure',
    'There is a chance',
    'Do not hold your breath',
    'Unlikely',
    'Fat chance'
]

# use a randome int at the lenght of the list to derive a message
# -1 is used since the list is 0 based
print(message[random.randint(0, len(message)-1)])

# view all messages
for i in message:
    print(i)
