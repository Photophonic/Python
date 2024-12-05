# Import GUI
import FreeSimpleGUI as sg

# create a zip file
import shutil

# create a series of new elements for the GUI
label1 = sg.Text("Select files to zip")
input_box1 = sg.Input(tooltip="File location")
# allows selection of multiple files in a location
add_button1 = sg.FilesBrowse("Choose")


label2 = sg.Text("Select file destination ")
input_box2 = sg.Input(tooltip="File location")
# use to select the folder location
add_button2 = sg.FolderBrowse("Choose")


# create button to zip files
zip_button = sg.Button("Zip Files")

# create a window instance,
# items in layout need to be in brackets. Each pair is a row
window = sg.Window(
    "File Zip",
    layout=[
        [label1, input_box1, add_button1],
        [label2, input_box2, add_button2],
        [zip_button],
    ],
)
# display the list of objects from the window
window.read()
# close the application when we close the window
window.close()


# provide name of path & file name, type, location
shutil.make_archive("section_notes/myfiles/output", "zip", "section_notes/myfiles")
