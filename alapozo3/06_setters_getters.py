class Dice:
    class_weight = 10

    def __init__(self, sides, color):
        self._sides = sides
        self._color = color
        self.__weight = Dice.class_weight

    # getter for sides
    def get_sides(self):
        return self._sides

    # getter for color
    def get_color(self):
        return self._color

    # getter for weight
    def get_weight(self):
        return f"The weight is: {self.__weight}"

    # setter for the color attribute
    def set_color(self, color):
        assert isinstance(color, str), "Color must be of type string!"
        self._color = color

    # setter for weight
    def set_weight(self, weight):
        assert isinstance(weight, int) and weight >= 0, "Weight must be int >= 0!"
        self.__weight = weight


my_dice = Dice(6, "white")
print(my_dice.get_sides())
print(my_dice.get_color())

my_dice.set_color("blue")
print(my_dice.get_color())

print(my_dice.get_weight())

Dice.class_weight = 86
my_dice_w = Dice(8, "green")
print(my_dice_w.get_weight())

my_dice_w.set_weight(893)

print(my_dice_w.get_weight())
