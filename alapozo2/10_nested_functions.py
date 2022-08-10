name = "Gábor"


def say_hello(name_in):
    print(name)
    print(name_in)

    def say_my_name():
        print(name)

    say_my_name()


say_hello("Csaba")
