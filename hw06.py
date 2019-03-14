import math

#HW06_EASY

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
# фунция для определения длинны линии
        def line(top1, top2):
            return math.sqrt((top1[0]-top2[0])**2 + (top1[1]-top2[1])**2)
#определяем длинны гранией треугольника
        self.ab = line(self.a, self.b)
        self.bc = line(self.b, self.c)
        self.ca = line(self.c, self.a)
# определение площади треугольника
    def triangle_s(self):
        p = (self.ab + self.bc + self.ca)/2
        return math.sqrt(p*(p-self.ab)*(p-self.bc)*(p-self.ca))
# определение высоты треугольника

     def triangle_h(self):
        return self.triangle_s()*2/self.ca
# определяем периметр
    def triangle_p(self):
        return self.ab + self.bc + self.ca

 # Ввоодим координаты
trin = Triangle((25, 15), (18, 22), (32, 56))
print(f'Площадь треугольника равна {round(trin.triangle_s())}')
print(f'Высота треугольника равна {round(trin.triangle_h())}')
print(f'Периметр треугольника равен {round(trin.triangle_p())}')


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
# фунция для определения длинны линии
        def line(top1, top2):
            return math.sqrt((top1[0] - top2[0]) ** 2 + (top1[1] - top2[1]) ** 2)

 # определяем диагонали для проверки на равнобедренную тропецию
        self.ac = line(self.a, self.c)
        self.bd = line(self.b, self.d)
# определяем длинну гранией
        self.ab = line(self.a, self.b)
        self.bc = line(self.b, self.c)
        self.cd = line(self.c, self.d)
        self.da = line(self.d, self.a)
# расчет высоты трапеции
        self.h = math.sqrt(self.ab**2 - ((self.da-self.bc)**2/4))
# расчет площади чере высоту
        self.s = (self.h*(self.da-self.bc))/2
# проверка - является ли это равнобедренной трапецией
    def check(self):
        if self.ac != self.bd:
            return 'Это не равнобедренная тропеция'
        else:
            return True
# определяем грани
    def face(self):
        return (f'Грань AB = {round(self.ab)}, грань BC = {round(self.bc)}, '
                f'грань CD = {round(self.cd)}, грань DA = {round(self.da)}')

     def p(self):
        return self.ab + self.bc + self.cd +self.da


 trap = Trapeze((25, 15), (18, 22), (32, 22), (45, 15))
if trap.check() == True:
    print(trap.face())
    print(f'Периметр трапеции равен: {(round(trap.p()))}')
    print(f'Площадь трапеции равна {round(trap.s)}')
else:
    print('Это не равнобедренная тропеция')

#HW06_NORMAL
# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class People:
    def __init__(self, name, patronymic, surname):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

     def get_full_name(self):
        return self.name + ' ' + self.patronymic + ' ' + self.surname

     def get_short_name(self):
        return '{} {}.{}.'.format(self.surname.title(), self.name[0].upper(), self.patronymic[0].upper())

class Student(People):
    def __init__(self, name, patronymic, surname, mom, dad, school_class):
        People.__init__(self, name, patronymic, surname)
        self.mom = mom
        self.dad = dad
        self.school_class = school_class

class Teacher(People):
    def __init__(self, name, patronymic, surname, subject):
        People.__init__(self, name, patronymic, surname)
        self.subject = subject

class Class_rooms:
    def __init__(self, class_room, teachers):
        self.class_room = class_room
        self.teachersdict = {t.subject: t for t in teachers}


 if __name__ == '__main__':  # Тестирование.
    teachers = [Teacher('Иван', 'Иванович', 'Иванов', 'Математика'),
                Teacher('Сергей', 'Сергеевич', 'Сергеев', 'Русский язык'),
                Teacher('Петр', 'Петрович', 'Петров', 'Физика'),
                Teacher('Дмитрий', 'Дмитриевич', 'Дмитриев', 'История'),
                Teacher('Алексей', 'Алексеевич', 'Алексеев', 'Литература')]
    classes = [Class_rooms('11 А', [teachers[0], teachers[1], teachers[2]]),
               Class_rooms('11 Б', [teachers[1], teachers[3], teachers[4]]),
               Class_rooms('10 А', [teachers[3], teachers[1], teachers[0]])]
    parents = [People('Михаил', 'Михаидлвич', 'Михаилов'),
               People('Мария', 'Мариеевна', 'Мариева'),
               People('Люк', 'Энакинович', 'Скайуокер'),
               People('Виктория', 'Виториевна', 'Викториева'),
               People('Владимир', 'Владимирович', 'Владимиров'),
               People('Павел', 'Александрович', 'Дюжев')]
    students = [Student('Вячеслав', 'Вячеславович', 'Вячеславов', parents[0], parents[1], classes[0]),
                Student('Ольга', 'Петровна', 'Рюриковна', parents[2], parents[3], classes[1]),
                Student('Анна', 'Дмитриевна', 'Андреева', parents[4], parents[5], classes[2])]
    print('Список классов в школе: ')
    for f in classes:
        print(f.class_room)

     for f in classes:
        print('Учителя, преподающие в {} классе:'.format(f.class_room))
        for teacher in classes[0].teachersdict.values():
            print(teacher.get_full_name())
    for f in classes:
        print("Ученики в классе {}:".format(f.class_room))
        for st in students:
            print(st.get_short_name())

    # for f in students:
    #     print('Список предметов ученика {}'.format(f.school_class))
    #     for teacher in classes[0].teachersdict.values():
    #         print(teacher.get_full_name()) 

