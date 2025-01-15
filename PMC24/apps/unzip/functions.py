import zipfile


def extract_archive(filepath, folder):
    # to view the contents of the zip file use read
    with zipfile.ZipFile(filepath, "r") as archive:
        archive.extractall(folder)


if __name__ == "__main__":

    extract_archive(
        # list of files & paths
        filepath="unzip/dest/archive.zip",
        # string dest
        folder="unzip/dest",
    )
