def get_averages():
    with open("section_notes/myfiles/file.txt", "r") as file:
        # readlines to get items as a list of strings
        data = file.readlines()
        # us [:] to slice and skip first line
        values = data[1:]
        # use list comp to get the float of each value
        values = [float(i) for i in values]
        # sum() is built in function
        averages = sum(values) / len(values)
    return averages


average = get_averages()
print(average)
