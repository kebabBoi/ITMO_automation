# # num_float = 3.4
# # num_float = 0
# num_float = -123.4
#
# if num_float > 0:
#     print('polozhitelnoe')
# elif num_float == 0:
#     print('Noll')
# else:
#     print('otrizzatilnoe')

# permit_print = False
# num = 2
# if num > 0 and permit_print:
#     print('num +')
# elif not permit_print:
#     print('Pechat zapreshena')

def vashe_zvanie(k):
    if k >= 1 and k <= 4:
        print('bachalor')
    elif k >= 5 and k <= 6:
        print('magistr')
    elif k >= 7 and k <= 9:
        print('aspirant')
    else:
        print('Введите коррекктный год обучения')
vashe_zvanie(10)

# #решение из курса
# def student_rank(year):
#     if year == 1 or year == 2 or year == 3 or year == 4:
#         print('vy - bakalavr')
#     elif year in range(5, 7):
#         print('vy - magistr')
#     elif 7 <= year <= 9:
#         print('vy - aspirant')
#     else:
#         print('vvedite korrektnyi god')
# student_rank(1)

def sto(x):
    if x >= 100 :
        print("-")
    elif x <= -100:
        print("-")
    else:
        print("+")
sto(-1000)