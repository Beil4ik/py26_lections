# sentence = input('Vvedite predlojeniye: ')

# if sentence[-1] == '?':
#     print('Voprositel\'noe predlojeniye!')
# else:
#     print('Normal one!')

# print('Voprositel\'noe predlojeniye!' if sentence[-1] == '?' or sentence[-2:] == '?!' else 'Normal one!')
'-----------------------------------------------------------------------------------'

# Ternery operators(Тернарный оператор) - это конструкция, которая аналогична по-своему действию  конструкции if\else, но при этом записывается в одну строчку

# number = 21
# res = 'even number' if number % 2 == 0 else 'odd number'
# print(res)

# <выражение если в условии True> if <условие> else <выражение если в условии False>

# num = int(input('Vvedite chislo: '))

# res = num -100 if num <100 else num * 2
# print(res)

# ls = [55, 65, 75, 89, 100, 15, 6]
# print(ls)
# choice = input('Vvedite max/min: ')

# res = max(ls) if choice.lower().strip() == 'max' else min(ls)
# print(res)

# if choice.lower().strip() == 'max':
#     res = max(ls)
# elif choice.lower().strip() == 'min':
#     res = min(ls)
# else:
#     res = 'Invalid choice'
# print(res)
'-----------------------------------------------------------------------------------'

# from string import digits

# symbols = digits + '-' + '.' #0123456789-.
# flag = True

# while flag:
#     is_correct_number = True
#     num1 = input('Введите первое число: ')
#     for x in num1: #56y56yt
#         if not x in symbols:
#             print('Вы ввели неправильное число! ')
#             is_correct_number = False
#             break
#     if not is_correct_number:
#         continue

#     num2 = input('Введите второе число: ')
#     for x in num2: #587t
#         if not x in symbols:
#             print('Вы ввели неправильное число! ')
#             is_correct_number = False
#             break
#     if not is_correct_number:
#         continue

#     num1 = float(num1) if '.' in num1 else int(num1)
#     num2 = float(num2) if '.' in num2 else int(num2)
#     operator = input('Введите оператор(+, -, *, /): ')

#     if operator == '+':
#         print(f'Результат: {num1 + num2}')
#     elif operator == '-':
#         print(f'Результат: {num1 - num2}')
#     elif operator == '*':
#         print(f'Результат: {num1 * num2}')
#     elif operator == '/':
#         print(f'Результат: {num1 / num2}')
#     else:
#         print('Вы ввели неправильный оператор!')

#     choice = input('Хотите продолжить(yes/no)? ')
#     if choice.lower().strip() == 'no':
#         flag = False
#         print('Пока, пока!')

