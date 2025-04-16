print("Hello")
print("well" + "hello")
print("fdfd dfd ".upper())
print("WERT".lower())
print("fdfD dfd".title()) # CTRL + D = a sort lemásolja
print("fdfD dfd".title())
print("fdfd dfd".replace("fd", "ddddeded", -1))
print("ddf s s sd s s".split()) # space -> listát ad vissza
print("ddf s s sd s s".split("sd"))
print("ddf s s sd s s".split("s"))
print("csaba fgt".capitalize())

my_string = "Elekes Csaba"

# right 2 characters = ba
print(my_string[-2:])

# left 3 characters = Ele
print(my_string[:3])

# 4th through 6th characters (index starts at 0) = es - jobbról nyitott! 4. és 5. karakter lesz!
print(my_string[4:6])

for i, name in enumerate(my_string):
    print(f"{i} - {name}")