name = 'Alex'
age = None

a = 42
print(id(a))
a = 'Hello world'
print(id(a))
a = 3.14 / 3
print(id(a))
print(name, age, a, 456, 'text', sep=' (=^.^=) ', end='#')
print('Any text')
res = input('print your text: ')
print('ты написал: ', res)

age = int(input('сколько тебе лет? '))
ADULT = 21
now_old = ADULT - age
print(now_old, 'осталось до совершеннолетия')

