class House:
    house_history = []
    def __new__(cls, *args, **kwargs):
        cls.house_history.append(args[0])
        instance = super().__new__(cls)
        return instance

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")



h1 = House('ЖК Олимп', 23)
print(House.house_history)
h2 = House('Дом у дороги', 4)
print(House.house_history)
h3 = House('ЖК Московкий', 12)
print(House.house_history)

del h2
del h3