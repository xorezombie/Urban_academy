class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print('Такого этажа не существует')


h1 = House('ЖК Олимп', 23)
h2 = House('Дом у дороги', 4)

h1.go_to(11)
h2.go_to(10)

