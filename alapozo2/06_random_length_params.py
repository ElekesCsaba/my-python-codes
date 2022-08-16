def random_length_params(*args):
    print(args, type(args))
    # tuple - only readable param!

    for i in args:
        print(i)


random_length_params(78, "Csaba", [3, 4])
