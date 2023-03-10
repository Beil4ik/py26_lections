# num1 = 28
# num2 = 65
# num3 = 1100
# num4 = 54
# num5 = 32

# def operations(num):
#     print({"2": num  2, "3": num  3, "100": num / 100})

# operations(num1)
# operations(num2)
# operations(num3)
# operations(num4)
# operations(num5)
# dict1 = {"2": num1  2, "3": num1  3, "100": num1 / 100}
# dict2 = {"2": num2  2, "3": num2  3, "100": num2 / 100}
# dict3 = {"2": num3  2, "3": num3  3, "100": num3 / 100}
# dict4 = {"2": num4  2, "3": num4  3, "100": num4 / 100}
# dict5 = {"2": num5  2, "3": num5  3, "100": num5 / 100}
# print(dict1,dict2,dict3,dict4,dict5)

# Функция - это именнованная часть программы, которая содержит в себе набор инструкций, и котороя может вызываться в других частях программы столько раз, сколько угодно


# def name_of_function(<a, b> #параметры)
    # <body> #код, какая-то логика который возвращает конечный результат
    # <return> #оператор для возвращения результата

# name_of_function(<5, 6> #аргументы)

# Параметры функции - переменные, которые будут принимать данные, которые мы передаём в функцию

# Аргументы - данные, которые мы передаём в функцию, в моменте когда её вызывает

# return - оператор, который нужен для того, чтобы функция возвращала результат, если return не указать, то функция возвращает None

# len([1,2,3,4,5])

# ls = [1,2,3,4,5,6,7]
# str1 = 'Hello world s vami Kani!'

# def our_len(obj):
#     i = 0
#     print(obj)
#     for x in obj:
#         i += 1
#     print('result:', i)
#     return i

# print(our_len(ls), '!!!!!')
# our_len(str1)
# result = our_len('12345')
# print(result)

# res = print('123')
# print(res)

# res = max([1,2,3,4])
# print(res)
# print(max([123]))


# def isEven(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False

# print(isEven(7))
# print(isEven(9))
# print(isEven(10))

# from typing import List


# def isEven(obj: int) -> bool:
#     '''Our function returns True or False while checking number for even number!'''
#     if obj % 2 == 0:
#         return True
#     return False

# print(isEven(8))

# ls = [1,2,3]
# print(ls.reverse())
# print(ls)

# def my_func(a,b,c):
#     pass

# my_func(1,2,3)


# tenet, ded, anna, kazak
# from typing import List

# def get_palindrome(words: List[str]) -> List[str]:
#     '''Function return a polindrom list of strings!'''
#     result = []
#     for x in words:
#         if x.lower() == x[::-1].lower():
#             print('Polindrom find: {x}!')
#             result.append(x)
#     return result

# ls = ['John', 'Ono', 'kazak', 'Peter', 'dovod', 'radar', 'apa', 'piko']
# print(f'Result: {get_polindrom(ls)}')
# print(get_polindrom(['John', 'Snow', 'from']))

# '''Напишите функцию которая будет возвращать ваш депозит через определнное время с процентом 10%, возращать финальное количество денег. Мин период вложения 3 года. Мин ставка денек 30 000 сомов'''

# from typing import Optional

# def get_percentage(money: Optional(int, float), period: int) -> Optional(int, float):
#     '''returns final amount of money!'''
#     if money < 30000:
#         raise ValueError('Invalid value for money parameter!')
#     elif period < 3:
#         raise ValueError('Invalid value for period parameter!')

#     i = 0
#     while i < period:
#         money += money * 0.1
#         # money = money * 1.1
#         # money = money + (money / 100 * 10)
#         i += 1
#     return money


# try:
#     money = float(input('Введите сумму денег: '))
#     year = float(input('Введите срок вашего депозита: '))
# except ValueError:
#     print('Invalid values!')
# else:
#     print(get_percentage(money, year))

# print([1,2,3,4,5].index(3,4))

'-------------------------------------------------------------------------'
# Default parametres
# def func():
#     print('Hello world')

# func()

# def print_welcome(name ='User'):
#     print(f'Welcom, {name}!')

# print_welcome('Beil4ik')

# def introduce(name: str, last_name: str, work: str = None):
#     print(f'This person name is {name}!')
#     print(f'This person last name is {last_name}!')
#     if work:
#         print(f'This persons name is {work}!')

# introduce('John', 'Snow', 'King')
# introduce('Sultan', 'Katana')

'-------------------------------------------------------------------------'
# 'Hello world! My name is John^ last name is Snow. Nice to meet you!'
# 'you! meet to Nice Snow. ...'

# def get_reverse_text(text: str) -> str:
#     '''reversing the text'''
#     ls = text.split(' ')
#     # print(ls[::-1])
#     return ' '.join(ls[::-1])

# str1 = 'Hello world! My name is John, last name is Snow. Nice to meet you!'
# print(get_reverse_text(str1))