class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name


class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name


class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

# Создаем объекты
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Выводим названия объектов
print(a1.name)
print(p1.name)

# Проверяем начальные состояния
print(a1.alive)
print(a2.fed)

# Пытаемся съесть растения
a1.eat(p1)  # Волк пытается съесть не съедобный цветок
a2.eat(p2)  # Хатико съедает фрукт

# Проверяем конечные состояния
print(a1.alive)
print(a2.fed)
