class UrTube:
    users = {}
    videos = []
    current_user = None


    def register(self, nickname, password, age):
        nickname = input('Введите логин: ')
        password = hash(input('Введите пароль: '))
        age = input('Ваш возраст: ')
        if nickname in UrTube.users:
            print(f'Пользователь {nickname} уже существует')
        else:
            UrTube.current_user = User(nickname, password, age)


    # def log_in(nickname, password):
    #     nickname = input('Введите логин: ')
    #     password = input('Введите пароль: ')
    #
    #     if nickname in users:
    #         if password == users[]:
    #             print(f'Вход выполнен, {login}')
    #             break
    #         else:
    #             print('Неверный пароль')
    #     else:
    #         print('Пользователь не найден')
    #


class Video:
    time_now = 0
    adult_mode = False

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def __str__(self):
        return (f'Название: {self.title}, Продолжительность: {self.duration},'
                f' Остановлен на: {self.time_now}, {self.adult_mode}')

# vid = Video('Gustav', 2)
# vid.time_now = 6
# print(vid)

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

# User1 = User('glj', 'faf', 24)
# print(User1.password)
# print(hash('faf'))


ur = UrTube()
ur.register('nickname', 'password', 22)
print(ur.current_user)
