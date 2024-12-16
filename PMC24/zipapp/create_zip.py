import zipfile
import pathlib


# the function will iterate over the filepaths and put them into to destination folder.
def create_archive(filepaths, dest_dir):
    # create destination path that can concat the text
    dest_path = pathlib.Path(dest_dir, "archive.zip")
    # similar to with open()
    with zipfile.ZipFile(dest_path, "w") as archive:
        # loop through each path in the filepaths variable
        for filepath in filepaths:
            # write to the archive the files
            archive.write(filepath)


if __name__ == "__main__":

    create_archive(
        filepaths=["zipapp/test.txt", "zipapp/test2.txt", "zipapp/test3.txt"],
        dest_dir="zipapp/dest",
    )
