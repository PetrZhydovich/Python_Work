"""Условие:
Написать функцию на Python, которой передаются в качестве параметров
команда и текст. Функция должна возвращать True, если команда успешно
выполнена и текст найден в её выводе и False в противном случае. 
Передаваться должна только одна строка, разбиение вывода использовать 
не нужно
"""
import subprocess



def func(comand, text):
    result = subprocess.run(comand, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if result.returncode == 0 and text in result.stdout:
        return True
    else:
        return False
        
