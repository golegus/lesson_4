"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию


year = input('Ввведите год рождения А.С.Пушкина:')
while year != '1799':
    print("Не верно")
    year = input('Ввведите год рождения А.С.Пушкина:')

day = input('Ввведите день рождения Пушкин?')
while day != '6':
    print("Не верно")
    day = input('В какой день июня родился Пушкин?')
print('Верно')
"""

def check_year(year, person):
    input_year=''
    while year!=input_year:
        input_year=input (f'Введите год рождения {person}: ')
        if year!=input_year :
            print('Неверно. Попробуйте еще раз.')
    print('Верно!')
    return input_year

def check_day(day, month, person):
    input_day=''
    while day!=input_day:
        input_day=input (f'В какой день {month} родился {person}?: ')
        if day!=input_day :
            print('Неверно. Попробуйте еще раз.')
    print('Верно!')
    return input_day

def check_birthday(kwargs):
    check_year(kwargs.get('birth_year'),kwargs.get('person'))
    check_day(kwargs.get('birth_day'),kwargs.get('birth_month'),kwargs.get('person'))

birthday={'person':'А.С.Пушкин', 'birth_day':'6', 'birth_month':'июня', 'birth_year':'1799'}

check_birthday(birthday)


