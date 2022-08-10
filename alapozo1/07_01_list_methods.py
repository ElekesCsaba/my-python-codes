my_name = "Csaba"
names = ["Elek", "Decs", "Hus", "Edu", "Bela", "Edu", my_name]

print("Nr of occurance: ", names.count("Edu"))

names.append("Gábor")
print(names)

names.insert(3, "Johnny")
print(names)

names.remove("Edu") #csak az elsőt törli!!!
print(names)

del names[0]
print(names)

# names.clear()
# print(names)

numbers = list(range(6, 100)) #balról zárt, jobbról nyilt: 6-99
print(numbers[0:11])  #0. index - 11-1. index
print(numbers[0:46:3]) #0. index - 46-1. index, minden 3. index
