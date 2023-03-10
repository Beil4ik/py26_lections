# Магические методы (dunder - duble umderscore)- методы, у которых два нижних подчеркивания в начале и в конце. Магия в том, что мы их не вызываем напрямую, а они вызываются в определённый момент, либо они вызываются определёнными операторами или функциями


# res = 5 + 5 #__add__
# print(res)

# class A(int):
#     pass

# obj = A()
# print(dir(obj))


# магические методы которые срабатывают при помоши оператора:

# __eq__(self, other)-> ==  : 5 == 7 seelf: 5 other: 7
# __ne__(self, other)-> !=
# __lt__(self, other)->  < ;  le -> <=
#__gt__(self, other) ->  > ;  ge ->  >=


# __sub__ ->(self, other)  div -> /
# __mul__ -> *  mod ->  %
# __floordiv__ -> // add -> +
#__pow__ -> **


# class MyClass:
#     def __init__(self, string):
#         self.string = string


#     def __add__(self, other):
#         print('add сработал')
#         print(self, '!!!')
#         print(other, '****')
#         res = self.string + other.string
#         return MyClass(res)
     
#     def __str__(self) -> str:
#         return self.string

# obj1 = MyClass('John')
# obj2 = MyClass('Bek')
# obj3 = MyClass('Bayel') 
# # print(obj1 + obj2 + obj3)
# res = (obj1 + obj2 + obj3)
# print(res)
# print(res.string)


# class Word(str):
#     def __init__(self, word):
#         self.word =word

#     def __gt__(self, other: str) -> bool:
#         print(' gt  сработал')
#         print(self, '!!!')
#         print(other, '****')
#         return len(self) > len(other)


# obj1 = Word('Johnb   ')
# obj2 = Word('Hello world')
# print(obj1 > obj2)

'-------------------------------------------------------------------------'
# Конструктор -> __new__(cls)
# Инициализатор -> __init__(self)
# Вызывается, когда создаём объект


# class Conventer(float):
#     def __new__(cls, x):
#         print(' new сработал')
#         print(cls, '!!!')
#         print(__x, 'xxx')
#         if __x < 50:
#             raise ValueError('x  меньше 50!')
#         return super().__new(cls, x)

#     def __init__(self, x):
#         print('init сработал')
#         print(self, '!!!')
#         self.number = x

# obj = Conventer(51)
# print(obj)


# class Word(str):

#     def __new__(cls, word):
#         word = word.replace(' ', '')
#         return super().new(cls, word)

#     def __init__(self, word):
#         self.word =word

#     def __gt__(self, other: str) -> bool:
#         print(' gt  сработал')
#         print(self, '!!!')
#         print(other, '****')
#         return len(self) > len(other)


# obj1 = Word('John   ')
# obj2 = Word('Hello world')
# print(obj1 > obj2)


'-------------------------------------------------------------------------'
# дандер метод стокового отображения объектов

# __str__ -> для отображения строки, которую будут видеть пользователи

# __repr__ -> строковую информацию о том, как создать объект


# __len__ -> len(obj)
# __repr__ ->repr(obj)

# __evel__('6 + 6') -> 6 + 6


# class Base:
#     def __init__(self, string):
#         self.string = string

#     def __str__(self):
#         return f'объект: {self.string}'

#     def __repr__(self):
#         return f'Base("string")'

#     def __len__(self):
#         return 5

# user = Base('Hello John')
# print(user)
# print(repr(user))
# obj1 = eval(repr(user)) #Base("string")
# print(obj1)




# class Person:
#     def __init__(self, attrs: dict):
#         # self.name = attrs['name']
#         #self.a = 5 == settatr(self, 'a' 5)
#         for key, value in attrs.items():
#             setattr(self, key, value)



# alice = Person({'name': 'alice Rose', 'income':180000, 'eyes': 'btown'})
# john = Person({'email': 'johnsnow@gmail.com', 'last_name': 'snow'})
# print(f'{alice.name} --{alice.income}-- {alice.eyes}')
# print(f'{john.email} -- {john.last_name}')

# class MyList(list):
#     def __init__(self, ls):
#         self.ls = ls

#     def __getitem__(self, index):
#         print(self.ls[index - 1])

# x = MyList(['1,2,3,', 'Hello world', 2, 4, 5])
# x[1]
# x[3]
# x[2]


# __iter__ - вызывается, когда мы итерируем объект


# class A:
#     def __init__(self, word):
#         self.word = word

#     def __iter__(self):
#         for i in self.word:
#             # print('iter method')
#             yield i

# x = A('Humnan')
# for i in x:
#     print(i)



# a = range(1, 10)
# print(a)
# for x in a:
#     print(x)

# def generator(num):
#     for i in range(num):
#         yield i

# a =  generator(5)
# for x in a:
#     print(x)

'-------------------------------------------------------------------------'
# class User:
#     def __init__(self, name):
#         self.name = name

#     def __call__(self):
#         print(f' user objerct: {self.name}')
# user1 = User('john Snow')
# user1()