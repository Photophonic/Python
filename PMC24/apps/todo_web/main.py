import streamlit as st
import functions

# create variable to get and hold the list of to-do's
todos = functions.get_todos()

# create callback function for input
def add_todo():
    # variable to hold value entered into the text_input using key "new_todo" along with new line.
    todo = st.session_state["new_todo"]+ "\n"
    # apend the todo value to the todos list variable
    todos.append(todo)
    # call our functions package to write to the file
    functions.write_todos(todos)

st.title("Todo App")
st.subheader("App to track your todos")
st.write("Help you keep your day in order")

# loop over the todos. Use enumerate to get index from list and the value
for index, todo in enumerate(todos):
    # dynamically create a checkbox based on the current iteration of the todos, key must be a unique value, so using todo as key will address this.
    checkbox = st.checkbox(todo, key=todo)
    # check if checked = true
    if checkbox:
        # print(index,todo)
        todos.pop(index)
        functions.write_todos(todos)
        # delete the existing k/v pair from session state
        del st.session_state[todo]
        # regen the checklist
        st.rerun()

# text box to receive user input
st.text_input("Enter your todos:",placeholder='Add new todo...', on_change=add_todo, key="new_todo")

# view the key/value items for the dictionary
# st.session_state
