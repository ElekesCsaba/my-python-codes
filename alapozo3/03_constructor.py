class Dice:
    # constructor of a class
    # double underscore method = dunder method
    def __init__(self, sides, color):
        # instance attribute
        self.sides = sides
        self.color = color

        # variable used just inside this method
        name = "robert"

    def __str__(self):
        return f"Sides: {self.sides}, color: {self.color}."


my_dice1 = Dice(6, "white")
my_dice2 = Dice(10, "blue")
my_dice3 = Dice(20, "red")

# adding new attribute to this instance only
my_dice1.name = "Csaba"

my_dice1.color = 10
print(my_dice1.name)  # my_dice2.name does not exist!!!

print(dir(my_dice2))
