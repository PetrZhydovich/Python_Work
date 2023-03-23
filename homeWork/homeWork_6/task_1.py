# Добавьте в модуль с загадками функцию, которая хранит словарь списков. 
# Ключ словаря - загадка, значение - список с отгадками. 
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

__all__ = ['dictMystery', 'mystery', 'mystery']
dictList = {}


def dictMystery(question, answers) -> dict[str:str]:
    dictList[question] = answers
    return dictList


def mystery(question: str, answer: list, chanse: int) -> int:
    print(question)
    
    for i in range(chanse):
        ans = input("Введите ответ: ")     
        if ans in answer:
            print('Верно')
            return i + 1
        else:
            print('Не верно')
        
    return 0


def mysteryCall(answers: dict) -> None:
    ch = 5
    [mystery(i, j, ch) for i, j in answers.items()]
   
   
if __name__ == '__main__':
    
    q = 'Человек это производит, но им не пользуется. А когда пользуется об этом не знает! '
    an = ['гроб']
    dictMystery(q, an)
    
    q = 'Шел дождь, ехал автобус, в автобусе все спали и Толька - водитель не спал.Как завли водителя и какие были номера автобуса?'
    an = ['Толька', 'мокрые']
    
    mysteryCall(dictMystery(q, an,))
