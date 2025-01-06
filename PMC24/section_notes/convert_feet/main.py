import FreeSimpleGUI as sg
import functions


feet_label = sg.Text("Enter feet: ")
input_feet = sg.Input(tooltip="Enter Feet", key="input_feet")

inches_label = sg.Text("Enter inches: ")
input_inches = sg.Input(tooltip="Enter Inches", key="input_inches")

convert_button = sg.Button("Convert")
convert_message = sg.Text(key="convert_message")

layout = [
    [feet_label, input_feet],
    [inches_label, input_inches],
    [convert_button, convert_message],
]


window = sg.Window("Converter", layout=layout, font=("Helvetica", 16))


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        # exit loop and close app
        break

    print(event)
    print(values)

    feet = float(values["input_feet"])
    inches = float(values["input_inches"])

    meters = functions.convert(feet, inches)

    window["convert_message"].update(value=f"{meters} m")

# close the application when we close the window
window.close()
