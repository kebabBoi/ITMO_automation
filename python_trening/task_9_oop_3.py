class Soda():
    def __init__(self, add = None):
        self.add = add

    def show_my_drink(self, drink):
        if self.add:
            print(f'Soda with  {self.add}') #тут используется f строк и параметр передается в {}, типа как format.(self)
        else:
            print('Typical soda')


drink1 = Soda('lemon')
drink2 = Soda()
drink1.show_my_drink(())
drink2.show_my_drink(())