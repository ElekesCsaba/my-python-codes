status = 1004

print("If, elif, else")
if status == 100:
    print("100")
elif status == 200:
    print("200")
elif status == 300:
    print("300")
else:
    print("Unknown.")

print("match, case")
match status:
    case 100:
        print("100")
    case 200:
        print("200")
    case _:
        print("Unknown")