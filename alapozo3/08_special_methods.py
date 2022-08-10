class Dice:
    def __init__(self, color, sides):
        self._color = color
        self._sides = sides

    # @property
    # def sides(self):
    #     return self._sides

    @property
    def color(self):
        return self._color

    def __str__(self):
        return f"Color: {self.color} Sides: {self._sides}"


class Person:
    def __init__(self, name, age, email):
        self._name = name
        self._age = age
        self._email = email

    def __eq__(self, other):
        return isinstance(other, Person) and self._age == other._age

        return False

    def __hash__(self):
        return hash(self._age)

    def __str__(self):
        return f"Name: {self._name}\nAge: {self._age}\nEmail: {self._email}"

    def __repr__(self):
        return self._name


my_dice1 = Dice("White", 6)
my_dice2 = Dice("Red", 10)
my_dice3 = Dice("Blue", 20)
my_dices = [my_dice1,  my_dice2, my_dice3]

my_person1 = Person("Robert", 34, "robert@gmail.com")
my_person2 = Person("Csaba", 20, "csaba@gmail.com")
my_person3 = Person("Kriszta", 26, "kriszta@gmail.com")

my_persons = [my_person1, my_person2, my_person3]

# Dice __str__ is ok.
print(my_dice1)
# Dice __repr__ is missing. It is good for list.
print(my_dices)

# Person __str__ is ok.
print(my_person3)
# Person __repr__ is ok.
print(my_persons)

John = Person("John", 34, "john@mail.com")
Jane = Person("Jane", 34, "jane@mail.com")

print(John is Jane)
print(John == Jane)
print(John == 32)

print(hash(John))
print(hash(Jane))
