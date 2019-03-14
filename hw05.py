import os
import sys
import shutil

# HW05_Easy

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def instruction():
    print("[1] - Создать заданное кол-во папок в текущей дериктории")
    print("[2] - Удалить заданное кол-во папок в текущей директории")


def create_dir(number_dir):
    for i in range(1, number_dir + 1):
        dir_path = os.path.join(os.getcwd(), "Новая папка" + str(i))
        try:
            os.mkdir(dir_path)
            print("Папка создана")
        except FileExistsError:
            print("Такая папка уже существует")

def delete_dir(number_dir):
    for i in range(1, number_dir + 1):
        dir_path = os.path.join(os.getcwd(), "Новая папка" + str(i))
        try:
            os.rmdir(dir_path)
            print("Папка удалена")
        except FileNotfoundError:
            print("Такой папки не существет")

instruction()
answer = input("Выберите нужное действие: ")

if answer == "1":
    number = int(input("Выберите  сколько папок нужно создать: "))
    create_dir(number)


elif answer == "2":
    number=int(input("Выберите сколько папок нужно удалить: "))
    delete_dir(number)

else:
    print("Неизвестное действие")

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def instruction():
    print("[1] - Отобразить папки в текущей лиректории")

files = os.listdir()
dir_list = []

for el in range(0, len(files)):
    file_path = os.path.join(os.getcwd(), files[el])
    dir_cheсk = os.path.isdir(file_path)
    if dir_check:
        dir_list.append(files[el])

if len(dir_list) > 0:
    print(f"\nСписок папок в текущей директории:\n{dir_list}")
else:
    print("\nВ данной директории нет папок")                        


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

file_name = os.path.basename(sys.argv[0])
dupl_file = file_name[:-3] + ".dupl.py"
shutil.copy(file_name, dupl_file)

print("\nФайл успешно скопирован")

# HW05_Normal

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

def instruction():
    print("[1] - Перейти в папку")
    print("[2] - Просмотреть содержимое текущей папки")
    print("[3] - Удалить папку")
    print("[4] - Создать папку")
    print("[5] - Покинуть программу")

def path():
    current_path = os.getcwd()
    return current_path

def goto_dir(current_path, dir_name)
    new_path = os.path.join(current_path, dir_name)
    os.chdir(new_path)

def dir_content():
    content = os.listdir()
    if len(content > 0:
        print(f"Список файлов в текущей папке:\n{content}")
    else:
        print("\nДанная папка пуста")

def create_dir(current_path, dir_name):
    new_dir = os.path.join(current_path, dir_name)
    os.mkdir(new_dir)

def delete_dir(current_path, dir_name):
    dir_to_delete = os.path.join(current_path, dir_name)
    os.rmdir(dir_to_delete)

current_path = path()
while True:
    instruction()

    number = int(input("\nВыбирете нужное действие: "))
    while choice not in range(1, 6):
        number = int(input("\nВыберите действие: "))

    if number == 1:
        name_dir = input("Введите наименование папки: ")
        try:
           goto_dir(current_path, name_dir)
           current_path = path()
        except FileNotFoundError:
           print("\nТакой папки не существует")

    elif number == 2:
        dir_content()

    elif number == 3:
        name_dir = input("Введите имя новой папки: ")
        try:
           create_dir = input("Введите наименование новой папки: ")
           print("Новая папка успешно создана")
        except FileExistsError:
           print("Папка с таким именем уже существует")

    elif number == 4:
        name_dir = input("\nВведите наименование папки: ")
        try:
           delete_dir(current_path, name_dir)
           print("Папка успешно удалена")
        except FileNotFoundError:
           print("Папка с таким именем уже существует")
        except OSError:
           print("Невозможно удалить папку, в ней содержаться данные")

    elif number == 5;
           print("\n\t\t\До свидания")
           break
           

  
        

        
       
