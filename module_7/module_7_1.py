from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        data = file.read()
        file.close()
        return data

    def add(self, *products):
        current_products = self.get_products()
        products_list = current_products if current_products else ""

        file = open(self.__file_name, 'a')

        for product in products:
            product_str = str(product)
            if product_str not in products_list:
                file.write(product_str + '\n')
                print(f'Добавлен: {product_str}')
                products_list += product_str + '\n'
            else:
                print(f'Продукт {product_str} уже есть в магазине')

        file.close()

        print('Текущие продукты в магазине:')
        pprint(products_list)

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
p4 = Product('Water', 70.0, 'Drink')

print(p1)
print(p4)

s1.add(p1, p2, p3, p4)
print(s1.get_products())
