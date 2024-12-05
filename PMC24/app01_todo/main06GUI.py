# import after running pip install FreeSimpleGUI from terminal
import FreeSimpleGUI as sg
import functions

# create a series of new elements for the GUI
label = sg.Text("Enter a To-Do")
# key sets the ID for the input box and is how it is referenced
input_box = sg.Input(tooltip="Enter a To-Do", key="todo")
add_button = sg.Button("Add")

# create a window instance,
# items in layout need to be in brackets. Each pair is a row
window = sg.Window(
    "My To Do App", layout=[[label], [input_box, add_button]], font=("Helvetica", 20)
)

while True:
    # display the list of objects from the window
    # store the event and then the key/value dict in variables
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            # print(values)
            # add the value from key todo
            new_todo = values["todo"] + "\n"
            todos.append(new_todo.title())
            # update parameter to pass in the list. Path is defaulted
            functions.write_todos(todos)
        # use the built in code to get close event and break loop
        case sg.WIN_CLOSED:
            break

# close the application when we close the window
window.close()
