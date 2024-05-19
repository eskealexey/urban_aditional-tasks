import time
class Video:
    def __init__(self, title: str, duration: int, time_now: int = 0, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def get_title(self):
        return self.title

    def __str__(self):
        return f'{self.title}'


class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def get_nickname(self):
        return self.nickname

    def get_hash(self):
        return self.password

    def get_age(self):
        return self.age
    def __str__(self):
        return f'Имя: {self.nickname}, Возраст: {self.age}'

    def __eq__(self, other):
        return self.nickname == other.nickname and self.password == other.password

class UrTube:
    users = []
    videos = []
    current_user = None

    def log_in(self, nickname: str, password: str):
        """Метод log_in, который принимает на вход аргументы: login, password
        и пытается найти пользователя в users с такмими же логином и паролем.
        Если такой пользователь существует, то current_user меняется на найденного.
        Помните, что password передаётся в виде строки, а сравнивается по хэшу."""
        password = hash(password)
        chek_user = User(nickname, password, None)
        for user in self.users:
            if user == chek_user:
                self.current_user = user

    def register(self, nickname: str, password: str, age: int):
        """Метод register, который принимает три аргумента: nickname, password, age,
        и добавляет пользователя в список, если пользователя не существует (с таким же nickname).
        Если существует, выводит на экран: "Пользователь {nickname} уже существует".
        После регистрации, вход выполняется автоматически."""
        nickname = nickname
        password = hash(password)
        age = age
        us = User(nickname, password, age)
        lst_ = [u for u in self.users]
        lst_nick = []
        for nick in lst_:
            lst_nick.append(User.get_nickname(nick))
        if us.nickname not in lst_nick:
            self.users.append(us)
            self.current_user = us
            self.__str__()
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        """Метод log_out для сброса текущего пользователя на None."""
        self.current_user = None

    def add(self, *args):
        """Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos,
        если с таким же названием видео ещё не существует. В противном случае ничего не происходит."""
        lst_ = [v for v in ur.videos]
        lst_t = []
        for t in lst_:
            lst_t.append(Video.get_title(t))
        for video in args:
            if not video.get_title() in lst_t:
                self.videos.append(video)

    # classmethod
    # def __change_user(cls):
    #     user = cls.current_user
    #     if user != None:
    #         print(user)
    #         return False
    #     else:
    #         print(user)
    #         return True


    def get_videos(self, word: str):
        """Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео,
        содержащих поисковое слово. Следует учесть, что слово 'UrbaN'
        присутствует в строке 'Urban the best' (не учитывать регистр)."""
        list_title = []
        list_video = [v for v in self.videos]
        for video in list_video:
            if word.lower() in video.title.lower():
                list_title.append(video.title)
        return list_title

    def watch_video(self, title_video: str):
        """Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела),
        то ничего не воспроизводится, если же находит ведётся отчёт в консоль на какой секунде ведётся просмотр.
        После текущее время просмотра данного видео сбрасывается."""
        if not self.current_user:
            print('Войдите в аккаунт чтобы смотреть видео')
        else:
            list_video = [v for v in self.videos]
            for video in list_video:
                if title_video == video.title:
                    if self.current_user.get_age() < 18 and video.adult_mode == True:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        print(f'View video {title_video}')
                        sec = 0
                        while video.duration > sec:
                            time.sleep(1)
                            sec += 1
                            video.time_now = sec
                            print(video.time_now, sep='/')
                        video.time_now = 0
                        print('Конец видео')

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
