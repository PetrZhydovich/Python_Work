# Напишите программу, которая принимает две строки 
# вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.


from math import gcd

n1, d1 = map(int, input().split('/'))
n2, d2 = map(int, input().split('/'))
 
if d1 == d2:
    print('{}/{}'.format(n1+n2, d1))
else:
    cd = int(d1*d2/gcd(d1, d2))
    rn = int(cd/d1*n1+cd/d2*n2)
    g2 = gcd(rn, cd)
    n = int(rn/g2)
    d = int(cd/g2)
    print('{}/{}'.format(n, d) if n != d else n)
    