MIN_NUMBER = 1
MAX_NUMBER = 100000
get_number = int(input("Введите число от 1 до 100000: "))
j = 0

if get_number < MIN_NUMBER or get_number > MAX_NUMBER:
    print("Введите корректное число !!!")
    quit()
else:
    for i in range(2, get_number):
        if get_number % i == 0:
            j += 1
    if j <= 0:
        print("Число простое")
    else:
        print("Число составное")
        