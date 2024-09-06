class Horse:
    def __init__(self):
        self.x_distance = 0  # пройденный путь
        self.sound = 'Frrr'  # звук, который издаёт лошадь

    def run(self,dx):
        self.x_distance += dx

class Eagle:
    def __init__(self):
        self.y_distance = 0  #высота полёта
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()
        Eagle.__init__(self)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)

p1 = Pegasus()

print(p1.get_pos())
p1.move(20, 44)
print(p1.get_pos())
p1.move(-10, 11)
print(p1.get_pos())

p1.voice()



