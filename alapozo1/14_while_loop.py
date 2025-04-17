number = 0

while number < 10:
    number += 1
    if number == 6:
        continue
    if number == 8:
        # break
        pass
    print(number)
else:
    print(f"Number is {number}.")

print("-"*100)

if number > 1 or number > 2 \
        or number > 3:
    print(number)
