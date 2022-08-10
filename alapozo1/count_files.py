import os

# print(os)
# r = raw string (csak Windows!), nem foglalkozik a spec karakterekkel \a-val

my_dir = r"c:\Work\PythonSuli\pycore-220108\alapozo1"
# files = os.listdir(r"c:\Work\PythonSuli\pycore-220108\alapozo1")
files = os.listdir(my_dir)

"""
print(files)
print(len(files))
print(files[-1])
"""

for i, name in enumerate(files):
    print(i, "-", name)

my_str = "Csaba"
for i, name in enumerate(my_str):
    print(i, "-", name)
