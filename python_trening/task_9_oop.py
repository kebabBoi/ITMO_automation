class Button:

    type: str = 'Кнопка'

    def __init__(self, text, link):
        self.text = text
        self.link = link

#Создание экземпляров класса
home = Button('Домой', '/home')
catalog_msk = Button ('Каталог', '/msk/catalog')

#Получение доступа к атрибутам
print(home.text)
print('Кнопка ' + home.text + ' имеет ссылку ' + home.link)

print('\n')

print(catalog_msk.text)
print('Кнопка ' + catalog_msk.text + ' имеет ссылку ' + catalog_msk.link)

print('\n')

class ButtonTwo:
    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc

    def click(self):
        return "Клик по локатору - {}".format(self.loc)


# Создание экземпляров класса
home_two = ButtonTwo('Домой', '/home', 'button#home')

print(home_two.click())

class Input:
    def __init__(self, loc):
        self.loc = loc

search = Input('input#search')

print(search.loc)