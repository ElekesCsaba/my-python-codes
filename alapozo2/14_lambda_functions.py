add_numbers = lambda a, b: a+b
multiply_numbers = lambda a, b: a*b
divide_numbers = lambda a, b: a/b


print(add_numbers(4, 6))
print(multiply_numbers(4, 6))
print(divide_numbers(4, 6))

# keresztnév szerint rendezni!!!
name_list = ["Vári Róbert", "Kiss Elemér", "Nagy Adrienn", "Elekes Csaba"]
print(sorted(name_list))
print(sorted(name_list, key=lambda name: name.split()[-1]))

students = {
    0: {"name": "Vári Róbert", "grade": 34},
    1: {"name": "Kiss Elemér", "grade": 23},
    4: {"name": "Nagy Adrienn", "grade": 11},
    3: {"name": "Elekes Csaba", "grade": 99}
}

key_list = sorted(students)

for key in key_list:
    print(f"Key: {key}, value: {students[key]['name']}.")

grade_list = sorted(students, key=lambda id: students[id]["grade"], reverse=True)

print("")

for key in grade_list:
    print(f"Key: {key}, value: {students[key]['grade']}.")
