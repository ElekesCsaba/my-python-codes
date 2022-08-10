def countdown(n, nums=[]):
    if n == 0:
        return
    else:
        nums.append(n)
        countdown(n - 1, nums)
        return sorted(nums)


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def rec_sum(n):
    if n == 1:
        return 1
    else:
        return n + rec_sum(n - 1)


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def power_of_10(n):
    if n == 0:
        return 1
    else:
        return power_of_10(n-1) * 10


def power_of_n(nr, n):
    if n == 0:
        return 1
    else:
        return power_of_n(nr, n-1) * nr


def dec_to_other_system(dec: int, nr: int) -> str:
    if dec == 0:
        return ""
    else:
        return dec_to_other_system(int(dec/nr), nr) + str(dec % nr) + "|"
