# import after running pip install FreeSimpleGUI from terminal
import FreeSimpleGUI as sg
import functions

# create a series of new elements for the GUI
label = sg.Text("Enter a To-Do")
input_box = sg.Input(tooltip="Enter a To-Do")
add_button = sg.Button("Add")

# create a window instance,
# items in layout need to be in brackets. Each pair is a row
window = sg.Window("My To Do App", layout=[[label], [input_box, add_button]])
# display the list of objects from the window
window.read()
# close the application when we close the window
window.close()
