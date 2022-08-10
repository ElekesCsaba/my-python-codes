import os


def get_files(root_folder: str, files=[], name_filter=None) -> list:
    """
    It looks for all files in the given folder and all sub folders.
    If filter is set, only the matching files are selected.
    :param root_folder:
    :param files:
    :param name_filter:
    :return: list
    """

    # It checks whether the root exists.
    # If expression is False, the error message appears and the program stops at once.
    assert os.path.exists(root_folder), f"Folder does not exist: {root_folder}."

    folder_content = os.listdir(root_folder)

    # Looking for the files in the given folder.
    for i in folder_content:
        # Checks it is a file.
        if os.path.isfile(os.path.join(root_folder, i)):
            # Checks if filter is set.
            if name_filter:
                if name_filter.lower() in i.lower():
                    files.append(os.path.join(root_folder, i))
            else:
                files.append(os.path.join(root_folder, i))

    # Looking for sub dirs in the given folder.
    sub_folders = []
    for i in folder_content:
        if os.path.isdir(os.path.join(root_folder, i)):
            sub_folders.append(os.path.join(root_folder, i))

    # Recursion with all sub folders.
    for sub_folder in sub_folders:
        get_files(sub_folder, files, name_filter)

    return files


# Only for testing.
# It will not run when function will be called.
if __name__ == '__main__':
    found_files = get_files(r"c:\Work\PythonSuli\pycore-220108\alapozo2", name_filter=".py")
    for f in found_files:
        print(f)
