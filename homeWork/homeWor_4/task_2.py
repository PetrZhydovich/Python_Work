# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.

def modic_dic(**kwargs):
    dictionary = {}
    for key, item in kwargs.items():
        item = str(item)
        dictionary[item] = key
        
    return dictionary


print(modic_dic(a = 12, b = 5, c = 8))
