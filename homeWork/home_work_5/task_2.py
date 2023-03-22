# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой 
# длины: имена str, ставка int, премия str с указанием процентов вида «10.25%». 
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

from decimal import Decimal

names = ['Max', 'Gray', 'Fill', 'Nika', 'Sandra']
salaries = [5000, 15000, 20000, 10000, 25000]
bonuses = ['10.25%', '5.25%', '7.00%', '5.75%', '12.50%']

result = {name: bonus for name, bonus in zip(names, (salary * Decimal(rate[:-1]) / 100
                                                     for salary, rate in zip(salaries, bonuses)))}

print(result)
