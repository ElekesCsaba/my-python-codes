# parameter notations: type (nem kötelező)
def say_hello(name: str, address: str, email: str):
    print(f"Hello {name}! Your address is {address}, {email}.")


say_hello("Csaba", "Budapest", "csaba@email.hu")