import os

print(os)
# r = raw string (csak Windows!), nem foglalkozik a spec karakterekkel pl. \a-val vagy \n-el

my_dir = r"C:\Dropbox\PythonSuli\pycore-220108\alapozo1"
# files = os.listdir(r"C:\Dropbox\PythonSuli\pycore-220108\alapozo1")
files = os.listdir(my_dir) # rejtett mappákat is listázza

"""
print(files)
print(len(files))
print(files[-1])
"""

for i, name in enumerate(files):
    print(f"{i} - {name}")
