# def func(text: str) -> list[int]:
#     result = set()

#     for char in text:
#         result.add(ord(char))
#     result = sorted(result, reverse=True)
#     return result


# print(func('Напишите функцию, которая принимает строку текста'))




# Функция получает на вход строку из двух чисел через пробел. 
# Сформируйте словарь, где ключом будет символ из Unicode, 
# а значением - целое число. 
# Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел
#  до наибольшего включительно


# def two_num (n: str) -> dict[str, int]:
#     one, two = map(int, n.split())
#     result = {}

#     for i in range(min(one, two), max(one, two)+1):
#         result[chr(i)] = i
#     return result

# print(two_num('50 100'))




# Функция получает на вход список чисел. 
# Отсортируйте его элементы in place без использования встроенных
#  в язык сортировок. 
# Как вариант напишите сортировку пузырьком. 
# Её описание есть в википедии.



# def buble(a: list) -> None:
#     n = 1

#     while n < len(a):
#         for i in range(len(a)-n):
#             if a[i] > a [i+1]:
#                 a[i], a[i+1] = a[i+1], a[i]
#         n +=1

# list1 = list((10, 363, 3, 576, 6, 43))
# buble(list1)
# print(buble)




# Функция принимает на вход три списка одинаковой длины:
# имена str, 
# ставка int, 
# премия str с указанием процентов вида “10.25%”.
# Вернуть словарь с именем в качестве 
# ключа и суммой премии в качестве значения. 
# Сумма рассчитывается как ставка умноженная на процент премии



def awards(names: list[str], level: list[int], bonus: list[str]) -> dict[str, float]:
    
    result = {}
    
    for n, l, b in zip(names, level, bonus):
        result[n] = (l * float(b[:-1])) / 100
    return result

n1 = ['Ivan', 'Alex', 'Maria']
l1 = [15000, 18000, 19000]
b1 = ['10.25%', '11.80%', '9.00%']

print(awards(n1, l1, b1))

