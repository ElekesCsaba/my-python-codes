import os
import json


def delete_all_files(folder_path: str) -> None:

    # Delete all files in the given folder.
    for f in os.listdir(folder_path):
        os.remove(os.path.join(folder_path, f))


def create_thumbnail_folder(root_folder: str) -> str:

    # Create default thumbnail folder.
    thumbnail_folder = os.path.join(root_folder, "_thumbnails")

    # If folder does not exist make it.
    if not os.path.exists(thumbnail_folder):
        os.makedirs(thumbnail_folder)
    # If exists delete files in it.
    else:
        delete_all_files(thumbnail_folder)

    return thumbnail_folder


def create_json_file(root_folder: str, photo_data: dict) -> None:

    # Create default path of json file.
    json_file_path = os.path.join(root_folder, "photo_data.json")

    # Write into json file.
    with open(json_file_path, "w") as f:
        json.dump(photo_data, f)


def check_dir_exists(dir_name: str) -> None:

    # It checks whether the root folder exists.
    # If expression is False, the error message appears and the program stops at once.
    assert os.path.exists(dir_name), f"Folder does not exist: {dir_name}."


def get_root_folder_name(default_folder=None) -> str:

    # Only for testing default is being used.
    if not default_folder:
        root_folder = input("Folder name to start with: ")
    else:
        root_folder = default_folder

    return root_folder


def convert_list_to_lowercase(list_in: list) -> list:

    # The following code uses list comprehension to convert
    # a list of strings to lowercase (https://www.delftstack.com/howto/python/python-lowercase-list/)
    return [i.lower() for i in list_in]


def get_files(root_folder: str, files=[], filters=[]) -> list:
    """
    It looks for all files in the given folder and all sub folders.
    If filter is set, only the matching files are selected.
    :param root_folder:
    :param files:
    :param filters:
    :return: list
    """

    if filters:
        filters = convert_list_to_lowercase(filters)

    folder_content = os.listdir(root_folder)

    # Looking for the files in the given folder.
    for i in folder_content:
        # Checks it is a file.
        if os.path.isfile(os.path.join(root_folder, i)):
            # Checks if filter is set.
            if filters:
                if any(ele in i.lower() for ele in filters):
                    files.append(os.path.join(root_folder, i))
            else:
                files.append(os.path.join(root_folder, i))

    # Looking for sub dirs in the given folder.
    sub_folders = []
    for i in folder_content:
        folder_path = os.path.join(root_folder, i)
        if os.path.isdir(folder_path):
            sub_folders.append(folder_path)

    # Recursion with all sub folders.
    for sub_folder in sub_folders:
        get_files(sub_folder, files, filters)

    return files
