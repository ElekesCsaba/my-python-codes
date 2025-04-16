status = 100

status_dict = {100: "continue", 200: "ok", 300: "multiple choices"}

print("Dictionary")
print(status_dict[status])

print("If, elif, else")
if status == 100:
    print("continue")
elif status == 200:
    print("ok")
elif status == 300:
    print("multiple choices")
else:
    print("unknown.")

print("match, case")
match status: # 3.10 verziótól
    case 100:
        print("continue")
    case 200:
        print("ok")
    case 300:
        print("multiple choices")
    case _:
        print("unknown")