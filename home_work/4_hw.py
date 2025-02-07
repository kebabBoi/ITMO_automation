#задание 1
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self. width = width

    def calc_square (self, square):
        self.square = square
        return self.length * self.width

    def calc_perimeter (self, perimeter):
        self.perimeter = perimeter
        return self.length + self.width

a = Rectangle(18483, 12313.4)
print('Площадb прямоугольника равна')
print(a.calc_square(1))
print('Периметр прямоугольника равен')
print(a.calc_perimeter(1))
print('\n')

#задание 2
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self, addition):
        self.addition = addition
        return self.a + self.b

    def multiplication(self, multiplication):
        self.multiplication = multiplication
        return self.a * self.b

    def devision(self, devision):
        self.devision = devision
        return self.a / self.b

    def substruction(self, substraction):
        self.substruction = substraction
        return self.a - self.b

calc = Math(100, 10)

print('Сложение a на b')
print(calc.addition(1))
print('Умножение a на b')
print(calc.multiplication(1))
print('деление a на b')
print(calc.devision(1))
print('Вычитание b из а')
print(calc.substruction(1))
print('\n')

#задание 3
