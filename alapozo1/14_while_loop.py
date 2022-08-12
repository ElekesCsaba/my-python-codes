number = 0

while number < 10:
    number += 1
    if number == 6:
        break
    # if number == 7:
    #     continue
    else:
        print(number)
else:
    print("Number is 10.")

print("-"*100)

if number > 1 or number > 2 \
        or number > 3:
    print(number)
