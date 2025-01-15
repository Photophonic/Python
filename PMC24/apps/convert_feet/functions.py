def get_feet_inches(feet_inches):
    # split the string on the space and create a list
    imperial = feet_inches.split(" ")

    # assign each list position to a variable
    feet = float(imperial[0])
    inches = float(imperial[1])

    return (feet, inches)


def convert(feet, inches):

    meters = feet * 0.3048 + inches * 0.0254

    return meters
