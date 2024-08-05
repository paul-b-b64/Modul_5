from time import sleep

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        comp = False
        for i in self.users:
            if nickname == i.nickname:
                comp = True
        if not comp:
            self.current_user = User(nickname, password, age)
            self.log_in(nickname, password)
            self.users.append(self.current_user)
        else:
             print(f'Пользователь {nickname} уже существует')



        # return self.current_user

    def log_in(self, nickname, password):
        for i in self.users:
            if nickname == i.nickname and hash(password) == i.password:
                print(f'Вход выполнен, {nickname}')
                self.current_user = i
            # else:
            #     print('Нет такого пользователя, зарегистрируйтесь!')

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            comp = False
            for j in self.videos:
                if i.title == j.title:
                    comp = True
            if not comp:
                self.videos.append(i)
    def get_videos(self, word):
        find_video = []
        for i in self.videos:
            if word.lower() in i.title.lower():
                find_video.append(i.title)
        return find_video

    # def watch_video(self, title):
    #
    #     if len(self.current_user) == 0:
    #         print('Войдите в аккаунт, чтобы смотреть видео')
    #
    #


class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        # self.time_now = 0
        # self.adult_mode = False


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


if __name__ == '__main__':
    ur = UrTube()

    ur.register('Рупрехт', 'wtnd', 33)
    ur.register('Семен', 'dgld',25)
    ur.register('Герхардт', 'gdcle', 34)
    ur.register('Рупрехт', 'ccse', 33)


    print(len(ur.users))
    # ur.log_in('Семе', 'dgld')
    # print(len(ur.users))
    #
    # v1 = Video('Лучший язык программирования 2024 года', 200)
    # v2 = Video('Для чего девушкам парень-программист?', 10, adult_mode=True)
    # v3 = Video('Лучший язык программирования 2024 года', 50)
    # v4 = Video('Мухлоярск-1985', 2)
    # v5 = Video('Симеон - лучший из пловцов', 60)
    #
    # ur.add(v1, v2, v3, v4, v5, v1, v2, v3, v4, v5, v1, v2, v3, v4, v5)
    # print(len(ur.videos))
    # print(ur.get_videos('лучший'))
    # print(ur.get_videos('ПРОГ'))
    # print(ur.get_videos('плов'))

    # ur.videos.append(v1)
    # ur.videos.append(v2)
    # ur.videos.append(v3)
    # ur.videos.append(v4)
    # print(len(ur.videos))

    #
    # ur.register('tnt', 'dljf', 24)
    # print(ur.current_user.nickname)
    # print(ur.current_user.password)
    # print(ur.current_user.age)
    # # ur.watch_video('ntn')


    #
    # # ur.add(v1, v2, v3, v4)
    # # print(len(ur.videos))
    #
    # for j in ur.videos:
    #     print (j.title)
    #
    # print(ur.get_videos('лучший'))
    # #
    #
