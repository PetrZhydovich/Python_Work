"""Доработаем задачи 5. Создайте класс-фабрику. Класс принимает тип животного 
(название одного из созданных классов) и параметры для этого типа. 
Внутри класса создайте экземпляр на основе переданного типа и верните
его из класса-фабрики.
"""

class Fauna:
    def __init__(self, name: str, blood_color: str):
        self.name = name
        self.blood_color = blood_color

    def eat(self):
        print(' Need food')


class Birds(Fauna):
    def __init__(self, name: str, blood_color: str, feathers: bool):
        super().__init__(name, blood_color)
        self.feathers = feathers

    def fly(self):
        print('I can fly!')


class Fishes(Fauna):
    def __init__(self, name: str, blood_color: str, gills: bool):
        super().__init__(name, blood_color)
        self.gills = gills


class Reptiles(Fauna):
    def __init__(self, name: str, blood_color: str, scales: bool):
        super().__init__(name, blood_color)
        self.scales = scales


class Factory(Fishes):
    def __init__(self, name: str, blood_color: str, type_animals: bool):
        super().__init__(name, blood_color)
        self.type_animals = type_animals
        return type_animals

bird = Birds('Кеша', 'красная', True)
bird.fly()
bird.eat()