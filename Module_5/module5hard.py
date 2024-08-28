class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age

class Video:
    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode