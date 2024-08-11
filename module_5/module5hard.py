from time import sleep as sl
class User:
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = password
        self.age = age

    def __hash__(self):
        return hash(self.password)

    def __repr__(self):
        return self.nickname


# user_1 = User('Nazim', '123', 50)
# print(f'Имя пользователя: {user_1.nickname}, хеш пароля: {hash(user_1.password)}, Возраст: {user_1.age} лет')
# print(hash(user_1.password))
# print(hash(user_1.nickname))

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __repr__(self):
        #return f"{self.title}"
        return f"{self.title}, {self.duration}, {self.adult_mode}"

# v1 = Video('Лучший язык программирования 2024 года', 200)
# v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# v3 = Video('Тестовое видео', 15)
# print(f"Имя файла: {v2.title} Длительность: {v2.duration} Возрастные ограничения: {v2.adult_mode}")
# print(f"Имя файла: {v3.title} Длительность: {v3.duration} Возрастные ограничения: {v3.adult_mode}")
# print(v1, v2, v3)

class UrTube:
    def __init__(self):
        self.users = []
        self.nickname = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        hash_password = hash
        for user in self.users:
            if user.nickname == nickname and user.password == hash_password:
                self.current_user = user
                return
        print("Неверный логин или пароль")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not any(i.title == video.title for i in self.videos):
                self.videos.append(video)

    def get_videos(self, word):
        word = word.lower()
        return [video.title for video in self.videos if word in video.title.lower()]

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                for i in range(video.time_now + 1, video.duration + 1):
                    print(i, end=" ")
                    sl(1)
                print("Конец видео")
                video.time_now = 7 # установка начала видео после просмотра
                return

        print("Видео не найдено")

# Код для проверки
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Видео для тестов', 3, adult_mode=True)

# Добавление видео
ur.add(v1, v2, v3)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
print(ur.get_videos('тест'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)

# test
# ur.register('nazim', '123', 11)
# ur.log_out()
# print(ur.current_user)
# input(ur.log_in("name", "password"))
# print(ur.current_user)

ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# test
# ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')




