# Вручную создайте список с целыми числами, которые повторяются.
#  Получите новый список, который содержит уникальные 
# (без повтора) элементы исходного списка. 
# # *Подготовьте два решения, короткое и длинное, 
# которое не использует другие коллекции помимо списков.







list1 = [1, 2, 3, 5, 2, 2, 1, 13, 4, 2]
list2 = []

for item in list1:
    if item not in list2:
      list2.append(item)  

print(list2)

list3 = list(set(list1))
print(list3)



# Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
# целое положительное число
# вещественное положительное или отрицательное число
# строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
# строку в верхнем регистре в остальных случаях


# data = input("insert your data: ")
# if data.isdecimal():
#     a1 = int(data)

# elif data.replace('.', '').replace('-', '').isdecimal():
#     a1 = float(data)

# elif not data.islower():
#     a1 = data.lower()

# else:
#     a1 = data.upper()

# print(f"{a1 = } {type(a1)}")





# Создайте вручную кортеж содержащий элементы разных типов. 
# Получите из него словарь списков, где 
# ключ - тип элемента,
# значение - список элементов данного типа.



# my_tuple = (1, "werwer", True, 1.23, 345345, "werwer", 12, False)
# my_dict = {}

# for item in my_tuple:
#     # if type(item) in my_dict.keys():
#     #     my_dict[type(item)] = item
#     key = my_dict.setdefault(type(item), list())
#     key.append(item)

# print(my_dict)




# Создайте вручную список с повторяющимися элементами.
# Удалите из него все элементы, которые встречаются дважды.


# list = [1, 5, 7, 2, 3, 4, 5, 3, 5, 7]

# for item in list:
#     if list.count(item) > 1:
#         for i in range(list.count(item)):
#             list.remove(item)

# print(list)


# Создайте вручную список с повторяющимися целыми числами. 
# Сформируйте список с порядковыми номерами нечётных элементов исходного списка. 
# Нумерация начинается с единицы.



list = [1, 5, 7, 2, 3, 4, 5, 3, 5, 7]
list2 = []

for i, item in enumerate(list, start=1):
    if item % 2 != 0:
        list2.append(i)

print(list2)



# Пользователь вводит строку текста. 
# Вывести каждое слово с новой строки.
# Строки нумеруются начиная с единицы
# Слова выводятся отсортированными согласно кодировки Unicode
# Текст выравнивается по правому краю так,
#  чтобы у самого длинного слова был один пробел между ним и номером строки


str_1 = input().split()

str_1.sort()
temp = 0

for item in str_1:
    if len(item) > temp:
        temp = len(item)

for i, k in enumerate(str_1, start=1):
    print(f"{i} {k:>{temp}}")

