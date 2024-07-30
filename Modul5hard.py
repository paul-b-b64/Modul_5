class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = []

    def register(self, nickname, password, age):
        hpass = hash(password)
        if nickname in self.users:
            print(f'Пользователь {nickname} уже существует')
        else:
            self.current_user = User(nickname, hpass, age)
            self.users.append(self.current_user)

    def log_in(self, nickname, password):
        for i in range(len(ur.users)):
            if nickname == getattr(ur.users[i], 'nickname') and hash(password) == getattr(ur.users[i], 'password'):
                print(f'Вход выполнен, {nickname}')
                ur.current_user = ur.users[i]
                break
            else:
                if i == len(ur.users)-1:
                    print('Нет такого пользователя, зарегистрируйтесь!')



class Video:

    def __init__(self, title, duration, time_now, adult_mode):
        self.title = title
        self.duration = duration
        time_now = 0
        adult_mode = False

    def __str__(self):
        return (f'Название: {self.title}, Продолжительность: {self.duration},'
                f' Остановлен на: {self.time_now}, {self.adult_mode}')


# vid = Video('Gustav', 2)
# vid.time_now = 6
# print(vid)

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


if __name__ == '__main__':
    ur = UrTube()
    #
    # while True:
    # choice = int(input('Здравствуйте! Выберите действие: \n1 - Вход\n2 - Регистрация\n'))
    # if choice == 1:
    #     ur.register('nickname', 'password', 22)
    #     if ur.current_user in ur.users:
    #         print(f'Вход выполнен, {ur.current_user.nickname}')
    #     #         break
    #     #     else:
    #     #         print('Неверный пароль')
    #     # else:
    #     #     print('Пользователь не найден')
    # # if choice == 2:
    # #     user = User(input('Введите логин:'), password := input('Введите пароль:'),
    # #                 password2 := input('Подтвердите пароль:'))
    # #     # if len(password) < 4:
    # #     #     print('короткий пароль')
    # #     if password != password2:
    # #         print('Пароли не совпадают, пробуйте еще')
    # #         continue
    # #     database.add_user(user.username, user.password)
    # # print(database.data)
    #
    user1 = User('Семен', 'dgld',25)
    ur.users.append(user1)
    user2 = User('Герхардт', 'gdcle', 34)
    ur.users.append(user2)
    user3 = User('Рупрехт', 'wtnd', 33)
    ur.users.append(user3)


    ur.log_in('Семен', 'dgld')

    # print(ur.users)
    # print(user1 in ur.users)
    # print(user2 in ur.users)
    # for i in range(len(ur.users)):  #такая вот конструкция родилась
    #     print(getattr(ur.users[i], 'nickname'))

    # print(ur.users[0])
    # print('Семен' in ur.users[0])
    # print('Семен' in ur.users[1])
    # for f in ur.users:
    #     print('Семен' in f)
    # #

    # ur.log_in('Семен', 'dgld')
    # print(ur.current_user)
