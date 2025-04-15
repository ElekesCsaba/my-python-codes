# 1.feladat
import random

print("Egy számot kell kitalálnod 1 és az általad megadott felső határérték között.")
hatar = int(input("Adja meg a határértéket: "))

# 2.feladat
tippek = []
szam = random.randint(1, hatar)
print(szam)

# 3.feladat
szamlalo = 1
gondolt = int(input("Melyik számra gondoltam (kilépés: -1)? "))
tippek.append(gondolt)

while szam != gondolt:

    szamlalo += 1

    if gondolt == -1:
        break

    elif gondolt < szam:
        print("Nagyobb számra gondoltam!")
    else:
        print("Kisebb számra gondoltam!")

    gondolt = int(input("Melyik számra gondoltam (kilépés:-1)? "))
    tippek.append(gondolt)

if gondolt == -1:
    print("Sajnálom a kitalálandó szám", szam, "volt.")
else:
    print("Eltaláltad", szamlalo, "próbálkozásból!")
    print(tippek)