password_1 = int(input('Введите первый пароль: '))
def pass_2(number):
    result = ''
    param = 0
    if number % 2 == 0:
        param = number // 2
    else:
        param = number // 2 + 1
    for i in range(1,param):
        for j in range(2,number):
            if number % (i+j) == 0:
                result += str(i)+str(j)
    return result

print (pass_2(password_1))
