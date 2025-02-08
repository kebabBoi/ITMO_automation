# class Button:
#
#     type: str = 'Кнопка'
#
#     def __init__(self, text, link):
#         self.text = text
#         self.link = link
#
# #Создание экземпляров класса
# home = Button('Домой', '/home')
# catalog_msk = Button ('Каталог', '/msk/catalog')
#
# #Получение доступа к атрибутам
# print(home.text)
# print('Кнопка ' + home.text + ' имеет ссылку ' + home.link)
#
# print('\n')
#
# print(catalog_msk.text)
# print('Кнопка ' + catalog_msk.text + ' имеет ссылку ' + catalog_msk.link)
#
# print('\n')
#
# class ButtonTwo:
#     def __init__(self, text, link, loc):
#         self.text = text
#         self.link = link
#         self.loc = loc
#
#     def click(self):
#         return "Клик по локатору - {}".format(self.loc)
#
#
# # Создание экземпляров класса
# home_two = ButtonTwo('Домой', '/home', 'button#home')
#
# print(home_two.click())

from task_9_checks import Checks

class Input(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text

class Button(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text

class Title(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text

class Link(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text


search = Input('input#search','Поиск')
print(search.loc + ' ' + search.text)
print(search.check_text(1))

next = Button('button#next', 'Далее')
print(next.loc + ' ' + next.text)
print(next.check_text(1))

logo = Title('title#logo', 'Заголовок')
print(logo.loc + ' ' + logo.text)
print(logo.check_text(1))

hyper = Link('link#hyper', 'Ссылка')
print(hyper.loc + ' ' + hyper.text)
print(hyper.check_text(1))