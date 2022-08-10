from utilities.file_utils import get_files, get_root_folder_name, check_dir_exists, create_thumbnail_folder
from utilities.image_utils import create_thumbnails


def main():

    # Ask root folder name from user.
    root_folder = get_root_folder_name(default_folder=r"C:\Work\PythonSuli\pycore-220108\kepek")

    # Check folder exists.
    check_dir_exists(root_folder)

    # Make an empty _thumbnails folder in the root folder.
    thumbnail_folder = create_thumbnail_folder(root_folder)

    # Get image files from root folder.
    file_list = get_files(root_folder, filters=[".JPG", ".jpeg", ".png"])

    # Create and save thumbnails.
    create_thumbnails(file_list, thumbnail_folder, thumb_size=150)

    # Print message.
    print(f"Nr of files converted: {len(file_list)} in {thumbnail_folder}.")


main()
