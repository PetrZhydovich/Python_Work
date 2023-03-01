# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата. 

# number = int(input("Enter your number: "))
# number = hex(number)
# print(number)

NUM = 16
DATA = '0123456789ABCDEF'
 
while True:
    getNumber = int(input("enter an integer"))
    if getNumber >= 0:
        break

number = getNumber
result = ''

while number:
    num = number % NUM
    result = DATA[num] + result
    number //= NUM

print(f'Hexadecimal string representation of a number {number} - {result} ')
print(hex(getNumber))
