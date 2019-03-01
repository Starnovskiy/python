
#Homework03_easy

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    number = number * (10 ** ndigits) + 0.41
    number = number // 1
    return number / (10 ** ndigits)

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):

        str_number = str(ticket_number)

        if sum(map(int, str_number[0:3])) == sum(map(int, str_number[3:])):
                return True
        else:
                return False

#Homework03_normal

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n: int, m: int):
    result = [1, 1]
    position = 2
    if n < 1:
        return None
    if n > m:
        return None
    while position < m:
        result.append(sum([result[-1], result[-2]]))
        position += 1
    return [result[x] for x in range(n-1, m)]



# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    pass
    for i in range(len(origin_list)-1, 0, -1):
        for sort in range(i):
            if origin_list[sort] > origin_list[sort+1]:
                temp = origin_list[sort]
                origin_list[sort] = origin_list[sort + 1]
                origin_list[sort + 1] = temp

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

a = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
sort_to_max(a)
print(a)

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

a = ["", "A", 6, 8, "b", -25, 0, 13, 42, 75, True, False]


def check(x):
    return bool(x)


def filters(func, arg):
    lis_t = [i for i in arg if func(i)]
    return lis_t


b = filters(check, a)
print(b)


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def parallelogram(A, B, C, D):
    A_B = math.sqrt((B["x2"] - A["x1"]) ** 2 + (B["y2"] - A["y1"]) ** 2)
    A_D = math.sqrt((D["x4"] - A["x1"]) ** 2 + (D["y4"] - A["y1"]) ** 2)
    C_D = math.sqrt((D["x4"] - C["x3"]) ** 2 + (D["y4"] - C["y3"]) ** 2)
    B_C = math.sqrt((C["x3"] - B["x2"]) ** 2 + (C["y3"] - B["y2"]) ** 2)
    if A_B == C_D and A_D == B_C:
        return "Да"
    else:
        return "Нет"


A = {"x1": 1, "y1": 3}
B = {"x2": 4, "y2": 7}
C = {"x3": 2, "y3": 8}
D = {"x4": -1, "y4": 4}
print(f"Даны точки {A} {B} {C} {D}, являются ли они вершинами параллелограмма - {parallelogram(A, B, C, D)}")

