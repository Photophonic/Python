import FreeSimpleGUI as sg
import functions
import time
import os

# if file does not exist, create it
if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        # don't write anything to the file
        pass

sg.theme("Black")

label = sg.Text("Enter a To-Do")
clock_label = sg.Text("", key="clock")

input_box = sg.Input(tooltip="Enter a To-Do", key="todo_input")
add_button = sg.Button("Add")


list_box = sg.Listbox(
    values=functions.get_todos(), key="todos_list", enable_events=True, size=[45, 10]
)

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
message = sg.Text(key="message")

layout = [
    [label, clock_label],
    [input_box, add_button],
    [list_box, edit_button, complete_button],
    [exit_button, message],
]

window = sg.Window(
    "My To Do App",
    layout=layout,
    font=("Helvetica", 20),
)


while True:
    event, values = window.read(timeout=999)

    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo_input"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos_list"].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values["todos_list"][0]
                new_todo = values["todo_input"]
                todos = functions.get_todos()
                todo_index = todos.index(todo_to_edit)
                todos[todo_index] = new_todo
                functions.write_todos(todos)
                window["todos_list"].update(values=todos)
            except IndexError:
                sg.popup("Please select an item to edit.", font=("Helvetica", 20))

        case "Complete":
            try:
                todo_to_complete = values["todos_list"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos_list"].update(values=todos)
                window["todo_input"].update(value="")
            except IndexError:
                sg.popup("Please select an item to complete.", font=("Helvetica", 20))

        case "Exit":
            break

        case "todos_list":
            window["todo_input"].update(value=values["todos_list"][0])

        case sg.WIN_CLOSED:
            break


window.close()
