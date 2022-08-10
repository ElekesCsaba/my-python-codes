import os

folder_name = r"C:\Work\PythonSuli\pycore-220108\kepek"
file_name = r"C:\Work\PythonSuli\pycore-220108\kepek\photo_data.txt"

print(os.path.exists(folder_name))
print(os.path.isdir(folder_name))

print(os.path.exists(file_name))
print(os.path.isfile(file_name))
