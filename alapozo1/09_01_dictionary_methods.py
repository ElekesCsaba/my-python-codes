phonebook = {
    "+36 30 528 9973": {
        "Name": "Robert",
        "Address": "Budapest"
    },
    "+36 31 234 4567": {
        "Name": "Csaba",
        "Address": "Pécs",
        "Age": 34
    },
    "+36 31 234 4533": {
        "Name": "Tibor",
        "Age": 45
    }
}

phonebook["+36 31 234 4533"]["Name"] = "Karesz" #modify

print(phonebook)

phonebook["+36 31 234 4533"] = "Tom"

print(phonebook["+36 31 234 4533"])

# delete key from dictionary
del phonebook["+36 31 234 4533"]

print(phonebook)

# empty dictionary
phonebook.clear()

print(phonebook)