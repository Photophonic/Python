import streamlit as st
import functions

# create variable to get and hold the list of to-do's
todos = functions.get_todos()

st.title("Todo App")
st.subheader("App to track your todos")
st.write("Help you keep your day in order")

# loop over the todos
for todo in todos:
    # dynamically create a checkbox based on the current iteration of the todos
    st.checkbox(todo)

# text box to receive user input
st.text_input("Enter your todos:",placeholder='Add new todo...')