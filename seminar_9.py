# import random

# def deco(func):
#     def wrapper(a: int, count: int):
#         if a < 1 or a > 100:
#             a = random.randint(1,101)
            
#         if count < 1 or count > 10:
#             count = random.randint(1,11)
#         result = func(a, count)
#         return result
#     return wrapper

# @deco
# def ugadai(a: int, count: int) -> None:

#     for i in range(count):
#         num = int(input('Введите число 1 - 100: '))
#         if num > a:
#             print('Число больше')
#         elif num < a:
#             print('Число меньше')
#         else:
#             print('Вы угадали ')
#             break

# ugadai(108, 17)




"""Напишите декоратор, который сохраняет в json файл параметры 
декорируемой функции и результат, который она возвращает. 
При повторном вызове файл должен расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ json словаря.
Для декорирования напишите функцию, которая может принимать как 
позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой функции.
"""

# import json
# from pathlib import Path

# def deco_file(func):
#     file = Path(f'{func.__name__}.json')#Имя файла должно совпадать с именем декорируемой функции
#     if file.is_file():
#         with open(file, 'r', encoding='utf-8') as f:
#             data = json.load(f)
#     else:
#         data =[]
#     def wrapper(*args, **kwargs):
#         new_data = {'args':args, **kwargs}#ключевой параметр сохраните как отдельный ключ json словаря
#         result = func(*args, **kwargs)
#         data.append(new_data)
#         with open(file, 'w', encoding='utf-8') as f:#'w' для json вместо 'a'
#             json.dump(data, f)
#         return result
#     return wrapper


# @deco_file
# def call(*args, **kwargs):
#     pass


# call(31,15,178, x = 18, z = 'a')

""" Создайте декоратор с параметром. 
Параметр - целое число, количество запусков декорируемой функции.
"""




