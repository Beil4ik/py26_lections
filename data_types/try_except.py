# Обработка исключений
# Оператор try except

#  ошибки -> связаны с кодом
# SyntaxError
# IndexError
# IndentationError
# TabError

# исключения -> Invalid value
# ZeroDivisError
# ArithmeticError
# NameError
# KeyError
# IndexError
# ValueError
# ImportError
# BaseException #прородитель всех исключенмй

# try except

# try:
#     <body try>
# except <Exception>:
#     <body>
# <else>:
#     <body> Только если всё окей
# <finally>:
#     <body> В любом случае в конце

# num1 = int(input('Введите число: '))
# print(num1)
# print('Important!')

# try:
#     num1 = int(input('Введите число: '))
#     print(num1)
# except ValueError:
#     print('Invalid Value')
# print('Important!')


# try:
#     num1 = int(input('Введите 1-ое число: '))
#     num2 = int(input('Введите 2-ое число: '))
#     print(num1 / num2)
# except (ValueError, ZeroDivisionError) as error:
#     print('Вы ввели некорректные данные!')
#     print(error)

# try:
#     num1 = int(input('Введите 1-ое число: '))
#     num2 = int(input('Введите 2-ое число: '))
#     print(num1 / num2)
# except Exception as error:
#     print('Вы ввели некорректные данные!')
#     print(error)

# list_ = [1,2,3,4,5]
# try:
#     index = int(input('Введите index: '))
#     res = list_[index]
#     print(res)
# except ValueError:
#     print('Value error!')
# except IndexError:
#     print('Index error!')

# try:

#     num1 = int(input('Enter:'))
#     num2 = int(input('Enter:'))
#     result = num1 / num2
# except ZeroDivisionError:
#     print('na 0 delit\' nal\'zya!')
# except ValueError:
#     print('invalid symbols for int()!')
# else:
#     print(result)
# finally:
#     print('The end!')
