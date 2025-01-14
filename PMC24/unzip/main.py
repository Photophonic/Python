import FreeSimpleGUI as sg
from functions import extract_archive

sg.theme("Black")


# create a series of new elements for the GUI
label1 = sg.Text("Select file to unzip")
label2 = sg.Text("Select file destination")


input_box1 = sg.Input()
input_box2 = sg.Input()

# allows selection of singular files in a location
add_button1 = sg.FileBrowse("Choose", key="archive")
# use to select the folder location
add_button2 = sg.FolderBrowse("Choose", key="folder")


# create button to zip files
unzip_button = sg.Button("Unzip File")
# create success message
output_msg = sg.Text(key="output", text_color="green")

# create a window instance,
# items in layout need to be in brackets. Each pair is a row
window = sg.Window(
    "File Unzip",
    layout=[
        [label1, input_box1, add_button1],
        [label2, input_box2, add_button2],
        [unzip_button, output_msg],
    ],
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
    filepath = values["archive"]
    # get the folder path from the destination button dest_btn
    folder = values["folder"]
    # pass the file paths into the external function
    extract_archive(filepath, folder)
    # update success message
    window["output"].update(value="file unzipped")

# close the application when we close the window
window.close()
