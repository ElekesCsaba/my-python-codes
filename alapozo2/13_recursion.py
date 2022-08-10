from utilities.recursive_functions import fibonacci


def call_myself(n):
    if n >= 10:
        print("n = 10")
    else:
        print(f"I called myself {n} times.")
        call_myself(n+1)


# call_myself(0)
print(fibonacci(10))

