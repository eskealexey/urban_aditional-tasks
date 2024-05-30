import math


class Figure:
    sides_count = 0

    def __init__(self, color: list, *args, filled=True):
        self.__color = color
        self.set_sides(*args)
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if (0 <= r <= 255) and (0 <= g <= 255) and (0 <= b <= 255):
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def set_sides(self, *args):
        if self._is_valid_sides(args):
            if isinstance(self, Cube):
                self.__sides = [args[0] for _ in range(self.sides_count)]
            else:
               self.__sides = list(args)
        else:
            # self.__sides = [1 for _ in range(self.sides_count)]
            if self.__sides == None:
                self.__sides = [1 for _ in range(self.sides_count)]


    def get_sides(self):
        return self.__sides

    def _is_valid_sides(self, args):
        # c = 0
        if isinstance(self, (Circle, Cube)):
            c = 1
        else:
            c = self.sides_count
        for x in args:
            if (x > 0) and (len(args) == c):
                return True
            else:
                return False

    def __len__(self):
        s = self.get_sides()
        self.perimetr = 0
        for side in s:
            self.perimetr += side
        return self.perimetr


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: list, *args):
        super().__init__(color, *args)

    def get_radius(self):
        side = self.get_sides()
        return side[0] / (2 * 3.14)

    def get_square(self):
        r = self.get_radius()
        return 3.14 * r ** 2

    def __str__(self):
        return len(self)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color: list,  *args):
        super().__init__(color, *args)
        if not self.check_validate():
            raise 'С данными сторонами построить треугольник нельзя'

    def get_height(self):
        p = len(self) / 2
        lst_ = self.get_sides()
        __height = 2 * (math.sqrt(p * (p - lst_[0]) * (p - lst_[1]) * (p - lst_[2]))) / lst_[0]
        return __height

    def check_validate(self):
        list_ = sorted(self.get_sides(self.get_sides()))
        if list_[0] + list_[1] > list_[2]:
            return True
        else:
            return False

    def set_sides(self, *args):
        super().set_sides(*args)
        # super()._is_valid_sides(args)
        if not self.check_validate():
            raise 'С данными сторонами построить треугольник нельзя'

    def get_square(self):
        h = self.get_height()
        lst_ = self.get_sides()
        return h * lst_[0] / 2


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: list, *args):
        super().__init__(color, *args)
        # self.set_sides = [args[0] for _ in range(12)]

    # def set_sides(self, *args):
    #     super().set_sides(*args)
    #     super()._is_valid_sides(args)


    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222,35,130), 6)

circle1.set_color(55, 66, 77)
cube1.set_color(300, 70, 15)
print(circle1.get_color())
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
circle1.set_sides(15)
print(cube1.get_sides())
print(circle1.get_sides())

print(len(circle1))
print(cube1.get_volume())

# trio = Triangle((10, 10, 10), 2, 5, 4)
# print(trio.get_sides())
# trio.set_sides(1, 2, 6)
# print(trio.get_sides())