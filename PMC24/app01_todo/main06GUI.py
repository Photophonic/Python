# import after running pip install FreeSimpleGUI from terminal
import FreeSimpleGUI as sg
import functions

# create a series of new elements for the GUI
label = sg.Text("Enter a To-Do")
# key sets the ID for the input box and is how it is referenced
# do_not_clear=False, will clear the input field after button action
input_box = sg.Input(tooltip="Enter a To-Do", key="todo_input")
add_button = sg.Button("Add")

# display a list of to-dos from the file. Enable True/False events. Define the size of the box.
list_box = sg.Listbox(
    values=functions.get_todos(), key="todos_list", enable_events=True, size=[45, 10]
)
edit_button = sg.Button("Edit")

complete_button = sg.Button("Complete")

# create a window instance,
# items in layout need to be in brackets. Each pair is a row
window = sg.Window(
    "My To Do App",
    layout=[
        [label],
        [input_box, add_button],
        [list_box, edit_button],
        [complete_button],
    ],
    font=("Helvetica", 20),
)

while True:
    # display the list of objects from the window
    # store the event and then the key/value dict in variables
    event, values = window.read()
    print("1", event)
    print("2", values)
    print("3", values["todos_list"])
    match event:
        case "Add":
            todos = functions.get_todos()
            # add the value from key todo
            new_todo = values["todo_input"] + "\n"
            todos.append(new_todo.title())
            # update parameter to pass in the list. Path is defaulted
            functions.write_todos(todos)
            # refresh the list with added value
            window["todos_list"].update(values=todos)

        case "Edit":
            # point to the value to edit, using [0] will get only the string value
            todo_to_edit = values["todos_list"][0]
            print(todo_to_edit)
            # grab the new value from the top entry field
            new_todo = values["todo_input"]
            print(new_todo)

            # get current to_do list
            todos = functions.get_todos()
            # get selected item's index
            todo_index = todos.index(todo_to_edit)
            # update with new value
            todos[todo_index] = new_todo
            # write to the list
            functions.write_todos(todos)
            # call update method on window. Use "todos" key for list_box, update it with the todos
            window["todos_list"].update(values=todos)
        # when you click on an item in the list get the value
        case "todos_list":
            # select the input box and update with the value from the lists window.
            window["todo_input"].update(value=values["todos_list"][0])

        case "Complete":
            print("Test")

        # use the built in code to get close event and break loop
        case sg.WIN_CLOSED:
            break

# close the application when we close the window
window.close()
