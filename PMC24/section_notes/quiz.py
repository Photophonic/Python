import json

with open("section_notes/myfiles/questions.json", "r") as file:
    # load the json file int a variable with .read() as a str
    content = file.read()

# create a list variable using json.loads() with the read data
data = json.loads(content)
# print(type(content))
# print(type(data))

for question in data:
    print(question["question"])
    # loop through each item in the second item in the dictionary
    # use index and enumerate to create an index value for the output

    for index, choice in enumerate(question["choice"]):
        # create a +1 to the index for visual output
        print(index + 1, "-", choice)

    # gether user answer and convert to int
    user_choice = int(input("Enter your answer: \n"))
    # append a new key to the current dictionary in the loop
    # add the user's input as the new value to the K/V pair
    question["user_choice"] = user_choice

# initialize score value
score = 0

# loop over the dictionaries again
for index, question in enumerate(data):

    if user_choice == question["answer"]:
        score += 1
        result = "Correct Answer"
    else:
        result = "Incorrect Answer"

    message = f'Question {index+1}, your answer is {question["user_choice"]}, correct answer is {question["answer"]}. {result}'

    print(message)


print(f"\n{score} out of {len(data)} correct")
