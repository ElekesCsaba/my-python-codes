import os
from PIL import Image, ExifTags
import json
from openpyxl import Workbook

photo_folder = r"c:\Work\PythonSuli\pycore-220108\kepek"
photos = []
extensions = [".jpg", ".jpeg", ".png"]
photo_data_txt = ""
photo_data_dict = {}

# read directory
files = os.listdir(photo_folder)

# filter for extensions
for file in files:
    name, ext = os.path.splitext(file)

    if ext.lower() not in extensions:
        continue

    photos.append(file)

# open excel sheet
workbook = Workbook()
sheet = workbook.active

# add header to workbook
sheet["A1"] = "Path"
sheet["B1"] = "Date"
sheet["C1"] = "Size"
sheet["D1"] = "Camera"
sheet["E1"] = "ISO"

# open images with PIL (Python Image Library) = Pillow
for index, file in enumerate(photos):
    # op.path.join is a system independent method!!!
    photo_path = os.path.join(photo_folder, file)
    img = Image.open(photo_path)

    # add data for text file
    photo_data_txt += f"{file} {img.size}\n"

    # create dictionary for json file
    photo_data_dict[file] = {
        "x": img.size[0],
        "y": img.size[1],
        "path": photo_path,
        "date": None,
        "camera": None,
        "iso": None
    }

    #  add data to workbook
    sheet[f"A{index + 3}"] = photo_path
    sheet[f"C{index + 3}"] = f"{img.size[0]} x {img.size[1]}"

    # get exif data
    exif_data = img._getexif()
    if not exif_data:
        continue

    # load some ExifTag values into dictionary and workbook
    for key, value in exif_data.items():
        tag_name = ExifTags.TAGS.get(key)

        match tag_name:
            case "DateTimeOriginal":
                photo_data_dict[file]["date"] = value
                sheet[f"B{index + 3}"] = value
            case "Model":
                photo_data_dict[file]["camera"] = value
                sheet[f"D{index + 3}"] = value
            case "ISOSpeedRatings":
                photo_data_dict[file]["iso"] = value
                sheet[f"E{index + 3}"] = value
            case _:
                continue

# create and write text file
text_file_path = os.path.join(photo_folder, "photo_data.txt")
with open(text_file_path, "w") as f:
    f.write(photo_data_txt)

# create and write json file
json_file_path = os.path.join(photo_folder, "photo_data.json")
with open(json_file_path, "w") as f:
    json.dump(photo_data_dict, f)

# save Excel file
excel_file_path = os.path.join(photo_folder, "photo_data.xlsx")
workbook.save(excel_file_path)