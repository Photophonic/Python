import FreeSimpleGUI as sg
import functions

sg.theme("Black")

feet_label = sg.Text("Enter feet: ")
input_feet = sg.Input(tooltip="Enter Feet", key="input_feet")

inches_label = sg.Text("Enter inches: ")
input_inches = sg.Input(tooltip="Enter Inches", key="input_inches")

convert_button = sg.Button("Convert")
convert_message = sg.Text(key="convert_message")

exit_button = sg.Button("Exit")

layout = [
    [feet_label, input_feet],
    [inches_label, input_inches],
    [convert_button, exit_button, convert_message],
]


window = sg.Window("Converter", layout=layout, font=("Helvetica", 16))


while True:

    event, values = window.read()
    print("test", event)

    match event:
        case "Convert":
            try:
                print(event)
                print(values)

                feet = float(values["input_feet"])
                inches = float(values["input_inches"])

                meters = functions.convert(feet, inches)

                window["convert_message"].update(value=f"{meters} m")
            except ValueError:
                sg.popup("Please provide values to convert.", font=("Helvetica", 20))

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break
# close the application when we close the window
window.close()
