names = ["Robert", "Csaba", "Kriszta", "Csilla"]

# empty inside with pass
for name in names:
    # pass
    print(name)

print("break".ljust(50, "-"))
for i in names:
    pass
    if i == "Kriszta":
        break
    print(i)

print("continue".ljust(50, "-"))
for i in names:
    if i == "Kriszta":
        continue
    print(i)

print("enumerate".ljust(50, "-"))
for index, value in enumerate(names):
    print(f"Index: {index}, name: {value}")