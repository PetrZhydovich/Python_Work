"""Пользователь вводит строку из четырёх или более целых чисел,
 разделённых символом “/”. \
Сформируйте словарь, где:
второе и третье число являются ключами
первое число является значением для первого ключа
четвертое и все возможные последующие числа хранятся
 в кортеже как значения второго ключа
"""

# def slash (s: str) -> dict[int, int]:
#     one, two, three, *other = s.split('/')
#     result ={int(two):int(one), int(three):tuple(map(int, other))}
#     return result
    
# print(slash(input("Enter srting: ")))



"""Самостоятельно сохраните в переменной строку текста.
Создайте из строки словарь, где ключ - буква, а значение - код буквы.
Напишите преобразование в одну строку.
"""


# string_user = "текст состоящий из слов!"
# res_dict = {key: ord(key) for key in string_user}

# print(res_dict)
# print(res)




"""Продолжаем развивать задачу 2.
Возьмите словарь, который вы получили. 
Сохраните его итераторатор.
Далее выведите первые 5 пар ключ-значение, 
обращаясь к итератору, а не к словарю.
"""


# string_user = "Текст состоящий из слов!"
# res_dict = {key: ord(key) for key in string_user}
# my_iter = iter(res_dict.items())

# for i in range(5):
#     print(*next(my_iter))



# Создайте генератор чётных чисел от нуля до 100.
# Из последовательности исключите числа, сумма цифр которых равна 8.
# Решение в одну строку.


# gen_chet = (i for i in range(0, 101, 2) if 8 != (i // 10) + (i % 10) != 8)
# print(*gen_chet)



"""Напишите программу, которая выводит на экран числа от 1 до 100.
При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»
Вместо чисел, кратных пяти — слово «Buzz».
Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz»
*Превратите решение в генераторное выражение.
"""

# my_list = []
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         my_list.append("FizzBuzz")
#     elif i % 3 == 0:
#         my_list.append("Fizz")
#     elif i % 5 == 0:
#         my_list.append("Buzz")
#     else:
#         my_list.append(i)

# print(my_list)

# my_list = ("FizzBuzz" if (i % 3 == 0 and i % 5 == 0) else "Fizz" if (i % 3 == 0) else "Buzz" if (i % 5 == 0) else i for i in range(1, 101))

# print(*my_list)



"""Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
Таблицу создайте в виде однострочного генератора, где каждый элемент генератора - 
отдельный пример таблицы умножения.
Для вывода результата используйте “принт” без перехода на новую строку.
"""

# tab_list = print(*(f'{i: > 2} * {j: > 2} = {i * j: > 2}' for i in range(2, 10) for j in range(2, 11)), end= '')





"""Создайте функцию-генератор.
Функция генерирует N простых чисел, начиная с числа 2.
Для проверки числа на простоту используйте правило:
 “число является простым, если делится нацело только на единицу и на себя”.
 """


# def gen_num(num: int) -> int:

#     for i in range(2, num):
#         for j in range(2, i):
#             if i % j ==0:
#                 break
#         else:
#             yield i

# print(*gen_num(int(input("Enter your number: "))))
