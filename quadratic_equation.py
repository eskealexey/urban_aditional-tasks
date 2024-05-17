# Квадратные уравнения — это уравнения вида aх2+bx+c=0, где коэффициенты a, b,c — это некоторые числа, причём a ≠ 0.
import math

class Quadric:
    x1, x2 = 0, 0
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def disckrim(self):
        return self.b ** 2 - 4 * self.a * self.c


    def square_root(self):
        if self.disckrim() == 0:
            x1 = -self.b / 2 * self.a
            return x1
        elif self.disckrim() > 0:
            x1 = (-self.b + math.sqrt(self.disckrim()))/ 2 * self.a
            x2 = (-self.b - math.sqrt(self.disckrim())) / 2 * self.a
            self.lst_ = [x1, x2]
            return self.lst_


    def __str__(self):
        if self.disckrim() == 0:
            self.square_root()
            return f'Уравнение имеет один корень X = {self.x1}'
        elif self.disckrim() > 0:
            self.square_root()
            return 'Уравнение имеет два корня X1 = {:.3f} и X2 = {:.3f}'.format(self.lst_[0], self.lst_[1])
        else:
            return 'Корней нет'

print('Квадратные уравнения — это уравнения вида aх2+bx+c=0, где коэффициенты a, b,c — это некоторые числа, причём a ≠ 0.')
a = int(input('Введите a:'))
b = int(input('Введите b:'))
c = int(input('Введите c:'))

quad = Quadric(a, b, c)
print(quad)