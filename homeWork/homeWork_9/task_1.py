"""
- нахождение корней квадратного уравнения
- генерация csv с тремя числами в строке, 100-1000 строк
- декоратор, который запускает решение уравнения из csv
- декоратор, который сохраняет параметры и результат в json
"""

import csv
import json
from pathlib import Path
from typing import Callable
from random import randint

__all__ = [
    'quadratic_solve',
    'csv_maker',
]



def json_gen(directory: Path = Path('results.json')):
    def deco(func: Callable):
        def wrapper(*args):
            result = func(*args)
            data = {str(args): result}

            with open(directory, 'a', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
            return result

        return wrapper

    return deco


def solve_starter(directory: Path = Path('numbers.csv')):
    def deco(func: Callable):
        results = []

        def wrapper():
            with open(directory, 'r', encoding='utf-8', newline='') as f:
                csv_file = csv.reader(f)
                for line in csv_file:
                    a, b, c = [int(num) for num in line]
                    result = func(a, b, c)
                    results.append(result)
            return results

        return wrapper

    return deco


def csv_maker(directory: Path):
    num_qty = 3
    min_num = -1_000
    max_num = 1_000
    min_line = 100
    max_line = 1_000

    nums = [[randint(min_num, max_num) for _ in range(num_qty)] for _ in range(randint(min_line, max_line))]

    with open(directory, 'w', encoding='utf-8', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerows(nums)


@solve_starter()
@json_gen()
def quadratic_solve(a: int, b: int, c: int) -> tuple | float | str:
    if a == 0 or b == 0 or c == 0:
        return f'Квадратное уравнение неполное...используйте другую функцию'

    d = b ** 2 - 4 * a * c

    if d < 0:
        return f'not solve'
    if d == 0:
        return -b / 2 * a

    x1 = (-b - d ** 0.5) / (2 * a)
    x2 = (-b + d ** 0.5) / (2 * a)
    return x1, x2


if __name__ == '__main__':
    csv_maker(Path('numbers.csv'))
    print(quadratic_solve())