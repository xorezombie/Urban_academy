def print_params(a = 1, b ='строка', c = True):
    print(a, b, c)
print_params()
print_params(6)
print_params(34, 'Мяу')
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [12 , 'Hello', False]
values_dict = {'a': 1.2, 'b': "Go", 'c': [1, 2, 3]}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [2024, 'год']
print_params(*values_list_2, 42)
