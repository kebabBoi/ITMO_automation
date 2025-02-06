# a: int = 5
# b: str = 'stroka'
# c: list = [1,2,3]
#
# def indent(s: str, width: int) -> str:
#     return " "*(max(0, width - len(s))) + s
#
# print(indent('15', 15))

# #zadacha1
# def dlina_stroki(s: str = ''):
#     return len(s)
# s = 'asdas124as'
# print(dlina_stroki(s))
#
# #zadacha 2
# def max_list(a: list,b: list) -> int:
#     return max(len(a), len(b))
#
# a = [1, 2, 4, 5, 7, 8]
# b = ['dddddddddddd', 'fffffffffff']
#
# print(max_list(a = [1, 2, 4, 5, 7, 8], b = ['dddddddddddd', 'fffffffffff', 'dddddddddddd', 'fffffffffff', 'dddddddddddd', 'fffffffffff', 'dddddddddddd', 'fffffffffff']))

#zadacha 3
# def addition(a: list) -> list:
#     return a
# e : list = [5]
# print(addition(a = ['jfjfjfj', 4, '1212'])+e)

#zadacha 4
def summa(a: list) -> int:
    return sum(a)

print(summa(a = [1,4,6,67,2,5,6,6.4]))

