def get_feet_inches(feet_inches):
    imperial = feet_inches.split(" ")

    # assign each list position to a variable
    feet = float(imperial[0])
    inches = float(imperial[1])

    return (feet, inches)


def convert(feet, inches):

    meters = feet * 0.3048 + inches * 0.0254

    return meters


feet_inches = input("Enter the feet and incehs: ")

feet, inches = get_feet_inches(feet_inches)

meters = convert(feet, inches)

print(f"{meters} meters")

if meters < 1.0:
    print("too short")
else:
    print("have fun")
