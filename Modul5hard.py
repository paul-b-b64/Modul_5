class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = []

    def register(self, nickname, password, age):
        for i in range(len(self.users)):
            if (nickname == getattr(self.users[i], 'nickname') and
                    hash(password) == getattr(self.users[i], 'password') and
                    age == getattr(self.users[i], 'age')):
                print(f'Пользователь {nickname} уже существует')
            else:
                if i == len(self.users) - 1:
                    self.current_user = User(nickname, password, age)
                    self.users.append(self.current_user)
        return self.current_user

    def log_in(self, nickname, password):
        for i in range(len(self.users)):
            if nickname == getattr(self.users[i], 'nickname') and hash(password) == getattr(self.users[i], 'password'):
                print(f'Вход выполнен, {nickname}')
                self.current_user = self.users[i]
                break
            else:
                if i == len(self.users)-1:
                    print('Нет такого пользователя, зарегистрируйтесь!')
        return self.current_user

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            if len(self.videos) != 0:
                for j in range(len(self.videos)):
                    if i.title != getattr(self.videos[j], 'title'):
                        self.videos.append(i)
            else:
                self.videos.append(i)



class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
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
        self.password = hash(password)
        self.age = age


if __name__ == '__main__':
    ur = UrTube()

    user1 = User('Семен', 'dgld',25)
    ur.users.append(user1)
    user2 = User('Герхардт', 'gdcle', 34)
    ur.users.append(user2)
    user3 = User('Рупрехт', 'wtnd', 33)
    ur.users.append(user3)
    print(len(ur.users))

    ur.register('Рупрехт', 'wtnd', 33)
    print(len(ur.users))
    ur.log_in('Семе', 'dgld')
    print(len(ur.users))

    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень-программист?', 10, adult_mode=True)
    v3 = Video('Лучший язык программирования 2024 года', 2)

    ur.add(v1, v2, v3, v1, v3)

    print(len(ur.videos))



    # print(ur.users[0])
    # print('Семен' in ur.users[0])
    # print('Семен' in ur.users[1])
    # for f in ur.users:
    #     print('Семен' in f)
    # #

    # ur.log_in('Семен', 'dgld')
    # print(ur.current_user)
