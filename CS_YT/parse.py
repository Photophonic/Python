# using csv module makes reading csv's very easy
import csv

with open("names.csv", "r") as csv_file:
    # create a variable to hold the read csv file
    csv_reader = csv.reader(csv_file)

    # this will skip over the first line of the file
    # next(csv_reader)

    # open a new file for writing
    with open("new_names.csv", "w") as new_file:
        # pass in the file name alias to the writer method
        # second parameter changes the delimiter \t = tab
        csv_writer = csv.writer(new_file, delimiter="\t")

        # iterate over the opened file
        for line in csv_reader:
            # write current of line to the file
            csv_writer.writerow(line)


with open("names.csv", "r") as csv_file:
    # create a variable to hold the read csv file
    csv_reader = csv.reader(csv_file)

    # this will produce a list of each value
    for line in csv_reader:
        print(line)
    #  to print just the emails
    # print(line[2])


with open("names.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # this will print out an ordered dictionary
    # the field names are now the keys to the value pairs
    # easier to ready what the data represensts vs. index
    for line in csv_reader:
        # print(line)
        print(line["email"])
