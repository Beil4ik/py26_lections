# Инкапсуляция:
# 1. Связь данных с методами которые должны управлять этими атрибутами
# 2. Механизм языка, который позволяет ограничить доступ к определённым компонентам класса

# Инкапсуляция как связь


# class Phone:
#     number = '+996700700700'

#     def print_number(self):
#         print(f'Мой номер: {self.number}')

# my_phone = Phone()
# print(my_phone.number)
# my_phone.print_number()


# Инкапсуляция как управление доступом
# 3 уровня доступа в питоне :
        # 1. Публичный(public) - number, print_number
        # 2. Защищённый(protected, parent/child) - _number
        # 3.Приватный(__private, только в текущем) - __number

'-------------------------------------------------------------------------'

# class Car:
#     _country = 'Germany'

#     def __init__(self):
#         self.marka = 'Mercedes-Benz' # public(публичный)
#         self._model = 'w140' # protected(защищённый)
#         self.__motor = 'ABC' #private(приватный)

# obj = Car()
# print(obj.marka)
# print(obj._country)
# print(obj._model)
# print(obj._Car__motor)

'-------------------------------------------------------------------------'

# class Phone:
#     username = 'John Snow'
#     _caller = 'Jamie Lanister'
#     __count_of_calls = 0

#     def call(self):
#         print(f'{self._caller} звонит!')

#     def __increment_of_calls(self):
#         self.__count_of_calls +=1

#     def turn_on(self):
#         print(f'{self.username} взял трубку!')
#         self.__increment_of_calls()

#     def get_count(self):
#         print(self.__count_of_calls)

# obj = Phone()
# obj.get_count()
# obj.call()
# obj.turn_on()
# obj.get_count()

'-------------------------------------------------------------------------'

# getter & setter
# Они используются для получения и установки значений в защищённые атрибуты, чтобы избежать прямого доступа к защищённому атрибуту и ещё с помощью сеттеров и геттеров можно добавлять логику проверки при получении данных

# class Person:
#     def __init__(self, name) -> None:
#         self.name = name
#         self.age = 0

#     def display_info(self):
#         print(f'My name is {self.name}, I\'m {self.age} years old!')

# john = Person('John')
# john.display_info()
# john.name = None
# john.age = 18
# john.display_info()

# class Person:
#     def __init__(self, name) -> None:
#         self.__name = name
#         self.__age = 0

#     def display_info(self):
#         print(f'My name is {self.__name}, I\'m {self.__age} years old!')

#     # getter
#     def get_name(self): return self.__name

#     # setter
#     def set_name(self, name):
#         if not isinstance(name, str):
#             print('Invalid value fo name!')
#         else:
#             self.__name = name

#     def get_age(self): return self.__age

#     def set_age(self, age):
#         if not isinstance(age, int) or not 0 <= age <150:
#             print('Invalid value for age!')
#         else:
#             self.__age = age


# john = Person('John')
# john.display_info()
# john.set_name(None)
# john.set_age(-18)
# john.display_info()
# john.set_name('Jamie')
# john.set_age(24)
# john.display_info()


# class Russia:
#     __name = 'Russian Federation'
#     __population = 0

#     def get_population(self): return self.__population

#     def set_population(self, num):
#         if not isinstance(num, int) or num < 0:
#             print('Invalid value for population!')
#         else:
#             self.__population = num

#     def get_name(self): return self.__name

#     def display_info(self):
#         print(f'Population of {self.get_name()}: {self.get_population()}')

# obj = Russia()
# obj.set_population(143_000_000)
# obj.display_info()

'-------------------------------------------------------------------------'
# class Person:
#     def __init__(self, name) -> None:
#         self.name = name
#         self.__age = 0

#     def _age_increment(self):
#         self.__age += 1

#     def birthday(self):
#         print(f'Today {self.name}\'s birthday!!!')
#         self._age_increment()

#     def display_info(self):
#         print(self.name, self.__age)

# obj = Person('John')
# obj.display_info()
# obj.birthday()
# obj.display_info()

