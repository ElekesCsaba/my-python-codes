phonebook = {"+36 30 528 9973": {
    "Name": "Robert",
    "Address": "Budapest"
}, "+36 31 234 4567": {
    "Name": "Csaba",
    "Address": "Pécs",
    "Age": 34
}, "+36 31 234 4533": {
    "Name": "Tibor",
    "Age": 45}
}

phonebook["+36 31 234 4533"]["Name"] = "Karesz" #modify

print(phonebook)

phonebook["+36 31 234 4533"] = "Tom"

print(phonebook)

# del phonebook["+36 31 234 4533"] #delete

print(phonebook.keys()) # key list
print(list(phonebook)) # cast to list of keys
print(phonebook.values()) # value list