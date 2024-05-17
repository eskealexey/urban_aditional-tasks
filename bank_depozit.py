# Пользователь делает вклад в размере a рублей сроком на years лет под x% годовых
# (каждый год размер его вклада увеличивается на x%. Эти деньги прибавляются к сумме вклада,
# и на них в следующем году тоже будут проценты).
# Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.

class Depozit:
    def __init__(self, srok_, procent_, vklad_):
        self.__srok = srok_
        self.__procent = procent_ / 100
        self.__vklad = vklad_

    def calc(self):
        vklad_ = self.__vklad
        for i in range(self.__srok):
            sum_proc = vklad_ * self.__procent
            vklad_ += sum_proc
        return vklad_

    def __str__(self):
        return ('Вклад - {:.2f}, срок - {:d}, процент - {:.2%} | Итог - {:.2f} '
                .format(self.__vklad, self.__srok, self.__procent, self.calc()))


vklad = float(input('Введите первоначальную сумму - '))
procent = float(input('Введите % - '))
srok = int(input('Введите срок вклада - '))
depozit = Depozit(srok, procent, vklad)
print(depozit)
