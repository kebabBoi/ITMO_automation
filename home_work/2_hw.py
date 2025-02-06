# #variant 1_1
# ef task_1(a: int, b: float, c: str, d: list, e: bool):
#     return type(a), type(b), type(c), type(d), type(e)
#
# a = 123
# b = 12.12
# c = 'string'
# d = [1,1]
# e = False
#
# print(task_1(a, b, c, d, e))

#variant 2_1
def task_1() -> tuple:
    a: int = 123
    b: float = 12.12
    c: str = 'string'
    d: list = [1,1]
    e: bool = True
    return type(a), type(b), type(c), type(d), type(e)
print('\n' + 'Задание 1:')
print(task_1())

def task_2() -> list:
    a = [1, 2, 3, 5, 8, 13, 21] #это ряд Фибоначчи, но начинается не с 0
    return (type(a),a[0:3])
print('\n' + 'Задание 2:')
print(task_2())

def task_3(n: int) -> int:
    return n**2
print('\n' + 'Задание 3:')
print(task_3(674))