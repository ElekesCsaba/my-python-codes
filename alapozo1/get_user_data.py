phonebook = {}

name = input("Name: ")
phone = input("Phone: ")
email = input("Email: ")
phonebook[phone] = {"name": name, "email": email}

name = input("Name: ")
phone = input("Phone: ")
email = input("Email: ")
phonebook[phone] = {"name": name, "email": email}

print(phonebook)
print(phonebook.keys())
print(list(phonebook)) #castolás