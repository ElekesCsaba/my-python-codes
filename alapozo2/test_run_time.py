from utilities.decorators import timer
from utilities.recursive_functions import fibonacci


@timer
def calculating_with_for(my_num):
    num1 = 1
    num2 = 1
    for nr in range(3, my_num + 1):
        result = num1 + num2
        num1 = num2
        num2 = result
    return result


@timer
def calculating_with_recursive_function(my_num):
    return fibonacci(my_num)


def main():
    my_num = 40

    result = calculating_with_for(my_num)
    print(f"Result with for: {result}")

    result = calculating_with_recursive_function(my_num)
    print(f"Result with recursion: {result}")


main()
