# def find_max(list_):
#     max_= list_[0]
#     for i in list_:
#         if i > max_:
#             max_ = i
#     return max_
# print(find_max([1 , 3, 4, 24]))

# def count_even(list_):
#     even = 0
#     for i in list_ :
#         if i % 2 == 0:
#             even += 1
#     return even
# print(count_even([2, 13, 1, 24, 12, 3]))

def unique(list_):
    list_1 = []
    for i in list_:
        if i not in list_1:
            list_1.append(i)
    return list_1
print(unique([1, 3, 1, 3, 4, 132, 1, 132]))




class House:
    def __init__(self, name, number_of_floors):
        # Инициализация атрибутов
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        # Проверка корректности этажа
        if 1 <= new_floor <= self.number_of_floors:
            # Вывод всех этажей от 1 до new_floor включительно
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")