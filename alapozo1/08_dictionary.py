phonebook = {
    "+36 30 528 9973": {
        "Name": "Robert",
        "Address": "Budapest"
    },
    "+36 31 234 4567": {
        "Name": "Csaba",
        "Address": "Pécs",
        "Age": 34
    }
}

print(phonebook["+36 31 234 4567"]["Name"])
print(phonebook["+36 31 234 4567"]["Address"])
print(phonebook["+36 31 234 4567"]["Age"])
