'''Первое Д/З'''


class Figure:
    unit = 'sm'

    def __init__(self):
        self.__peremetr = 0

    @property
    def peremetr(self):
        return self.__peremetr

    @peremetr.setter
    def peremetr(self, value):
        self.__peremetr = value

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def info(self):
        pass


class Square(Figure):
    def __init__(self, side_length):
        super(Square, self).__init__()
        self.__side_length = side_length
        self.__peremetr = self.calculate_perimeter()  # 10

    def calculate_perimeter(self):
        return 4 * self.__side_length

    def calculate_area(self):
        return self.__side_length ** 2

    def info(self):
        return f'Square side length: {self.__side_length} {Figure.unit}, ' \
               f'perimeter: {self.__peremetr} {Figure.unit}, ' \
               f'area: {self.calculate_area()} {Figure.unit}.'


class Rectangle(Figure):
    def __init__(self, length, width):
        super(Rectangle, self).__init__()
        self.__width = width
        self.__length = length
        self.__peremetr = self.calculate_perimeter()

    def calculate_perimeter(self):
        return 2 * (self.__length + self.__width)

    def calculate_area(self):
        return self.__width * self.__length

    def info(self):
        return f'Rectangle length: {self.__length} {Figure.unit}, ' \
               f'width: {self.__width} {Figure.unit}, ' \
               f'perimeter: {self.__peremetr} {Figure.unit}, ' \
               f'area: {self.calculate_area()} {Figure.unit}'


figure_list = [Square(3), Square(9), Rectangle(12, 5), Rectangle(6, 7), Rectangle(2, 4)]

for i in figure_list:
    print(i.info())

'''Второе Д/З'''


class Figures:
    unit = 'mm'

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass


class Circle(Figures):
    pi = 'π'

    def __init__(self, radius):
        super(Circle, self).__init__()
        self.__radius = radius

    def calculate_area(self):
        return self.__radius ** 2  # and *  3.14

    def info(self):
        return f'Circle radius: {self.__radius} {Figures.unit}, ' \
               f'area: {self.calculate_area()}{Circle.pi} {Figures.unit}'


class RightTriangle(Figures):
    def __init__(self, side_a, side_b):
        super(RightTriangle, self).__init__()
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return round((self.__side_a * self.__side_b) / 2, 1)

    def info(self):
        return f'RightTriangle side a: {self.__side_a}{Figures.unit}, ' \
               f'side b: {self.__side_b}{Figures.unit}, ' \
               f'area: {self.calculate_area()}{Figures.unit}'


figure2_list = [Circle(4), Circle(6), RightTriangle(2, 4), RightTriangle(6, 7), RightTriangle(5, 7)]

for j in figure2_list:
    print(j.info())