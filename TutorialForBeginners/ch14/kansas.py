from random import choice

capital = "Topeka"

bird = "Western Meadowlark"

flower = "Sunflower"

song = "Home on the Range"


def randomfunfact():
    funfacts = [
        "Kansas is considered flat, but it does have a mountain.",
        "Wichita is the largest city in the state, but many would guess that it is Kansas City.",
        "A considerable portion of Kansas City is actually in Missouri.",
        "Most Kansans are annoyed by Wizard of Oz references from people outside of Kansas."
    ]

    # create the index using choice.
    index = choice("0123")
    # then convert to a string
    print(funfacts[int(index)])

# this is a special value contained in modules
if __name__ == "__main__":
    # if THIS is the running file, then it will run the function
    randomfunfact()