"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию

"""

def question_date(question, date):
    answer=input(question)
    while answer!=date:
        print("Не верно")
        answer=input(question)

person='А.С.Пушкин'
birth_year='1799'
birth_month= 'июня'
birth_day='6'

question_date(f"В какой год родился {person}? ",birth_year)
question_date(f"В какой день {birth_month} родился {person}? " ,birth_day)
print("Верно!")

