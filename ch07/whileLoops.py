# # input() will capture user input then proceed with the program
# message = input("Tell me something and I'll repeate it: input ")
# print(message)

# name = input("Please enter your name: ")
# print(f"Hi there {name}\n")


# # you can assign a message to a variable an display that in the promt and make it multiline.
# message = ("Tell me something about yourself. ")
# message += ("Like what's your favorite food? ")
# answer = input(message)
# print(f"{answer} is a good answer\n")


# # input() is considered a string, use int() to convert to numbers
# age = input("How old are you? ")
# if (int(age) >= 21):
#     print(f"{age} can got to the beer store!")
# else:
#     print(f"{age} is not quite old enough for the beer store.")


# # modulo, returns the remainder
# number = input("Enter a number and I will tell you if it is even or odd!\n")
# if int(number) % 2 == 0:
#     print(f"{number} is an even number")
# else:
#     print(f"{number} is an odd number")


# # while loops
# current_num = 1
# while current_num <= 5:
#     print(current_num)
#     current_num += 1


# # prompt = "Tell me when to quit the loop with QUIT\n"
# # # make sure to initialize a default value before going into the loop
# # message = ""
# # # condition evaluation
# # while message != "QUIT":
# #     # repeate our prompt above
# #     message = input(prompt)
# #     # and an if to determine if it should print the message or quite
# #     if message != "QUIT":
# #         print(message)


# # Using Flags to control a loop
# prompt = "Tell me when to quit the loop with QUIT\n"

# active = True

# while active:
#     # repeate our prompt above
#     message = input(prompt)
#     # and an if to determine if it should print the message or quite
#     if message == "QUIT":
#         active = False
#     else:
#         print(message)


# Loops and lists, moving items from one list to another with while loop
new_users = ['Bob', 'Jane', 'Steve', 'Sarah']
confirmed_users = []

# verify users unitl list is emptu
while new_users:
    # create holding variable in the loop, user list method .pop() to remove the current user
    current_user = new_users.pop()
    print(f"Verify user: {current_user.title()}.")
    # use append method to add the current user into the new list
    confirmed_users.append(current_user)

# display all confirmed users
print("\nConfirmed users:")
for confirmed_user in confirmed_users:
    print(confirmed_user)


# using .remove() in a loop on a list to remove all instances
pets = ['cat', 'dog', 'cat', 'rabbit', 'cat', 'axxolotl', 'cat', 'hyena']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# making a dictionary from user input in a list
responses = {}
# set flag to active
polling_active = True
while polling_active:
    name = input("Please enter your name?")
    response = input("\nWhat is your hobby?")

    # store the responses with new Key/Value pairs
    responses[name] = response

    # check if the person wants to keep responding
    repeat = input('Would you like someone else to answer?')

    if repeat == 'no':
        polling_active = False

print('Results of the poll:\n')
# must have .items() when acccessing k/v pairs in the dictionary
for name, response in responses.items():
    print(f'{name}: {response}')
