def add_numbers(a, b) -> int:
    return a+b


def multiply_numbers(a, b):
    return a*b


def divide_numbers(a: int, b: int) -> float:
    # ternary operator
    return 0 if b == 0 else a/b


# result = return_nothing() returns None
def return_nothing():
    pass


result = add_numbers(10, 20)
result = multiply_numbers(result, 10)
result = divide_numbers(result, 3)

print(f"Result is: {result}.")


