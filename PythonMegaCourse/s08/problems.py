# create a program with all of the core pieces of python


def make_sentence(phrase):
    question = ("how", "what", "where", "when", "why")
    capitalized = phrase.capitalize()

    if phrase.startswith(question):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)


# print(make_sentence("how are you"))
# print(make_sentence("I had waffles"))

phrases = []

while True:
    user_input = input("Say something: ")

    if user_input == "\\end":
        break
    else:
        phrases.append(make_sentence(user_input))


response = ", ".join(phrases)

print(response)
