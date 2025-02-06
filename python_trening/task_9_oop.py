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

class Input:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

class Button:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

class Title:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

class Link:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text


search = Input('input#search','Поиск')
print(search.loc + ' ' + search.text)

next = Button('button#next', 'Далее')
print(next.loc + ' ' + next.text)

logo = Title('title#logo', 'Заголовок')
print(logo.loc + ' ' + logo.text)

hyper = Link('link#hyper', 'Ссылка')
print(hyper.loc + ' ' + hyper.text)