def random_length_keyword_params(**kwargs):
    print(kwargs)
    print(type(kwargs))

    print("List of keys".ljust(100, "-"))
    for i in list(kwargs.keys()):
        print(i)

    print("List of values:".ljust(100, "-"))
    for i in list(kwargs.values()):
        print(i)


random_length_keyword_params(
    first_name="Csaba",
    last_name="Elekes",
    email="wer@gt.hu"
)