# Функция высшего порядка - это функция которая в качестве аргумента принимает другую функцию.



# Декоратор - это функция, которая позволяет без изменения кода обернуть другую функцию для того чтобы расширить функционально обернутой функции.


# from  datetime import datetime

# StopAsyncIteration

# start 


# finish

# def decorator(function,):
#     print(f" Called Func name: {function.name}")
#     return function()


# def hello():
#     print("Vsem privet!")
#     return "Hello"

# def john():
#     print("Hello my name is John Snow!")
#     return "John Snow"

# # hello()
# # john()
# decorator(hello)
# decorator(john)

# from typing import Callable


# def benchmark(func:Callable):
#     import time
#     start = time.time()
#     res = func()
#     finish = time.time()
#     print(f"Время выполнения функции {func.name}): заняло {finish - start}")
#     return res



# def loop():
#     i = 1
#     range_number = 100_000
#     while i <= range_number:
#         print(i)
#         i += 1
#     return i

# print(benchmark(loop))

# Pythonic way -> @decorator
# Синтаксический сахар - это кросота кода

# from typing import Callable

# def benchmark(func: Callable):
#     def wrapper(): # 2
#         import time
#         start = time.time()
#         res = func() # 3
#         finish = time.time()
#         print(f'Время выполнения функции {func.__name__}: заняло {finish - start}')
#         return res
#     return wrapper

# @benchmark
# def loop(): # 4
#     i = 0
#     range_number = 1_000_000
#     while i < range_number:
#         i += 1
#     return i

# @benchmark
# def add():
#     i = 0
#     range_number = 1_000_000
#     ls = []
#     while i < range_number:
#         i += 1
#         ls.append(i)
#     return ls

# print(loop()) # 1
# add()

# def strong(func):
#     def wrapper(*args, **kwards):
#         return '<strong>' + func() + '</strong>'
#     return wrapper

# def div(func):
#     def wrapper(*args, **kwards):
#         return '<div>' + func() + '<div>'
#     return wrapper

# @div
# @strong
# @div

# def John():
#     return 'John Snow'

# print(John())

# def trace(func):
#     def wrapper(*args, **kwargs):
#         print(f'Trace: вызвана {func.__name__}(),\n{args} {kwargs}')
#         original_result = func(*args, **kwargs)
#         print(f'Trace: вызвана {func.__name__}(),\nвернула {args} {kwargs}')
#         return original_result
#     return wrapper

# @trace
# def say(name, line):
#     return f'{name}: {line}'

# print(say('John', 'Snow'))

# def func():
#     print('hello world')
#     return func

# func()()()()

# def func1():
#     pass

# def func2(func1):
#     pass


# filter
# map
'-------------------------------------------------------------------------'

# users = ['Nurkamila']

# def login_required(post):    # post
#     def wrapper(user, post_):   # user, post_
#         if user in users:
#             return post(user, post_)
#         else:
#             return 'There is no such user'
#     return wrapper


# @login_required
# def post(user, post_):
#     return 'Succesfully posted'

# print(post('Nurkamila', 'cakes'))
'-------------------------------------------------------------------------'
'task в classroom 1)'
# def repeat(num):
#     def wrapper(func):
#         def wrapper2(name):
#             i = 0
#             while i < num:
#                 i += 1
#                 func(name)
#         return wrapper2
#     return wrapper
  

# @repeat(num=4)
# def function(name):
#     print(f"{name}")


# function('Python')
'-------------------------------------------------------------------------'
'task в classroom 2)'

'-------------------------------------------------------------------------'
