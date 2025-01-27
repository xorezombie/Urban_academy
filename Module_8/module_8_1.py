def add_everything_up(a, b):
    try:
        result = a+b
    except TypeError:
        return str(a) + str(b)
    else:
        if isinstance(a,int) and isinstance(b,int):
            print('Мы сложили числа. Ура')
        return result


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up(22, 32))
