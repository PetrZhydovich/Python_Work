"""Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания (time.time)
"""

# import time

# class MyString(str):

#     def __new__(cls, value: str, author: str):
#         instance = super().__new__(cls, value)
#         instance.author = author
#         instance.time = time.time()
#         return instance


# if __name__ == '__main__':
#     s = MyString("jdfosdfiosdfis", "Tryry")
#     print(s)
#     print(s.time)
#     print(s.author)


"""Создайте класс Архив, который хранит пару свойств. 
Например, число и строку. 
При нового экземпляра класса, старые данные из ранее 
созданных экземпляров сохраняются в пару списков-архивов
list-архивы также являются свойствами экземпляра
"""

class Archive():
    _one = None
    def __init__(self, num: int, val: str) -> None:
        self.num = num
        self.val = val
    
    def __new__(cls, *args, **kwargs):
        if cls._one is None:
            cls._one = super().__new__(cls)
            cls._one.numbers = []
            cls._one.values = []
        else:
            cls._one.numbers.append(cls._one.num)
            cls._one.values.append(cls._one.val)
        return cls._one

    def __str__(self):
        return f'Класс записывает число {self.num} и строку {self.val} в словарь'

    def __repr__(self):
        return f'Archive({self.num}, "{self.val}")'
        
s = Archive(123, '123355')
print(s.numbers, s.values)

s = Archive(5887, 'Hello')
print(s.numbers, s.values)

s = Archive(8952, 'Hi')
print(s.numbers, s.values)


"""Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания. 
При этом должен создаваться новый экземпляр прямоугольника. 
Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений.
"""

class Rectangle:

    def __init__(self, side_a: float, side_b=None):
        self.side_a = side_a
        if side_b is None:
            self.side_b = side_a
        else:
            self.side_b = side_b

    def square_rectangle(self):
        return self.side_a * self.side_b

    def len_rectangle(self):
        return (self.side_a + self.side_b) * 2


rect = Rectangle(5, 10)
print(rect.len_rectangle(), rect.square_rectangle())

def __add__(self, other):
    a = self.side_a + other.side_a
    b = self.side_b + other.side_b
    return Rectangle(a, b)
    
def __sub__(self, other):
    if self.len_rectangle() < other.len_rectangle():
        self, other = other, self
        a = self.side_a - other.side_a
        b = self.side_b - other.side_b
        return Rectangle(a, b)


rect = Rectangle(5, 10)
#print(rect.len_rectangle(), rect.square_rectangle())
rec1 = Rectangle(4, 8)
rec2 = rect + rec1
print(rect.len_rectangle(),rec1.len_rectangle(),rec2.len_rectangle(),)
rec3 = rect - rec1
print(rect.len_rectangle(),rec1.len_rectangle(),rec3.len_rectangle())
print(f'Первая строна {rec2.side_a} вторая строна {rec2.side_b}')
