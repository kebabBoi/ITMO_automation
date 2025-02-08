#задание 1
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self. width = width

    def calc_area (self, area):
        self.area = area
        return self.length * self.width

    def calc_perimeter (self, perimeter):
        self.perimeter = perimeter
        return 2 * (self.length + self.width)

a = Rectangle(18483, 12313.4)
print('Площадb прямоугольника равна')
print(a.calc_area(1))
print('Периметр прямоугольника равен')
print(a.calc_perimeter(1))
print('\n')

#задание 2
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        result = self.a + self.b
        print(f'Сложение a на b: {result}')

    def multiplication(self, ):
        result = self.a * self.b
        print(f'Умножение a на b: {result}')

    def devision(self):
        if self.b != 0:
            result = self.a / self.b
            print(f'деление a на b: {result}')
        else:
            print('На ноль делить нельзя')

    def substruction(self):
        result = self.a - self.b
        print(f'Вычитание b из а: {result}')

calc = Math(100, 0)
calc.addition()
calc.multiplication()
calc.devision()
calc.substruction()
print('\n')

#задание 3
class Site:

    def __init__(self, text, loc = ''):
        self.text = text
        self.type = 'Кнопка'
        self.loc = loc

    def click (self):
        return 'Клик по кнопке - {}'. format(self.text)

but1 = Site('Text Box')
print(but1.type, but1.text)
print(but1.click())

but2 = Site('Check Box')
print(but2.type, but2.text)
print(but2.click())

but3 = Site('Radio Button')
print(but3.type, but3.text)
print(but3.click())

but4 = Site('Web Tables')
print(but4.type, but4.text)
print(but4.click())

but5 = Site('Buttons')
print(but5.type, but5.text)
print(but5.click())

but6 = Site('Links')
print(but6.type, but6.text)
print(but6.click())

but7 = Site('Broken Links - Images')
print(but7.type, but7.text)
print(but7.click())

but8 = Site('Upload and Download')
print(but8.type, but8.text)
print(but8.click())

but9 = Site('Dynamic Properties')
print(but9.type, but9.text)
print(but9.click())