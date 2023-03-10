'''SCOPE - Области видимости и пространства'''

# def func():
#     var = 15
#     return var * 2

# print(func())

# Область видимости и пространство имён или scopes определяет контекст переменной, в рамках которого мы можем её использовать


# a = 5
# print(a)  # глобальная область видимости
# def func():
#     print(a)  #локальная область видимости
# func()

# built-in (всторенная ) - print, len, max 
# global (глобальнная)
# enclosed (не локальная , nonlocal)
#local (локальнная)

# x = 200

# def func():
#     print(x, '!')

# func()

'-------------------------------------------------------------------------'

# a = 10 # global
# print #built - in
# def hello(): #global
#     a = 'hello world' # local
#     print(a, 'local inside at func')

# hello()
# print(a, 'global')

# LEGB 
# local -> enclosed -> global -> built-in


# x = 'global'
# print(x, '1')

# def enclosed():
#     x = 'enclosed' # enclosed
#     def local():
#         x = 'local' # local
#         print(x, '3')
#     print(x, '2')
#     local()
#     print(x, '4')

# enclosed()
# print(x, '5')

'-------------------------------------------------------------------------'

# a = 10

# def func():
#     a = 'local'
#     print(a)

# func()
# print(a)

# LEGB

'-------------------------------------------------------------------------'

# i = 0

# def increment():
#     i = i + 1

# increment()

# global -> позволяет изменять значение глобальной переменной, находясь в локальной или замкнутой области видимости

# nonlocal -> позволяет изменять значение не локальной переменной, находясь в локальной области видимости


# var = 100

# def increment():
#     global var
#     var += 1

# print(var)
# increment()
# increment()
# increment()
# increment()
# increment()
# print(var)

'-------------------------------------------------------------------------'

# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment

# c = counter()
# print(c) # <function counter.<locals>.increment at 0x7f65c335e050>
# print(c()) # 1
# print(c()) # 2
# print(c()) # 3
# print(c()) # 4
# print(c()) # 5
# print(c()) # 6
# print(c()) # 7
# b = counter()
# print(c()) # 8
# print(b()) # 1
# print(b()) # 2
# print(c()) # 9

'-------------------------------------------------------------------------'

# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment

# i = counter()

# for x in range(0, 100000):
#     if x % 3 == 0 and x % 5 == 0:
#         res = i()
#         print(res)

# print(f'Result: {res}')

'-------------------------------------------------------------------------'

# print(dir(__builtins__))
# print(len(dir(__builtins__)))

'-------------------------------------------------------------------------'

# globals(), locals()

# a = 5
# b = 6
# c = 7
# def func():
#     john = 'John Snow'
#     print(locals())

# print(globals(), '\n')
# # print()
# func()
'-------------------------------------------------------------------------'

# Дан список внутри которого список из трех чисел. Нужно найти максимальную сумму среди всех списков.
# [[1,2,3], [3,3,5], [5,5,5,5]] -> 6, 11, 20 -> 20

# ls = [[1,2,3], [3,3,5], [5,5,5,5]]

# result = max(sum(x) for x in ls)
# print(result)

