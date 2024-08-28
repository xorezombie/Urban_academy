class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, login, password):
        self.data[login] = password

class User:
    def __init__(self, login, password, password_confirm):
        self.login = login
        if password == password_confirm:
            self.password = password


if __name__ == '__main__':
    database = Database()
    while True:
        choise = int(input('Выберите действие: \n1 - Вход\n2 - Регистрация\n'))
        if choise == 1:
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            if login in database.data:
                if password == database.data[login]:
                    print(f'Вход выполнен, {login}')
                    break
                else:
                    print('Пароль неверный')
            else:
                print('Пользователь не найден')
        if choise == 2:
            user = User(input('Введите логин: '), password := input('Введите пароль: '),
                        password2 := input('Повторите пароль: '))
            if password != password2:
                print('Пароли не совпадают')
                continue
            database.add_user(user.login, user.password)
        print(database.data)

