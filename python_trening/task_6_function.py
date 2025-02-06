# def add(x, y):
#     return x+y
#
# print(add(4, 56))
#
# print(add('kto', 'nikto'))
#
# def arg(a, b, c=4, d=5):
#     return a+b+c+d
#
# print(arg(1,1,1,1))
# print(arg(10, 10))
# print(arg(1,1,1))
# print(arg(0.4, 1))
#
#
# def range_arg(a, b, c, d):
#     return a+' '+b+' '+c+' '+d
#
# print(range_arg('1',d='2',c='3',b='4'))

#zadacha 1
def first_elem(a):
    return a

a = (1, 2, 3, 4)

print(first_elem(a[0]))
#pravilnoe reshenie 1
# def first_elema(a=(1,2,3,4)):
#     return a[1]
#
# print(first_elema())

#zadacha 2
def s_kruga(r, pi):
    return pi*r**2

r = 2
pi = 3.14159

print(s_kruga(r,pi))

#pravilnoe reshenie 2
# def compute_surface(radius, pi=3.14159):
#     return pi*radius*radius
#
# print(compute_surface(3))