# global scope / variable
name = "Csaba"
# constant - upper case letter
FOLDER_PATH = "c:\\...."


def say_my_name():
    # local scope / variable
    # name = "Tamás"
    # email = "ssss"
    print(name)


def override_global():
    global name
    name = "Más"


# global variable (name) is here = Csaba
# local variable (email) is not available here
say_my_name()

override_global()
say_my_name()

name = "sergre"
print(name)
