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

    def watch_video(self, title):
        def play():
            for j in range(i.duration):
                print(j)
                sleep(1)
            print('Конец видео')

        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for i in self.videos:
                if title == i.title:
                    if not i.adult_mode:
                        play()
                    else:
                        if self.current_user.age > 18:
                            play()
                        else:
                            print('Вам нет 18 лет, пожалуйста покиньте страницу')

class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


if __name__ == '__main__':
    ur = UrTube()

    ur.register('Рупрехт', 'wtnd', 33)
    ur.register('Семен', 'dgld', 15)
    ur.register('Герхардт', 'gdcle', 34)
    ur.register('Рупрехт', 'ccse', 33)

    ur.log_out()

    ur.log_in('Семен', 'dgld')

    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень-программист?', 10, adult_mode=True)
    v3 = Video('Лучший язык программирования 2024 года', 50)
    v4 = Video('Мухлоярск-1985', 2)
    v5 = Video('Симеон - лучший из пловцов', 5)

    ur.add(v1, v2, v3, v4, v5, v1, v2, v3, v4, v5, v1, v2, v3, v4, v5)
    print(len(ur.videos))
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))
    print(ur.get_videos('плов'))

    ur.watch_video('Для чего девушкам парень-программист?')
