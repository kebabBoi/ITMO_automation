class Page:
    def __init__(self, url):
        self.url = url

    def get(self):
        return "Это урл - {}".format(self.url)

home = Page('http://www.vk.com')
print(home.get())

# # Решение с курса
# class Page:
#     def __init__(self, url):
#         self.url = url
#
#     def get(self):
#         print(self.url)
#
# home = Page('http://www.vk.com')
# home.get()