# nested function will have access to the parent function

# can set the in value for the parent function's starting value
def parent_function(person, coin):
    coins = coin 

    def play_game():
        # nonlocal will all this nested function access to update coins in the parent function 
        nonlocal coins
        coins -= 1 

        if coins > 1:
            print("\n" + person + " has "+ str(coins) + " coins left. ")
        elif coins == 1:
            print("\n" + person + " has "+ str(coins) + " coin left. ")            
        else:
            print("\n" + person + " has no coins left. ")
    
    # return the nested function when the parent function is called. Note, it should just be the name, don't call the function, e.g. return play_game()
    return play_game


# Variable bob and sam will become a stored function
# by setting an in, this can allow the same function to operate with different number of internal values
bob = parent_function("Bob", 10)
sam = parent_function("Sam",3)

# call bob 3 times, will decrease the value of coins in the bob function's parent scope
for _ in range(3):
    bob()

# will decrease the sam function coin value by only 1
sam()