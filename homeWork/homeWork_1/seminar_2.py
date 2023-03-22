# a = 7
# b = 5
# txt = "massage"
# c = {1, 2, 3}
# d = True

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(txt))
# print(type(d))



# import sys

# data = ["text", 4, 4.6, True, 455, "reww"]
# for i, num in enumerate(data, start = 1):
#     print(i, num, id(num), sys.getsizeof(num), hash(num), end = " ")
#     if isinstance(num, int):
#         print("целое число")
#     elif isinstance(num, str):
#         print("сторка")
#     else:
#         print()


# number: int = int(input("ВВедите число: "))
# number1: int = number
# DOUBLE = 2
# OCT = 8

# print(bin(number))
# print(oct(number))

# for i in DOUBLE, OCT:
#     number = number1
#     result: str = ""
#     while number > 0:
#         double_num = number % 2
#         result = str(double_num) + result 
#         number = number // 2
#     print(result) 



# import math
# import decimal

# decimal.getcontext().prec = 42 
# diametr = decimal.Decimal(input("Введите диаметр: "))
# pi = decimal.Decimal(math.pi)
# MAX_LIMIT = 1000
# if  diametr < MAX_LIMIT:
#     length = math.pi * diametr / 2
#     square = math.pi * (diametr / 2) ** 2
#     print(length, square) 
# else:
#     print("введенный диамерт слишком большой!!")

   

    

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

disc = abs(b ** 2 - 4 * a * c)
result = (- b + (disc ** 0.5)) / (2 * a)
result2 = (- b - (disc ** 0.5)) / (2 * a)

print(disc)
