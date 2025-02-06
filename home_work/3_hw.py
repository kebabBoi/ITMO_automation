#задание 1
def task_1(num_a, num_b):
    if num_a > num_b:
        print(num_a)
    elif num_a < num_b:
        print(num_b)
    else:
        print('Числа равны')

task_1(555.3, 555.4)


def task_2(num_c, num_d):
    if num_c - num_d == 135 or num_d - num_c == 135:
        print('yes')
    else:
        print('no')

task_2(135, 1)


def task_3(num_month):
    # variant 1
    # if num_month == 1 or num_month == 2 or num_month == 12:
    #     print('Это зима')
    # elif num_month == 3 or num_month == 4 or num_month == 5:
    #     print('Это весна')
    # elif num_month == 6 or num_month == 7 or num_month == 8:
    #     print("Это лето")
    # elif num_month == 9 or num_month == 10 or num_month == 11:
    #     print('Это осень')
    # else:
    #     print('Введите номер месяца')
    #variant 2
    if 1 <= num_month <= 2 or num_month == 12:
        print('Это зима')
    elif num_month in range (3, 6):
        print('Это весна')
    elif 6 <= num_month <= 8:
        print("Это лето")
    elif 9 <= num_month <=11:
        print('Это осень')
    else:
        print('Введите номер месяца')
task_3(5)


def task_4(num_d, num_e, num_f):
    if num_d > 10 and num_e > 10 and num_f > 10:
        print('YESSSSSSSSS')
    else:
        print('NO :(')
task_4(1, 12, 100)


def task_5(list_a: list):
    poz = 0
    for num in list_a:
        if num > 0:
            poz += 1
    print(poz)
task_5(list_a=[-1, 1, -1, 1, -1])

def task_6(year: int, month: int):
    if year == 0:
        days = month * 29
    elif month == 12:
        days = (year + 1) * 12 * 29
    else:
        days = year * 12 * 29 + month * 29

    return days

print(task_6(1, 12))