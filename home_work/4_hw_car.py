#задание 4
class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print("Автомобиль заведен")

    def stop(self):
        print("Автомобиль зашлушен")

    def car_year(self, year):
        print(f'Машинка {self.year} года выпуска')

    def car_type(self, type):
        print(f'Машинка вида: {self.type}')

    def car_color(self, color):
        print(f'Цвет машинки: {self.color}')

car = Car ('Черный', 'Хэчбэк', '1992')
car.car_year(1)
car.start()
car.car_color(1)
car.car_type(1)
car.stop()