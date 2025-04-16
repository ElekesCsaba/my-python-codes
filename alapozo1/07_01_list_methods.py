my_name = "Csaba"
names = ["Elek", "Decs", "Hus", "Edu", "Bela", "Edu", my_name]

print("Nr of occurance: ", names.count("Edu"))

names.append("Gábor")
print(names)

names.insert(3, "Johnny")
print(names)

print(f"Edu: {names.count("Edu")}")

names.remove("Edu") # csak az elsőt törli!!!
print(names)

del names[0]
print(names)

names.clear()
print(names)

numbers = list(range(10))
print(numbers)

numbers = list(range(6, 100)) # balról zárt, jobbról nyilt: 6-99
print(numbers)
print(numbers[0:13])  # 0 - 12. index
print(numbers[0:13:3]) # 0 - 12. index, de csak minden 3.
