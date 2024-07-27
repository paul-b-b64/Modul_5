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
        for i in
        if nickname in self.users:
            if hash(password) == self.users[nickname]:
                print(f'Вход выполнен, {nickname}')
                self.current_user = self.users[nickname]
            else:
                print('Неверный пароль')
        else:
            print('Нет такого пользователя, зарегистрируйтесь!')
            # self.register()
class Video:

    def __init__(self, title, duration):
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
    user1 = User('Семен', 'dgld', 25)
    user2 = User('Герхардт', 'gdcle', age=34)
    ur.current_user = [user1.nickname, user1.password, user1.age]
    ur.users.append(ur.current_user)
    ur.current_user = [user2.nickname, user2.password, user2.age]
    print(ur.current_user)
    ur.users.append(ur.current_user)
    print(ur.users)
    print(ur.current_user in ur.users)
    print(ur.users[0])
    print('Семен' in ur.users[0])
    print('Семен' in ur.users[1])
    for f in ur.users:
        print('Семен' in f)
    #




    # ur.log_in('Семен', 'dgld')
    # print(ur.current_user)

