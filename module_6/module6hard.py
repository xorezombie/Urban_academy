import math

class Figure:
    sides_count = 0
    def __init__(self, __color, __sides ):
        self.__color = list(__color) if self.__is_valid_color(__color) else [0, 0, 0]


    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, __sides):
        return len(__sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in __sides)

    def get_sides(self):
        return self.__sides

    def _len_(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
class Circle(Figure):
    sides_count = 1
    def __init__(self, __color, __sides):
        super().__init__(__color, __sides)
        self.__radius = self.__calculate_radius(self.get_sides()[0])

    def __calculate_radius(self, circumference):
        return circumference / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, __sides):
        super().__init__(__color, __sides)

    def get_sides(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

class Cube(Figure):
    sides_count = 12
    def __init__(self, __color, __sides):
        super().__init__(__color, __sides)

    if len(sides) == 1:
        sides = [__sides[0]] * self.sides_count
    super().__init__(__color, __sides)

    def get_volume(self):

        side = self.get_sides()[0]
        return side ** 3

circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())  # [55, 66, 77]

cube1.set_color(300, 70, 15)  # Не изменится (некорректный цвет)
print(cube1.get_color())  # [222, 35, 130]

# Проверка на изменение сторон
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится (количество сторон не совпадает с sides_count)
print(cube1.get_sides())  # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]

circle1.set_sides(15)  # Изменится (корректное количество сторон)
print(circle1.get_sides())  # [15]

# Проверка периметра (длины окружности)
print(len(circle1))  # 15

# Проверка объема куба
print(cube1.get_volume())  # 216

