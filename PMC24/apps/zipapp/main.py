# Import GUI
import FreeSimpleGUI as sg
from create_zip import create_archive


# create a series of new elements for the GUI
label1 = sg.Text("Select files to zip")
input_box1 = sg.Input(tooltip="File location")
# allows selection of multiple files in a location
add_button1 = sg.FilesBrowse("Choose", key="select_btn")


label2 = sg.Text("Select file destination ")
input_box2 = sg.Input(tooltip="File location")
# use to select the folder location
add_button2 = sg.FolderBrowse("Choose", key="destination_btn")


# create button to zip files
zip_button = sg.Button("Zip Files")
# create success message
output_msg = sg.Text(key="output")


# allign using columns
col1 = sg.Column([[label1], [label2]])
col2 = sg.Column([[input_box1], [input_box2]])
col3 = sg.Column([[add_button1], [add_button2]])

# create a window instance,
# items in layout need to be in brackets. Each pair is a row
# window = sg.Window(
#     "File Zip",
#     layout=[
#         [label1, input_box1, add_button1],
#         [label2, input_box2, add_button2],
#         [zip_button, output_msg],
#     ],
# )

# render page with column layout
window = sg.Window(
    "Arcive Extractor", layout=[[col1, col2, col3], [[zip_button, output_msg]]]
)

while True:
    # display the list of objects from the window
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        # exit loop and close app
        break

    print("Event - ", event)
    print("Values - ", values)
    # get the file patch from the K/V pair above. Will need to split the string with split
    filepath = values["select_btn"].split(";")
    # get the folder path from the destination button dest_btn
    folder = values["destination_btn"]
    # pass the file paths into the external function
    create_archive(filepath, folder)
    # update success message
    window["output"].update(value="Zip file completed")

# close the application when we close the window
window.close()
