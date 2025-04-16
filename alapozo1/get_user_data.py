phonebook = {}

name = "Csaba" # input("Name: ")
phone = "+36405678999" # input("Phone: ")
email = "gr@gklom.com" # input("Email: ")
phonebook[phone] = {"name": name, "email": email}

name = "Peti" # input("Name: ")
phone = "+36703448899" # input("Phone: ")
email = "peti@halom.hu" # input("Email: ")
phonebook[phone] = {"name": name, "email": email}

print(phonebook)
print(phonebook.keys())
print(phonebook.values())
print(list(phonebook)) #castolás, csak a route kulcsok lesznek a listában!

for i in phonebook.keys():
    print(i)

for i in phonebook.values():
    print(i)