class Dice:
    def __init__(self, color, sides):
        self.__color = color
        self.__sides = sides

    @property  # getter
    def color(self):
        return self.__color

    @property  # getter
    def sides(self):
        return self.__sides

    @color.setter  # setter
    def color(self, new_color):
        assert isinstance(new_color, str), "Color must be of type string!"
        self.__color = new_color

    @sides.setter  # setter
    def sides(self, new_sides):
        assert isinstance(new_sides, int) and new_sides >= 4, "Sides must be int >= 4!"
        self.__sides = new_sides

    def __str__(self):
        return f"{self.color} - {self.sides}"


my_dice = Dice("red", 6)
print(my_dice)

my_dice.color = "green"
my_dice.sides = 78
print(my_dice)
