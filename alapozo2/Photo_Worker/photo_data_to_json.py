from utilities.file_utils import get_files, get_root_folder_name, check_dir_exists, create_json_file
from utilities.image_utils import create_image_dict


def main():

    # Ask root folder name from user.
    root_folder = get_root_folder_name(default_folder=r"C:\Work\PythonSuli\pycore-220108\kepek")

    # Check folder exists.
    check_dir_exists(root_folder)

    # Get image files from root folder.
    file_list = get_files(root_folder, filters=[".jpg", ".jpeg", ".png"])

    # Get Exif data in a dictionary.
    photo_data = create_image_dict(file_list)

    # Create and save json file in root folder.
    create_json_file(root_folder, photo_data)


main()
