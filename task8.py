x = int(input('Введите координаты точки X: '))
y = int(input('Введите координаты точки Y: '))

if x > 0 and y > 0:
    print(f' Точка с координатами {x, y} находится в 1 четверти')
elif x < 0 and y > 0:
    print(f' Точка с координатами {x, y} находится в 2 четверти')
elif x < 0 and y < 0:
    print(f' Точка с координатами {x, y} находится в 3 четверти')
elif x > 0 and y < 0:
    print(f' Точка с координатами {x, y} находится в 4 четверти')
elif x == 0 and not y == 0:
    print(f' Точка с координатами {x, y} находится на оси x')
elif not x == 0 and y == 0:
    print(f' Точка с координатами {x, y} находится на оси y')
else: #y == 0 and x == 0:
    print(f' Точка с координатами {x, y} находится в начале координат')
