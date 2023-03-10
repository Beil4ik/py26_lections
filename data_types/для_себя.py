# first = 1
# second = 2
# third = 3
# first, third, second = second, first, third
'-------------------------------------------------------------------------'

# string = "hohoho"

# print()

# print((1, 2, 3) < (1, 2, 4))
'-------------------------------------------------------------------------'

# ver = 0
# while (ver == 0):
#     player = int(input("1 - камень, 2 - ножницы, 3 - бумага. "))
# if (player == 1 or player == 2 or player == 3):
#     ver = 1

# if player == 1:
#         print("Вы выбрали камень.")
# if comp == 2:
#     print("Компьютер выбрал ножницы.")
#     win=1
#     win=2
#     win=0
'-------------------------------------------------------------------------'

# import random
# ver = 0
# while (ver == 0):
#         player = int(input("1 - камень, 2 - ножницы, 3 - бумага. "))
#         if (player == 1 or player == 2 or player == 3):
#             ver = 1    
# if player == 1:
#         print("Вы выбрали камень.")  
# if player == 2:
#         print("Вы выбрали ножницы.") 
# if player == 3:
#         print("Вы выбрали бумагу.")  
# comp = random.randint(1, 3)
# if comp == 1:
#         print("Компьютер выбрал камень.") 
# if comp == 2:
#         print("Компьютер выбрал ножницы.")
# if comp == 3:
#         print("Компьютер выбрал бумагу.")
# # определяем победителя
# if player == comp:
#         win = 0
# if player == 1 and comp == 2:
#         win = 1 
# if player == 1 and comp == 3:
#         win = 2 
# if player == 2 and comp == 1:
#         win = 2  
# if player == 2 and comp == 3:
#         win = 1 
# if player == 3 and comp == 1:
#         win = 1
# if player == 3 and comp == 2:
#         win = 2
# if win == 0:
#         print("Ничья!")
# if win == 1:
#         print("Победил игрок!")
# if win == 2:
#         print("Победил компьютер!")
'-------------------------------------------------------------------------'

# name = input('Введите число через запятую: ')
'-------------------------------------------------------------------------'

# a = list('py')
# print(len(a))
'-------------------------------------------------------------------------'

# for i in range(1, 10):
#     i -= 5
# print(i)
'-------------------------------------------------------------------------'

# a = [1,3]
# print(int(a))
'-------------------------------------------------------------------------'

# for i in range(9,4,-3):
#     print(i)
'-------------------------------------------------------------------------'

# list_ = [5, 7, 8, 1, 3, 0, 8]

# list_.insert(7, 'Makers')
# remove_element = list_.remove(8)

# print(list_)
# print(remove_element)
'-------------------------------------------------------------------------'

# list_ = [5, 7, 6, 1, 3, 0, 8]

# list_.insert(7, 'Makers')
# remove_element = list_.remove(8)

# print(list_)
# print(remove_element)
'-------------------------------------------------------------------------'

# def rev_key(dct):
#     dct_new = dict()
#     for i, v in dct.items():
#         for w in v:
#             dct_new[w] = dct_new.get(w, []) + [i]
#     return dct_new
        
# dct = {1: 'a', 2: 'b', 3: 'c'}
# print(rev_key(dct))
'-------------------------------------------------------------------------'

# nums = {1: 'a', 2: 'b', 3: 'c'}
# nums.pop(1)
# 'a'
# nums
# {2: 'b', 3: 'c'}
# nums.popitem()
# (3, 'c')
# nums
# {a: '1', b: '2', c: '3'}
# print(nums)
'-------------------------------------------------------------------------'

# a = {10: 'ten', 20: 'twenty', 30: 'thirty'}

# for i in a:
#     print(i)
'-------------------------------------------------------------------------'

# name = input('Количество гостей: ')
# name1 = input('Имена гостей: ')
# print(list(guest))
'-------------------------------------------------------------------------'

# a_set = {'Jane', 'Eyre', 22}
# print(a.append('Hello wrold'))
'-------------------------------------------------------------------------'

# robert = {5, 7, 11, 10, 28} 
# kail = {1, 5, 14, 8, 22} 
# merri = {19, 20, 3, 11, 10}

# if robert&kail and merri&robert:
#     print("kail merri")
# elif merri&robert:
#     print("merri")
# elif robert&kail:
#     print("kail")
# else:
#     print('no one')
'-------------------------------------------------------------------------'

# set1 = {i*2 for i in range(5)}
# set2 = {i*2+1 for i in range(5)}
# if set1 & set2:
#     print('Множества пересекаются!')
# else:
#     print('Множества не пересекаются!')
'-------------------------------------------------------------------------'

# tilek = {'Dodo', 'ImperiaPizza', 'Freshbox'}
# timur = {"OchakKebab", "FreshBox"}
# alexander = {"OchakKebab", "FreshBox"}
# elina = {}
'-------------------------------------------------------------------------'
# ingredients = {"cыр чеддар","грибы", "соус","шпинат"}
# ingredients.add("помидор")
# ingredients.discard("колбаса")
# ingredients.remove("шпинат")
# ingredients.add("базилик")
# ingredients.update({"cыр чеддар", "сыр моцарелла"})
# print(ingredients)
'-------------------------------------------------------------------------'

# inp1 = int(input())
# inp2 = int(input())
# inp3 = int(input())
# result = inp1*inp2 % inp3
# print(result)
'-------------------------------------------------------------------------'

# num1 = 8
# num2 = 4
# print(num1**num2)
# print(num2**num1)
'-------------------------------------------------------------------------'

# num = -2
# print(abs(num))
'-------------------------------------------------------------------------'

# string = 'kilimanjaro'
# print(string[-2:])
'-------------------------------------------------------------------------'

# string1 = 'makers'
# string2 = 'bootcamp'

# result = string1 + ' ' + string2
# print(result)
'-------------------------------------------------------------------------'

# string = 'Hello'

# f=string[0]
# l=string[-1]
# st1=string[1:-1]
# print(l+st1+f)
'-------------------------------------------------------------------------'

# string = 'Makers bootcamp'
# str_length = len(string)

# print(string[1::2])
'-------------------------------------------------------------------------'

# Объявите переменную string со значением в виде любой строки.
# Поменяйте шестую букву на K.
# Например, если в переменной хранится данная строка: 'abracadabra'

# string = 'abracadabra'
# result1 = string[0:5]
# result = string[6:]
# print(result1+"K"+result)
'-------------------------------------------------------------------------'

# string = 'hello world'
# print((string+'\n')*3)
'-------------------------------------------------------------------------'

# string = "          Как прекрасен этот мир!   "
# result = string.strip()
# print(result)
# print(len(result))
'-------------------------------------------------------------------------'

# Вам даны 2 списка, напишите код, который будет выводить разницу первого списка от второго и наоборот


# colors1 = ['red', 'orange', 'green', 'blue', 'white']
# colors2 = ['black', 'yellow', 'green', 'blue']

# res1 = []
# for i in range(len(colors1)):
#     if colors1[i] not in colors2:
#         res1.append(colors1[i])


# res2 = []
# for i in range(len(colors2)):
#     if colors2[i] not in colors1:
#         res2.append(colors2[i])

# print(res1, res2)
'-------------------------------------------------------------------------'

# name_of_friends = ['hello', 'world', 'python', 'makers', 'bootcamp']
# for x in name_of_friends:
#     print(x)
'-------------------------------------------------------------------------'

# labels = ['Honda', 'Kawasaki']
# for x in labels:
#     print('I like brand', x)
'-------------------------------------------------------------------------'

# name = input()
# list_ = sorted(name.split(","))
# print(list(list_))
'-------------------------------------------------------------------------'

# a = input()
# list_ = a.split(",")

# tuple_= tuple(list_)
# print(list_)
# print(tuple_)
'-------------------------------------------------------------------------'
# list_ = []
# name1 = input("Введите имя и фамилию: ")
# name2 = input("Введите имя и фамилию: ")
# name3 = input("Введите имя и фамилию: ")
# name4 = input("Введите имя и фамилию: ")
# name5 = input("Введите имя и фамилию: ")
# list_.append(name1)
# list_.append(name2)
# list_.append(name3)
# list_.append(name4)
# list_.append(name5)
# target = " "
# surnames = []
# for x in list_:
#     t = x.find(target)
#     v = x.rfind(target)
#     if x.count(target) > 1:
#         surnames.append(x[v+1:])
#     else:
#         surnames.append(x[t+1:])
# print(sorted(surnames))
'-------------------------------------------------------------------------'

# colors = ["Red", "Green", "Blue", "White", "Black", "Yellow", "Orange"]
# res = []
# for x in colors:
#     res.append(x[::-1])
# print(sorted(res, key=len))
'-------------------------------------------------------------------------'

# a = int(input())
# b = int(input())
# c = int(input())
# if a <= b and a <= c and b <= c:
#     print(a,b,c)
# elif a <= c and a <= b and c <= b:
#     print(a,c,b)
# elif b <= a and b <= c and a <= c:
#     print(b,a,c)
# elif b <= c and b <= a and c <= a:
#     print(b,c,a)
# elif c <= a and c <= b and a <= b:
#     print(c,a,b)
# elif c <= b and c <= a and b <= a:
#     print(c,b,a)
# else:
#     print(a,b,c)
'-------------------------------------------------------------------------'

# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# res = []
# for i in nums:
#     if i < 5:
#         res.append(i)
# print(res)
'-------------------------------------------------------------------------'

# list_ = ['world', 'hello']
# name = list_[0]
# name1 = list_[1]
# new_list = [name1,name]
# print(new_list)
'-------------------------------------------------------------------------'

# list_ = [8, 6, 8, 10, 8, 20, 10, 8, 8]
# number = 8
# name = list_.count(number)
# print(name)
'-------------------------------------------------------------------------'

# name_of_list = ['1234567']
# new_list = name_of_list[0]
# i = len(new_list)
# if i%2==0: new_list = name_of_list[0][i//2:] + name_of_list[0][:i//2]
# else:
#     new_list = name_of_list[0][i//2+1:] + name_of_list[0][:i//2+1]
# print(list(new_list))
'-------------------------------------------------------------------------'

# number = int(input())
# if number > 0:
#     print('True')
# else:
#     print('False')
'-------------------------------------------------------------------------'

# string = input()
# if len(string) > 5:
#     print('True')
# else:
#     print('False')
'-------------------------------------------------------------------------'

# greeting = input()
# if greeting is('Hi'):
#     print('Привет!')
# else:
#     print('NO')
'-------------------------------------------------------------------------'

# mark = int(input())
# if mark >= 90:
#     print('Отлично, Ваша оценка 5!')
# elif mark >= 80:
#     print('Здорово, Ваша оценка 4!')
# elif mark >= 70:
#     print('Хорошо, Ваша оценка 3!')
# elif mark >= 60:
#     print('Вам стоит подучить материал')
# else:
#     print('Вы не сдали экзамен')
'-------------------------------------------------------------------------'

# count = 0
# number = int(input())
# if number is.digital:
#     count.setdefault
'-------------------------------------------------------------------------'

# x = int(input())
# y = int(input())
# if x % y == 0:
#     print("x делится на y")
#     print("Частное: %s" %(x//y))
# else:
#     print("x не делится на y")
#     print("Частное: %s" %(x//y))
#     print("Остаток: %s" %(x%y))
'-------------------------------------------------------------------------'

# tuples = [(), ('ram','15','8'), (), ('laxman', 'sita')]
# cleared_tuples = [c for c in tuples if c]
# print(cleared_tuples)
'-------------------------------------------------------------------------'

# list_ = []
# for x in range(54, 9184):
#     if x % 5 == 0:
#         list_.append(x)
# print(list_)
'-------------------------------------------------------------------------'

# list1 = [1,2,3,4,5]
# list2 = [5,6,7,8,9]
# res = None
# for i in list1:
#     for j in list2:
#         if i==j:
#             res = True
#             break
#         else:
#             res = False
# print(res)
'-------------------------------------------------------------------------'
'Comprehensions'
# 1)
# list_ = [item for item in range(1, 101)]
# print(list_)
'-------------------------------------------------------------------------'
# 2)
# list_ = [x for x in range(1,50) if x % 2 != 0]
# print(list_)
'-------------------------------------------------------------------------'
# 3)
# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [x for x  in list_ if x % 2 == 0 and x > 0]
# print(int_list)
'-------------------------------------------------------------------------'
# 4)
# list_ = [x **2 for x in range (1,26)]
# print(list_)
'-------------------------------------------------------------------------'
# 5)
# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# int_list = [int(x) for x in str_list]
# print(int_list)
'-------------------------------------------------------------------------'
# 6)
# list_ = [x ** 2 if x % 2 == 0 else x for x in range(1, 11)]
# print(list_)
'-------------------------------------------------------------------------'
# 7)
# list_ = [x == False if x % 2 != 0 else True for x in range(1, 11)]
# print(list_)
'-------------------------------------------------------------------------'
# 8)
# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ]
# new_list = ['shorter' if len(i) <= 4 else 'longer' for i in list_name]
# print(new_list)
'-------------------------------------------------------------------------'
# 9)
# dict_ = {x: x**2 for x in range(1, 11)}
# print(dict_)
'-------------------------------------------------------------------------'
# 10)
# n = int(input())
# dict_ = {i: i ** 2 for i in range(n, 501) if i % n == 0}
# print(dict_)
'-------------------------------------------------------------------------'
# 11)
# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_ = {k: list(range(1,v+1)) for k, v in a.items()}
# print(dict_)
'-------------------------------------------------------------------------'
# 12)
# dict_ = {'first': 1, 'second': 2, 'third': 3}
# a = {k: 'odd' if v % 2 != 0 else 'even'for k, v in dict_.items()}
# print(a)
'-------------------------------------------------------------------------'
# 13)
# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# a = [int(i) for i in filter(lambda x: x.isnumeric(),string_.split())]
# list_ = list(map(str,a))
# print(list_)
'-------------------------------------------------------------------------'
# 14)
# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
# 'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
#  'Nik': {'history': 84, 'math': 85, 'literature': 87}}

# new_dict = {x:max(y,key=lambda x:y.get(x)) for x,y in dict_.items()} 
# print(new_dict)
'-------------------------------------------------------------------------'
# 15)
# my_dict = {'first': {'a': 1}, 'second': {'b': 2}}
# dict_ = {k:y for k,v in my_dict.items() for x,y in v.items()}
# print(dict_)
'-------------------------------------------------------------------------'
# 16)
# list_ = [x * 2 for x in range (1, 13)]
# print(list_)
'-------------------------------------------------------------------------'
# 17)
# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [x-x+1 if x < 0 else x for x in list_]
# print(int_list)
'-------------------------------------------------------------------------'
# 18)
# list1 = [1, 2, 'hello', 3, 'world', 4, 5, 'book', 'code', 6, 'Makers', 7, 8, 9, 10]
# list2 = [x for x in list1 if x == str(x)]
# print(list2)
'-------------------------------------------------------------------------'
# 19)
# list_ = [0, 3, 9, 7, 5, 2, 18, 4]
# list1 = [x for x in list_ if x > 5]
# print(list1)
'-------------------------------------------------------------------------'
# 20)
# list_ = [False, True, False, True, False, True, False, True, False, True]
# list1 = [x+0 if x == False else 1 for x in list_]
# print(list1)
'-------------------------------------------------------------------------'
# 21)
# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# new_list = [len(x) for x in list_name]
# print((new_list))
'-------------------------------------------------------------------------'
# 22)
# list_ = [x for x in range(1,1000,125) if x % 2 == 0]
# print(list_)
'-------------------------------------------------------------------------'
# 23)
# list1 = [44,54,64,74,104]
# list2 = [x+6 for x in list1]
# print(list2)
'-------------------------------------------------------------------------'
# 24)
# list1 = [2, 4, 6, 8, 10, 12, 14]
# list2 = [x for x in list1 if x**2 > 50]
# print(list2)
'-------------------------------------------------------------------------'
# 25)
# string = "happy birthday!"
# list_ = [x for x in string if x != " " and x != "!"]
# print(list_)
'-------------------------------------------------------------------------'
# 26)
# dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}}
# list1 = [y for k,v in dict_.items() for x,y in v.items()]
# print(list1)
'-------------------------------------------------------------------------'
# 27)
# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ]
# dict1 = {k : len(k)**2 for k in list_name if len(k)>4}
# print(dict1)
'-------------------------------------------------------------------------'
# 28)
# dict_ = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# list1 = [key.upper() for key,value in dict_.items() if 200 < value < 5000]
# print(list1)
'-------------------------------------------------------------------------'
# 29)
# dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# dict2 = {k.replace('i',''):k.count('i') for k,v in dict1.items()}
# print(dict2)
'-------------------------------------------------------------------------'
# 30)
# list1 = [1, 2, 3, 0, None, 'a', 'abc', [], 23, [1, 2, 3, 4], '', {'a': 1, 'b': 2}, 'drf', []]
# list2 = [x for x in list1 if x]
# print(list2)
'-------------------------------------------------------------------------'
# 31)
# SPL_Patrons = [
# ['Kim Tremblay', 134],
# ['Emily Wilson', 42],
# ['Jessica Smith', 215],
# ['Alex Roy', 151],
# ['Sarah Khan', 105],
# ['Samuel Lee', 220],
# ['William Brown', 24],
# ['Ayesha Qureshi', 199],
# ['David Martin', 56],
# ['Ajeet Patel',69]
# ]
# readers = [x[0] for x in SPL_Patrons if x[1] > 100]
# print(readers)
'-------------------------------------------------------------------------'
# 32)
# SPL_Patrons = [
# ['Kim Tremblay', 134],
# ['Emily Wilson', 42],
# ['Jessica Smith', 215],
# ['Alex Roy', 151],
# ['Sarah Khan', 105],
# ['Samuel Lee', 220],
# ['William Brown', 24],
# ['Ayesha Qureshi', 199],
# ['David Martin', 56],
# ['Ajeet Patel',69]
# ]
# saved_amount = [round(x[1]*11.95,2)for x in SPL_Patrons]
# print(saved_amount)
'-------------------------------------------------------------------------'
# 33)
# prairie_pirates = [
# ['Tractor Jack', 1000, True],
# ['Plowshare Pete', 950, False],
# ['Prairie Lily', 245, True],
# ['Red River Rosie', 350, True],
# ['Mad Athabasca McArthur', 842, False],
# ['Assiniboine Sally', 620, True],
# ['Thresher Tom', 150, True],
# ['Cranky Canola Carl', 499, False]
# ]
# spisok = [[x[0], x[1] * 42] for x in prairie_pirates if x[2]==True]
# print(spisok)
'-------------------------------------------------------------------------'
# 34)
# dict_ = {
#     'Sasha': {
#         'likes': 23,
#         'comments': 2,
#         'rating': 4
#     },
#     'Aliya': {
#         'likes': 34,
#         'comments': 5,
#         'rating': 5
#     },
#     'Dasha': {
#         'likes': 15,
#         'comments': 3,
#         'rating': 2
#     },
#     'Luna': {
#         'likes': 12,
#         'comments': 2,
#         'rating': 1
#     },
#     'Rena': {
#         'likes': 26,
#         'comments': 7,
#         'rating': 2
#     }
# }

# list_ = sum([v['likes'] for v in dict_.values() if v['rating'] > 3])

# print(list_)
'-------------------------------------------------------------------------'
# 35)
# dict_ = {
#     'Dasha': {
#         'likes': 15,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#         ],
#         'rating': 2
#     },
#     'Luna': {
#         'likes': 12,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#         ],
#         'rating': 1
#     },
#     'Rena': {
#         'likes': 26,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#             {'id': 4, 'text': 'some text'},
#             {'id': 5, 'text': 'some text'},
#             {'id': 6, 'text': 'some text'},
#         ],
#         'rating': 2
#     }
# }

# list_ = [v2['id']for v in dict_.values() for v2 in v['comments'] if len(v['comments']) > 3]
# print(list_)
'-------------------------------------------------------------------------'
# 36)
# list_ = [x/2 for x in range (0, 11) if x % 2 == 0]
# print(list_)
'-------------------------------------------------------------------------'
# 37)
# dict_ = { 1 : 'asd', 2 : 'qwgfe', 3 : 'zxca', 4 : 'fghjkl', 5 : 'tyhjklkjhbv' }
# dict_ = { k : len(v) if k % 2 == 0 else len(v)**3 for k, v in dict_.items()}
# print(dict_)
'-------------------------------------------------------------------------'
# 38)
# set1 = {x for x in range(10)}
# set2 = {a for a in range(8,18)}
# full_set = set1.union(set2)
# if len(full_set) < 20:
#     print(f'В этом сете было {20-len(full_set)} повторения, его длина составляет {len(full_set)}')
# elif len(full_set) == 20:
#     print("Ваш объединенный сет полностью уникальный!")
'-------------------------------------------------------------------------'
'Dictionary'
# 1)
# a = {'x': 1, 'y': 2, 'z': 1}
# print(list(a.keys())[0])
'-------------------------------------------------------------------------'
# 2)
# a = {'a': 1, 'b': 2, 'c': 1}
# print(a)
# removed = a.pop('a')
# print(removed)
'-------------------------------------------------------------------------'
# 3)
# a = {'a': 1, 'b': 2, 'c': 1}
# a.update( {'f': 55})
# print(a)
'-------------------------------------------------------------------------'
# 4)
# a = {'a': 1, 'b': 2, 'c': 1}
# a.clear()
# print(a)
'-------------------------------------------------------------------------'
# 5)
# a = {'a': 1, 'b': 2, 'c': 1}
# b = []
# for k,v in a.items():
#     b.append(k)
# print(b)
'-------------------------------------------------------------------------'
# 6)
# a = {'a': 1, 'b': 2, 'c': 1}
# b = a.copy()
# print(b)
'-------------------------------------------------------------------------'
# 7)
# a = {'a': 1, 'b': 2, 'c': 1}
# for x in a.keys():
#     print(x)
'-------------------------------------------------------------------------'
# 8)
# a = {'a': 1, 'b': 2, 'c': 1}
# for x in a.values():
#     print(x)
'-------------------------------------------------------------------------'
# 9)
# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
# b = {}
# for k, v in a.items():
#     if v%2==0:
#         b.setdefault(k, 2)
#     else:
#         b.setdefault(k,v)
# print(b)
'-------------------------------------------------------------------------'
# 10)
# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# a = {key:value for (key, value) in a.items() if value}
# print(a)
'-------------------------------------------------------------------------'
# 11)
# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
# c = {}
# for k, v in a.items():
#     b = v / 5
#     c.setdefault(k,b)
# print(c)
'-------------------------------------------------------------------------'
# 12)
# a = {'apple': 2, 'orange': 5, 'banana': 10}
# for k, v in list(a.items()):
#     if v % 2 == 0:
#         del a[k]
        
# print(a)
'-------------------------------------------------------------------------'
# 13)
# a = {'a': 1, 'b': 2, 'c': 3}
# b = {} 
# for k,v in a.items():
#     b.setdefault(v,k)
# print(b)
'-------------------------------------------------------------------------'
# 14)
# a = {'a': 3, 'b': 2}
# print(sum(a.values()))
'-------------------------------------------------------------------------'
# 15) 1 пример
# a1=dict(a=1, b=2, c=3)
# a2=dict([('d', 4),('e', 5),('f', 6)])
# a3=dict([('a', 1)], b=2, c=3)
# a4=dict({'a' : 1, 'b' : 2}, c=3)
# print(a1)
# print(a2)
# print(a3)
# print(a4)

# 2 пример
# a1 = {"a": 1,"b": 2,"v": 3}
# a2 = dict(a=1, b=2, c=3)
# a3 = {}
# for k,v in a1.items():
#     a3.setdefault(k, v)
# print(a1)
# print(a2)
# print(a3)
'-------------------------------------------------------------------------'
# 16)
# dict_ = {'x': 1, 'y': 2, 'z': 1}
# print(dict_.get('x'))
'-------------------------------------------------------------------------'
# 17)
# dict_ = {'a': 1, 'b': 2, 'c': 1}
# del dict_['a']
# print(dict_)
'-------------------------------------------------------------------------'
# 18)
# dict_ = {'a': 1, 'b': 2, 'c': 1}
# print(dict_.items())
'-------------------------------------------------------------------------'
# 19)

'-------------------------------------------------------------------------'
# 20)
# dict_ = {'a': 32, 'b': 56, 'c': 37, 'd': 21}
# min_val = min(dict_.values())
# print(min_val)
'-------------------------------------------------------------------------'
# 21)
# dict1 = {'a': 3, 'b': 4, 'c': 9, 'd': 5, 'e': 6}
# dict2 = {}
# for k,v in dict1.items():
#     if v%2!=0:
#         dict2.setdefault(k,1)
#     else:
#         dict2.setdefault(k,v)
# print(dict2)
'-------------------------------------------------------------------------'
# 22)
# dict_ = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# dict_2 = {}
# for k,v in dict_.items():
#     if v == None:
#         dict_2.setdefault(k,v)
#     dict_.clear
#     dict_ = dict_2
# print(dict_)
'-------------------------------------------------------------------------'
# 23)
# dict1 = {25: 'apple', 26: 'orange', 27: 'banana'}
# dict2 = {}
# for k,v in dict1.items():
#     dict2.setdefault(k**2,v)
# print(dict2)
'-------------------------------------------------------------------------'
# 24)
# list_ = ['Bootcamp', 'Makers', 'coding', 'hello']
# dict_ = {}
# for k in list_:
#     dict_.setdefault(k,len(k))
# print(dict_)
'-------------------------------------------------------------------------'
# 25)
# dict_ = {'Bootcamp': 8, 'Makers': 6, 'coding': 6, 'hello': 5}
# max_ = max(dict_.values())
# for k in dict_.keys():
#     if dict_[k] == max_:
#         print(k)
'-------------------------------------------------------------------------'
# 26)
# dict1 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
# dict2 = {}
# for k,v in dict1.items():
#     dict2.setdefault(k,k**3)
# print(dict2)
'-------------------------------------------------------------------------'
# 27)
# dict_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}
# for k,v in list(dict_.items()):
#     for v2 in v.values():
#         dict_[k] = v2
# print(dict_)
'-------------------------------------------------------------------------'
# 28)
# dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
# dict2 = {}
# for k,v in list(dict1.items()):
#     res = 1
#     for j in v.values():
#         res = res * j
#     dict2[k] = res

# print(dict2)
'-------------------------------------------------------------------------'
# 29)
# list_ = ['hello', 23, 56, 'world', 928, 'Makers', 456, 'word', 223, 89, 'bootcamp', 'coding']
# list1 = []
# list2 = []
# dict_ = {}
# for k in list_:
#     if type(k)==str:
#         list1.append(k)
#     if type(k) == int:
#         list2.append(k)
# dict_ = dict(zip(list1, list2))
# print(dict_)
'-------------------------------------------------------------------------'
# 30)
# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_values = sorted(dict_.values())
# sorted_dict = {}
# for i in sorted_values:
#     for k in dict_.keys():
#         if dict_[k] == i:
#             sorted_dict[k] = dict_[k]
#             break
# print(sorted_dict)
'-------------------------------------------------------------------------'
# 31)
# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_values = sorted(dict_.values(), reverse = True)
# sorted_dict = {}
# for i in sorted_values:
#     for k in dict_.keys():
#         if dict_[k] == i:
#             sorted_dict[k] = dict_[k]
#             break
# print(sorted_dict)
'-------------------------------------------------------------------------'
# 32)
# dict_ = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# key = input()
# if key in dict_:
#     print("Key is present in the dictionary")
# else:
#     print("Key is not present in the dictionary")
'-------------------------------------------------------------------------'
# 33)
# dict1 = {1:10, 2:20}
# dict2 = {3:30, 4:40}
# dict3 = {5:50, 6:60}
# dict4={}
# dict4.update(dict1)
# dict4.update(dict2)
# dict4.update(dict3)
# print(dict4)
'-------------------------------------------------------------------------'
# 34)
# list1 = [1, 2, 3, 4, 5, 6, 7]
# list2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
# dict_ = {}
# for i in range(len(list1)):
#     dict_[list1[i]] = list2[i]
# print(dict_)
'-------------------------------------------------------------------------'
# 35)
# dict_ = { 'math': { 'sum': sum }, 'vars': { 'a': 5, 'b': 20, 'c': 50 } }
# res = dict_.get('vars')
# for k, v in dict_.items():
#     for j in v.values():
#         if type(j) != int:
#             print(j(res.values()))
'-------------------------------------------------------------------------'
# 36)
# a = {'a': 10, 'b': 9, 'c': 3}
# result = 1
# for key in a:
#     result = result * a[key]
# print(result)
'-------------------------------------------------------------------------'
# 37)
# string = "pythonist"
# dict_ = {}
# for i in list(string):
#     dict_.setdefault(i, list(string).count(i))
# print(dict_)
'-------------------------------------------------------------------------'
'Try-except'
# 1)
'первый способ'
# try:
#     print("text")
# except:
#     print("none code")
# else:
#     print("none code")
# finally:
    # print("the end")


'второй способ'
# try:
#     pass
# except Exception:
#     pass
# else:
#     pass
# finally:
#     pass
'-------------------------------------------------------------------------'
# 2)
# try:
#     b = 10
#     c = 11
#     print(a)
# except:
#     print('Такой переменной не существует!')
'-------------------------------------------------------------------------'
# 3)
# try:
#     num1 = int(input())
#     num2 = int(input())
#     print(num1/num2)
# except ZeroDivisionError:
#     print('На ноль делить нельзя')
'-------------------------------------------------------------------------'
# 4)
# try:
#     num1 = int(input('Enter: '))
#     num2 = int(input('Enter: '))
#     res = num1+num2
# except ValueError:
#     print('Введите число!')
# else:
#     print(res)
'-------------------------------------------------------------------------'
# 5)
# dict_ = {'key1': 'value1', 'key2': 'value2'}
# try:
#     print(dict_['key1'])
# except KeyError:
#     print('Нет такого ключа!')
'-------------------------------------------------------------------------'
# 6)
# list_ = [1, 4, 9, 16, 25, 36]
# try:
#     print(list_[3])
# except:
#     print('Нет такого элемента!')
'-------------------------------------------------------------------------'
# 7)
# try:
#     age = int(input())
#     if age < 18:
#         raise ValueError('Доступ запрещён')
# except:
#     print('Введён некорректный возраст')
# else:
#     print('Спасибо')
# finally:
#     print('До свидания!')
'-------------------------------------------------------------------------'
# 8)
# try:
#     num1 = int(input())
#     num2 = int(input())
#     print(num1/num2)
# except (ValueError, ZeroDivisionError) as error:
#     print('Произошла ошибка!')
'-------------------------------------------------------------------------'
# 9)
# try:
#     cash = int(input())
#     if cash < 0:
#         raise Exception ('ValueError')
#     print(cash)
# except:
#     print('Сумма не может быть отрицательной!')
'-------------------------------------------------------------------------'
# 10)
# list_ = [1, 2, 3]
# try:
#     print(list_.get(1))
# except AttributeError:
#     print(list_[1])
'-------------------------------------------------------------------------'
# 11)
# try:
#     string = 'sdgsg'
#     num = 9
#     sum = string + num
#     print(sum)
# except TypeError:
#     print('Unsupported option')
'-------------------------------------------------------------------------'
# 12)
# try:
#     for x in range(10):
#         list_.append(x)
# except NameError:
#     print([0,1,2,3,4,5,6,7,8,9])
'-------------------------------------------------------------------------'
# 13)
# list_ = [1, 2, 3, 4]
# try:
#     for i in range(0, len(list_) + 1):
#         print(list_[i])
# except IndexError:
#     for i in range(0, len(list_)):
#         print(list_[i])
'-------------------------------------------------------------------------'
# 14)
# try:
#     password = 'short'
#     if len(password) < 6:
#         raise ValueError()
# except ValueError:
#     raise ValueError
'-------------------------------------------------------------------------'
# 15)
# warehouse = [
#     [],
#     [],
#     [[], [], []],
#     [[], [], {}],
# ]
# for i in warehouse:
#     if len(warehouse)>6 or len(i)>3:
#         raise ValueError()
'-------------------------------------------------------------------------'
# 16)
# def to_fahrenheit(k:int) -> float:
#     assert k>=0,'Холоднее абсолютного нуля!'
#     res=(k-273.15)*9/5+32
#     return res
# print(to_fahrenheit(3))
'-------------------------------------------------------------------------'
# 17)
# try:
#     import lamabimgo
# except ModuleNotFoundError:
#     print('Такого модуля нет')
'-------------------------------------------------------------------------'
# 18)
# def filter_comment(comment:str,banlist:list)->None:
#     for x in range(0,len(banlist)):
#         if banlist[x] in comment.lower():
#                 c=[1,2]
#                 c[0]=comment.lower().index(banlist[x])-1 if comment.lower().index(banlist[x])!=0 else comment.lower().index('!')
#                 c[1]=comment.lower().index(banlist[x])+len(banlist[x]) if comment.lower().index(banlist[x])+len(banlist[x])!=len(comment) else comment.lower().index('!')
#                 if not comment.lower()[c[0]].isalnum() and not comment.lower()[c[1]].isalnum():
#                     raise ValueError('Ваш комментарий отправлен на перепроверку, так как, возможно, содержит неблагоприятный контекст')
'-------------------------------------------------------------------------'
# 19)
# try:
#     num = 100_000_000
#     for i in range(0, num):
#         print('Nope')
# except KeyboardInterrupt:
#     print('Nope')
'-------------------------------------------------------------------------'
# 20)
# def collect_all_possibles(list_: list, num: int) -> list:
#     result = []
#     for x in list_:
#         try:
#             result.append(x*num)
#             result.append(x+num)
#             result.append(x-num)
#             result.append(x**num)
#             result.append(x//num)
#         except TypeError:
#             continue
#     return result
'-------------------------------------------------------------------------'
# 21)
# try:
#     inp1 = input('enter1: ')
#     inp2 = input('enter2: ')
#     print(int(inp1) + int(inp2))
# except:
#     print(inp1+inp2)
'-------------------------------------------------------------------------'
# 22)
# inp1 = input()
# res = inp1.split(' ')
# try:
#     list_=[int(x)
#     for x in res]
# except ValueError:
#     raise ValueError('Данный элемент не является числом!')
'-------------------------------------------------------------------------'
'Function(функции)'
# 1)
# def add(x, z):
#     return x + z
# print(add(2,4))
'-------------------------------------------------------------------------'
# 2)
# def get_string_length(str):
#     return len(str)
# print(get_string_length('hello'))
'-------------------------------------------------------------------------'
# 3)
# def get_type(x,y):
#     print(f'{type(x)}\n{type(y)}')
# get_type(5,'s')
'-------------------------------------------------------------------------'
# 4)
# def divide(a, b):
#     return a/b
# print(divide(24, 5))
'-------------------------------------------------------------------------'
# 5)
# dict_ = {}
# def dictionary(dict_):
#     for k,v in dict_.items():
#         print(k)
'-------------------------------------------------------------------------'
# 6)
# num = 6
# def check(num):
#     if num % 2 == 0:
#         return ("It is even number")
#     else:
#         return ("It is odd number")
'-------------------------------------------------------------------------'
# 7)
# def is_palindrome(str):
#         if str.lower() == str.lower()[::-1]:
#             return True
#         else:
#             return False
# print(is_palindrome('довод'))
'-------------------------------------------------------------------------'
# 8)
# def max_num(x, y):
#     return max(x, y)
# print(max_num(10, 12))
'-------------------------------------------------------------------------'
# 9)
# def multiply_list(list_):
#     n = 1
#     for i in list_:
#         n *= i
#     return n
# print(multiply_list([1, 2, 3, 4, 5, 6]))
'-------------------------------------------------------------------------'
# 10)
# def sum_digits(num):
#     return(sum([int(x) for x in str(num)]))
# print(sum_digits(105))
'-------------------------------------------------------------------------'
# 11)
# def func11(a,b,c):
#     if c!=0:
#         return (a+b)/c
#     else:
#         return (a+b)
# print(func11(5,6,0))
'-------------------------------------------------------------------------'
# 12)
'не правильный'
# def func12(words: list[str]):
#     return list(x.upper() for x in words)
    
# print(func12(["hEllo", 'wORld']))

'правильное способ решения'
# def func12(list1, b):
#     a = []
#     for i in list1:
#         if b == 'lower':
#             a.append(i.lower())
#         elif b == 'upper': 
#             a.append(i.upper())
#     return (a)

# func12(["hEllo", "wORld"], 'lower')
'-------------------------------------------------------------------------'
# 13)
# def func13(str):
#     return {x:str.count(x)
#     for x in str}
# print(func13("Hello"))
'-------------------------------------------------------------------------'
# 14)
# def add_(a, b):
#     return a + b
# def sub_(a, b):
#     return a - b
# def mult_(a, b):
#     return a * b
# def div_(a, b):
#     return a / b
# def calc(num1,num2, operation):
#     if operation == "+":
#         return add_(num1, num2)
#     elif operation == "-":
#         return sub_(num1, num2)
#     elif operation == "*":
#         return mult_(num1, num2)
#     elif operation == "/":
#         return div_(num1, num2)
# print(calc(40, 20, operation = "+"))
'-------------------------------------------------------------------------'
# 15)
# users = [
#   { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer' },
#   { 'name': 'Helen', 'age': 35, 'work': 'Nurse' },
#   { 'name': 'Bob', 'age': 35, 'work': 'Driver' },
#   { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer' },
#   { 'name': 'Helga', 'age': 35, 'work': 'IT-HR' }
# ]

# def func15(users):
#     for i in users: 
#         if i['work'].startswith('IT'):
#             print(f"{i['name']}, скидки в магазине компьютерной техники!")

# func15(users)
'-------------------------------------------------------------------------'
# 16)
# def func16(km, v):
#     return(f'На 100км. было расходовано {round(100*v/km)}л горючего')
# print(func16(50,8))
'-------------------------------------------------------------------------'
# 17)
# def func17(list_):
#     res = []
#     for i in list_:
#         i['salary'] = i['salary'] + i['overTime']*200
#         i.popitem()
#     return list_
# employees = [
#   {'name': 'Jack', 'salary': 10000, 'overTime': 4},
#   {'name': 'Tom', 'salary': 15000, 'overTime': 3},
#   {'name': 'Jessica', 'salary': 20000, 'overTime': 9},
#   {'name': 'Helen', 'salary': 25000, 'overTime': 2},
#   {'name': 'Peter', 'salary': 30000, 'overTime': 7}
# ]
# print(func17(employees))
'-------------------------------------------------------------------------'
# 18)
# def func18(gax):
#     str_list = [x for x in gax if str == type(x)]
#     num_list = [x for x in gax if int == type(x)]
#     return num_list, str_list
'-------------------------------------------------------------------------'
# 19)
# students = [
#   {'student': 'Jack', 'marks': 43},
#   {'student': 'Tom', 'marks': 92}, 
#   {'student': 'Helen', 'marks': 85}, 
#   {'student': 'Peter', 'marks': 58},
#   {'student': 'Jessica', 'marks': 78}
# ]

# def func19(list_:list):
#     list_.sort(key=lambda x:x['marks'],reverse=True)
#     return list_
    
# print(func19(students))
'-------------------------------------------------------------------------'
# 20)
# products = [
#   {
#     'title': 'Samsung S10', 
#     'price': 800, 
#     'count': 6, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 13 Pro', 
#     'price': 1200, 
#     'count': 9, 
#     'category': 'apple'},
#   {
#     'title': 'Xiaomi Mi 10', 
#     'price': 500, 
#     'count': 2, 
#     'category': 'xiaomi'},
#   {
#     'title': 'Samsung S9', 
#     'price': 600, 
#     'count': 4, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 11', 
#     'price': 850, 
#     'count': 1, 
#     'category': 'apple'}
# ]

# def func20(a:list,b:str) -> list:
#     result = list()
#     for i in a:
#         if b.lower() in i['title'].lower():
#             result.append(i)
            
#     return result
'-------------------------------------------------------------------------'
# 21)
# products = [
#   {
#     'title': 'Samsung S10', 
#     'price': 800, 
#     'count': 6, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 13 Pro', 
#     'price': 1200, 
#     'count': 9, 
#     'category': 'apple'},
#   {
#     'title': 'Xiaomi Mi 10', 
#     'price': 500, 
#     'count': 2, 
#     'category': 'xiaomi'},
#   {
#     'title': 'Samsung S9', 
#     'price': 600, 
#     'count': 4, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 11', 
#     'price': 850, 
#     'count': 1, 
#     'category': 'apple'}
# ]

# def func21(a:list,b:str) -> list:
#     result=list()
#     for i in a:
#         if b.lower() == i['category'].lower():
#             result.append(i)
            
#     return result
'-------------------------------------------------------------------------'
# 22)
# balance = 1_000
# def spent(a, b, c):
#     if c - b >= 0:
#         c -= b
#         return ({'target': a, 'spend': b}, c)
#     else:
#         return 'Недостаточно средств'
# print(spent('neger', 20000, balance))

# def deposit(a, b):
#         b += a
#         return b
'-------------------------------------------------------------------------'
# 23)
# database = list()
# def create(db:list, title:str, price:int, category:str) -> list:
#     db.append({'title': title, 'price': price,'category': category})
#     return db
# def read(db:list) -> list:
#     print(db)
#     return db
# def update(db:list, index:int, title:str, price:int, category:str) -> list:
#     db[index]['title'] = title
#     db[index]['price'] = price
#     db[index]['category'] = category
#     return db
# def delete(db,index):
#     db.pop(index)
#     return db
'-------------------------------------------------------------------------'
'Области видимости(scopes)'
# 1
# var = 'переменная в foo'
# def foo():
#     global var
#     var = 'переменная foo' 
#     print('переменная в foo: ', var)
#     def bar():
#         global var
#         var = 'переменная bar'
#     bar()
# foo()
# print('переменная в foo: ', var)
'-------------------------------------------------------------------------'
# 2)
# x = "Я глобальная переменная!"
# def my_func():
#     global x
#     print(x)
#     x = "Я могу изменяться"

# my_func()
# print(x)
'-------------------------------------------------------------------------'
# 3)
# num = 3
# def mul():
#     global num
#     num = num**2

# mul()
# mul()
# mul()
# print(num)
'-------------------------------------------------------------------------'
# 4)
# balance = 0
# def get_salary(amount):
#     global balance
#     balance = balance + amount
# def pay_bills(amount, long_name):
#     global balance
#     balance = balance - amount
#     print(f'Вы заплатили {amount} сом за {long_name}')
#     return balance
# def get_balance():
#     global balance
#     print(f'У вас на счету {balance} сом')

# get_salary(1000)
# get_balance()
# pay_bills(400, 'кабельное тв')
# get_balance()
'-------------------------------------------------------------------------'
# 5)
# result = 0
# def pow_first(x,y):
#     global result
#     result = pow(x, y)
# def pow_second(z):
#     global result
#     result = result % z

# pow_first(2, 3)
# pow_second(3)
# print(result)
'-------------------------------------------------------------------------'
# 6)
# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}
# def age():
#     global a
#     for k, v in a.items():
#         if v >= 17:
#             print(f"{k}, Вы можете войти в клуб")
#         else:
#             print(f"{k}, извините, Вы не проходите по age-control")
            
# age()
'-------------------------------------------------------------------------'
# 7)
# a = ['father', 'mother' 'brother', 'sister']
# b = []
# for i in a: b.append(i.capitalize())
# print(b)
'-------------------------------------------------------------------------'
# 8)
# def count_symbols(word):
#     glasnye = 0
#     soglasnye = 0
#     ostalnye = 0
#     for letter in word:
#         if letter.lower() in 'аяуюоеёэиы':
#             glasnye += 1
#         elif letter.lower() in 'бвгджзйклмнпрстфхцчшщ':
#             soglasnye += 1
#         else:
#             ostalnye += 1
#     return (f'Количество гласных: {glasnye}, согласных: {soglasnye}, остальных символов: {ostalnye}')
# print(count_symbols('Мурат супер!'))
'-------------------------------------------------------------------------'
# 9)
# a = [x for x in range(0,11)]
# print(a)
'-------------------------------------------------------------------------'
# 10)
# a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]
# def lower_7():
#     b = []
#     global a
#     for i in a:
#         if i < 7:
#             b.append(i)
#     return b
# print(lower_7)
'-------------------------------------------------------------------------'
'Логическая выражения'
# 1)
# number = int(input())
# if number >= 0:
#     print(True)
# else:
#     print(False)
'-------------------------------------------------------------------------'
# 2)
# string = 'Here, there everywhere'
# if len(string) > 5:
#     print(True)
# else:
#     print(False)
'-------------------------------------------------------------------------'
# 3)
# mark = int(input())
# if mark >= 90:
#     print('Отлично, Ваша оценка 5!')
# elif mark >= 80:
#     print('Здорово, Ваша оценка 4!')
# elif mark >= 70:
#     print('Хорошо, Ваша оценка 3!')
# elif mark >= 60:
#     print('Вам стоит подучить материал')
# else:
#     print('Вы не сдали экзамен')
'-------------------------------------------------------------------------'
# 4)
# number = int(input('Type your number:'))
# if number < 0:
#     print('negative')
# elif number > 0:
#     print('positive')
# elif number == 0:
#     print('zero')
'-------------------------------------------------------------------------'
# 5)
# x = 42
# y = 24
# if x > y:
#     print(y)
# elif x < y:
#     print(x)
'-------------------------------------------------------------------------'
# 6)
# x = 102
# y = 36
# z = 90
# if x < y and x < z:
#     print(x)
# elif y < x and y < z:
#     print(y)
# else:
#     print(z)
'-------------------------------------------------------------------------'
# 7)
# x = 32
# y = 32
# z = 100
# if x == y and y == z and x == z:
#     print('3')
# elif x == y or y == z or x == z:
#     print('2')
# else:
#     print('0')
'-------------------------------------------------------------------------'
# 8)
# x = int(input())
# y = int(input())
# if x % y == 0:
#     print('x делится на y')
#     d = x // y
#     print(f'Частное: {d}')
# else:
#     print('x не делится на y')
#     a = x // y
#     print(f'Частное: {a}')
#     b = x % y
#     print(f'Остаток: {b}')
'-------------------------------------------------------------------------'
# 9)
# year = int(input())
# if year % 4 == 0 and year % 100 != 0:
#     print('YES')
# elif year % 400 == 0:
#     print('YES')
# else:
#     print('NO')
'-------------------------------------------------------------------------'
# 10)
# nums = [1, 15, 36, 88]
# target = 25
# if target in nums:
#     print('Да')
# else:
#     print('Нет')
'-------------------------------------------------------------------------'
# 11)
# num = chr(int(input()))
# if num.isalpha():
#     print(f'Это буква "{num}"')
# else:
#     print(f'Это не буква, а символ "{num}"')
'-------------------------------------------------------------------------'
# 12)
# greeting = input()
# if 'Hi' in greeting:
#     print("Привет!")
# else:
#     print("NO")
'-------------------------------------------------------------------------'
# 13)
# count  = 0
# number = input()
# if number.isdigit():
#     count = int(number)
# print(count)
'-------------------------------------------------------------------------'
# 14)
# lang = 'en'
# if 'en' in lang:
#     print('This is english')
# elif 'ru' in lang:
#     print('Это русский')
# elif 'de' in lang:
#     print('Das ist Deutsch')
# elif 'kg' in lang:
#     print('Бул кыргыз тили')
'-------------------------------------------------------------------------'
# 15)
# string = "234234"
# if int(string[0])+int(string[1])+int(string[2])==int(string[3])+int(string[4])+int(string[5]):
#     print('да')
# else:
#     print('нет')
'-------------------------------------------------------------------------'
# 16)
# a = int(input())
# b = int(input())
# c = int(input())
# if a <= b and a <= c and b <= c:
#     print(a,b,c)
# elif a <= c and a <= b and c <= b:
#     print(a,c,b)
# elif b <= a and b <= c and a <= c:
#     print(b,a,c)
# elif b <= c and b <= a and c <= a:
#     print(b,c,a)
# elif c <= a and c <= b and a <= b:
#     print(c,a,b)
# elif c <= b and c <= a and b <= a:
#     print(c,b,a)
# else:
#     print(a,b,c)
'-------------------------------------------------------------------------'
# 17)
# age = int(input())
# if age < 18:
#     print('Доступ запрещен')
# else:
#     print('Добро пожаловать')
'-------------------------------------------------------------------------'
# 18)
# month = int(input())
# if month > 12:
#     print("Такого месяца нет")
# elif month <= 12 and month == 12 or month == 1 or month == 2:
#     print("зима")
# elif month <= 12 and month == 3 or month == 4 or month == 5:
#     print("весна")
# elif month <= 12 and month == 6 or month == 7 or month == 8:
#     print("лето")
# elif month <= 12 and month == 9 or month == 10 or month == 11:
#     print("осень")
'-------------------------------------------------------------------------'
# 19)

'-------------------------------------------------------------------------'
# 20)

'-------------------------------------------------------------------------'
# 21)
# a1 = int(input())
# b1 = int(input())
# c1 = int(input())
# c = max(a1, b1, c1)
# b = min(a1, b1, c1)
# a = sum([a1, b1, c1]) - min(a1, b1, c1) - max(a1, b1, c1)
# if c >= a + b:
#     print('impossible')
# elif c**2 == a**2 + b**2:
#     print('rectangular')
# elif c**2 < a**2 + b**2:
#     print('acute')
# elif c**2 > a**2 + b**2:
#     print('obtuse')
'-------------------------------------------------------------------------'
# 22)
# n = 100
# if n >= 11 and n <= 14:
#     print(f'На лугу пасется {n} коров')
# else:
#     temp = n % 10
#     if temp == 0 or (temp >= 5 and temp <= 9):
#         print(f'На лугу пасется {n} коров')
#     if temp == 1:
#         print(f'На лугу пасется {n} корова')
#     if temp >=2 and temp <=4:
#         print(f'На лугу пасется {n} коровы')
'-------------------------------------------------------------------------'
# 23)
# a = int(input('Количество учеников в классе: '))
# if a % 2 == 0:
#     print('второй')
# else:
#     print('первый')
'-------------------------------------------------------------------------'
# 24)
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if x1 == x2 or y1 == y2:
#     print('YES')
# else:
#     print('NO')
'-------------------------------------------------------------------------'
# 25)

'-------------------------------------------------------------------------'
'Списки (цикл for)'
# 1)

'-------------------------------------------------------------------------'
# 2)
# labels = ['Honda', 'Kawasaki']
# for x in labels:
#     print('I like brand', '' + x)
'-------------------------------------------------------------------------'
# 3)
# name_of_list = ['ьечноств']
# new_list = name_of_list[0]
# i = len(new_list)
# if i % 2 == 0:
#     new_list = name_of_list[0] [i // 2:] + name_of_list[0] [:i // 2]
# else:
#     new_list = name_of_list[0] [i // 2 + 1:] + name_of_list[0] [:i // 2 + 1]

# print(list(new_list))
'-------------------------------------------------------------------------'
# 4)

'-------------------------------------------------------------------------'
# 5)

'-------------------------------------------------------------------------'
# 6)

'-------------------------------------------------------------------------'
# 7)

'-------------------------------------------------------------------------'
# 8)

'-------------------------------------------------------------------------'
# 9)
# list_ = [1, 2, 3, 4, 5]
# new_list = []
# for x in list_:
#     if x % 2 == 0:
#         x = 'четное'
#         new_list.append(x)
#     elif x % 2 != 0:
#         x = 'нечетное'
#         new_list.append(x)
    
# print(new_list)
'-------------------------------------------------------------------------'
# 10)

'-------------------------------------------------------------------------'
# 11)

'-------------------------------------------------------------------------'
# 12)

'-------------------------------------------------------------------------'
# 13)

'-------------------------------------------------------------------------'
# 14)

'-------------------------------------------------------------------------'
# 15)

'-------------------------------------------------------------------------'
# 16)

'-------------------------------------------------------------------------'
# 17)

'-------------------------------------------------------------------------'
# 18)

'-------------------------------------------------------------------------'
# 19)

'-------------------------------------------------------------------------'
# 20)

'-------------------------------------------------------------------------'
# 21)

'-------------------------------------------------------------------------'
# 22)
# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]

# max_ = max([x for x in lists], key=len)
# min_ = None
# if len(lists) > 1: min_ = min([x for x in lists],key=len)
# if max_ == min_:
#     min_ = None
    
# print(f'max_list {max_}')
# print(f'min_list {min_}')
'-------------------------------------------------------------------------'
# 23)
'первый способ'
# step = 3
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# list1 = [list_[i::step] for i in range(len(list_))][:step] # if i < step
# print(list1)

'второй способ'
# step = 3
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# list1 = [list_[i::step] for i in range(len(list_)) if i < step]

# print(list1)
'-------------------------------------------------------------------------'
# 24)
# size = 3
# list_ = []
# for i in range(size): # => [ [], [], [] ] 0, 1, 2
#     list_.insert(i, list(range(1, size+1)))
# print(list_)
'-------------------------------------------------------------------------'
# 25)
# inp = input()
# list_ = ['sun', 'flowers', 'rumor', 'stranger', 'adventure', 'architect', 'accompany', 'abandon', 'cartoon']
# list_1 = []
# for i in list_:
#     if i.startswith(inp):
#         list_1.append(i)

# print(list_1)
'-------------------------------------------------------------------------'
# 26)
# colors1 = ["red", "orange", "green", "blue", "white"]
# colors2 = ["black", "yellow", "green", "blue"]
# resc1=[]
# resc2=[]
# for i in colors1:
#     if not i in colors2:
#         resc1.append(i)
# for k in colors2:
#     if not k in colors1:
#         resc2.append(k)
# print(resc1,resc2)
'-------------------------------------------------------------------------'
# 27)
'второй способ'
# list1 = [1,2,3,4,5] 
# list2 = [5,6,7,8,9] 
# res = None
# for i in list1: 
#     for j in list2: 
#         if i==j: 
#             res = True 
#             break
#         else: 
#             res = False
# print(res)

'второй, короткий способ'
# list1 = [1,2,3,4,5] 
# list2 = [5,6,7,8,9] 
# if set(list1).intersection(set(list2)):
#     print(True)
# else:
#     print(False)
'-------------------------------------------------------------------------'
# 28)
# list_ = [4, 6, 4, 3, 3, 8, 4, 3, 4, 3, 8, 8]
# repeats = 3

# res = []

# for i in list_:
#     if list_.count(i) >= repeats and i not in res:
#         res.append(i)

# print(res)
'-------------------------------------------------------------------------'
# 29)
# from itertools import permutations
# list_ = [1, 2, 3]
# comb = permutations(list_)

# for i in comb:
#     print(i)
'-------------------------------------------------------------------------'
# 30)
'первый способ'
# K = 3
# list_ = []
# ls = [0]
# for i in range(K):
#     list_.insert(i, ls*K)
# print(list_)

'второй способ'
# K = 3 
# list1 = [] 
# list2 = [] 
# for i in range(K): 
#     list2.append(0) 
# for v in range(K): 
#     list1.append(list2) 
# print(list1)
'-------------------------------------------------------------------------'
# 31)
# colors = ["Red", "Green", "Blue", "White", "Black", "Yellow", "Orange"] 
# res = []
# for x in colors: 
#     res.append(x[::-1]) 
# print(sorted(res, key=len))

'второй способ'
# colors = ["Red", "Green", "Blue", "White", "Black", "Yellow", "Orange"] 
# colors.sort(key=len) 
# m = [i[::-1] for i in colors] 
# b = ','.join(m).split(',') 
# print(b)
'-------------------------------------------------------------------------'
# 32)
# list_ = [1,2,3,4,5,6,7,8,9,0]
# step = 2
# element = 'A'
# i = step
# while i < len(list_) + 1:
#     list_.insert(i, element)
#     i += step + 1

# print(list_)
'-------------------------------------------------------------------------'
# 33)
# lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
# max_ = max([x for x in lists], key = sum)
# print(max_)
'-------------------------------------------------------------------------'
# 34)
# list_ = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# repeated = []
# for i in list_:
#     if list_.count(i) > 1:
#         repeated.append(i)
        
# print(repeated)
'-------------------------------------------------------------------------'
# 35)

'-------------------------------------------------------------------------'
'Внутренние функции(Built-in functions)'
# 1)
# from functools import reduce

# list_ = [1, 2, 3, 4]  
# result = reduce(lambda a, b: a + b, list_)
# print(result)
'-------------------------------------------------------------------------'
# 2)
# list_ = [5, 8, 4, 6, 7] 
# result = all(int > 3 for int in  list_)
# print(bool(result))
'-------------------------------------------------------------------------'
# 3)
# list_ = [5, 8, 4, 6, 7]
# result = all(x > 0 for x in list_)
# print(not result)
'-------------------------------------------------------------------------'
# 4)
# list_ = [1, 2, 3, 4]
# result = list(map(lambda x: x ** 2, list_)) 
# print(result)
'-------------------------------------------------------------------------'
# 5)
# list_ = [1, 2, 3, 4]
# result = list(filter(lambda x: x.startswith('чётное'), list_))  
# print(result) 
'-------------------------------------------------------------------------'
# 6)
# list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni',]
# result = list(filter(lambda x: len(x) > 7, list_))
# print(result)
'-------------------------------------------------------------------------'
# 7)
# from functools import reduce

# list_ = [5, 6, 7, 8]
# result = reduce(lambda a, b: a * b, list_)
# print(result)
'-------------------------------------------------------------------------'
# 8)
# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2 = len(list(filter(lambda x: x % 2 == 0, list_)))
# list3 = len(list(filter(lambda x: not x % 2 == 0, list_)))
# result = f'even: {list2}, odd: {list3}'
# print(result)
'-------------------------------------------------------------------------'
# 9)
# list_ = [-1, 2, 3, 5, -3, 7]
# result = list(map(lambda x: True if x > 0 else False, list_))
# print(result)
'-------------------------------------------------------------------------'
# 10)
# from functools import reduce

# list_ = ['Paul', 'George', 'Ringo', 'John']
# result = reduce(lambda x, y: x if len(x) > len(y) else y, list_)
# print(result)
'-------------------------------------------------------------------------'
# 11)
# from functools import reduce

# list_= list(range(1,50))
# result = list(map(lambda x: 'Fizz' if x % 3 == 0 else 'Buzz', list_))
# print(result)
'-------------------------------------------------------------------------'
# 12)
'первый способ'
# from functools import reduce

# list_ = [1,2,3,4,5,6,7,8,9,0]
# result = reduce(lambda x, y: x if x > y else y, list_)
# print(result)

'второй и короткий способ'
# list_=[1,2,3]
# print(max(list_))
'-------------------------------------------------------------------------'
# 13)
# from functools import reduce

# list_ = [1, 2, 3, 4, 5, 6, 7]
# result = reduce(lambda x, y: x if not x > y else y, list_)
# print(result)
'-------------------------------------------------------------------------'
# 14)
# string = 'hello'
# result = tuple(enumerate(string))
# print(result)
'-------------------------------------------------------------------------'
# 15)
'первый способ'
# list_ = [-7, -2, 12, 32, 432, 23, 37, 11, 76, 0, -23, 45, -32, -56]
# result = list(map(lambda x: abs(x), list_))
# print(result)

'второй и короткий способ'
# list_ = [-7, -2, 12, 32, 432, 23, 37, 11, 76, 0, -23, 45, -32, -56]
# result = [abs(x) for x in list_]
# print(result)
'-------------------------------------------------------------------------'
# 16)
# list_ = ['hello', 123]
# result = list(map(lambda x: type(x), list_))
# print(result)
'-------------------------------------------------------------------------'
# 17)
# names = ['rauchel','john','peter','jessica','steven123','dandy34','kamest','potter']
# result = list(map(lambda x: f'{x} Python' if len(x) > 5 else f'{x} JavaScript', names))
# print(result)
'-------------------------------------------------------------------------'
# 18)
# list_ = ['123hello@gmail.com', '123', 'hello']
# result = list(map(lambda x: x if '@gmail.com' in x else 'Not valid email', list_))
# print(result)
'-------------------------------------------------------------------------'
# 19)
# string = 'hello'
# res = tuple(enumerate(string,1))
# print(res)
'-------------------------------------------------------------------------'
# 20)
# list1 = ['M', 'A', 'K', 'E', 'R', 'S']
# list2 = [236, 54, 33, 21, 89, 1]
# list3 = list(zip(list1,list2))
# print(list3)
'-------------------------------------------------------------------------'
# 21)
# list_ = [-7, -2, 12, 32, 432, 23, 37, 11, 76, 0, -23, 45, -32, -56]
# list1 = list(filter(lambda x: x > 0, list_))
# list2 = list(filter(lambda x: not x > 0, list_))
# result = list(zip(list1, list2))
# print(result)
'-------------------------------------------------------------------------'
# 22)
# list_ = [0.334, 23.3443, 43.4, -13.44, 22.03, -11.033, 267.993, -3.24]
# result = list(map(lambda y: round(y ** 2, 3), list_))
# print(result)
'-------------------------------------------------------------------------'
# 23)
# from functools import reduce

# list_ = ['a', 'n', 'n', 'a']
# res = reduce( lambda x, y: x + y, list_)
# if res == res[::-1]:
#     print('YES')
# else:
#     print('NO')
'-------------------------------------------------------------------------'
'Основы GIT'
# 1)
# Ctrl+Alt+T
'-------------------------------------------------------------------------'
# 2)
# mkdir test
# cd test
# git init
'-------------------------------------------------------------------------'
# 3)
# touch test.txt
# nano test.txt
# hello world
'-------------------------------------------------------------------------'
# 4)
# git add .
# git commit -m 'created test.txt'
'-------------------------------------------------------------------------'
# 5)
# git log
'-------------------------------------------------------------------------'
# 6)
# git remote add origin git@github.com:student123/MyRepo.git
'-------------------------------------------------------------------------'
# 7)
# git branch
'-------------------------------------------------------------------------'
# 8)
# git push origin master
'-------------------------------------------------------------------------'
# 9)
# touch test2.txt
# nano test2.txt
# python is the best
'-------------------------------------------------------------------------'
# 10)
# git add .
# git commit -m 'created test2.txt'
'-------------------------------------------------------------------------'
# 11)
# git push origin master
'-------------------------------------------------------------------------'
'Файлы'
# 1)
# file = open('task1.txt')
# for i in file.readlines(9):
#     print(i)
#     file.close()
'-------------------------------------------------------------------------'
# 2)
# with open('task2.txt', 'r') as file:
#     for l in file.readlines():
#         print(l)
'-------------------------------------------------------------------------'
# 3)
# with open('task3.txt', 'a+') as file:
#     file.write('0*1*2*3*4*5*6*7*8*9*')
#     file.seek(0)
#     print(file.read())
'-------------------------------------------------------------------------'
# 4)
# with open('task4.txt','r') as file:
#     print(len(file.readlines()))
'-------------------------------------------------------------------------'
# 5)
# with open('task5.txt', 'r') as f:
#     list_ = []
#     ful = f.read() 
# for i in ful.split(): 
#     list_.append(int(i)) 
# with open('task6.txt', 'x') as fw: 
#     fw.write(f'{min(list_)}-{max(list_)}')
'-------------------------------------------------------------------------'
# 6)
# def read_last(lines, filename):
#     with open(filename) as file:
#         list_ = file.readlines()
#         list_.reverse()
#         if len(list_) > lines:
#             i = 0
#             while i < lines:
#                 print(list_[i].replace('\n', ''))
#                 i += 1
#         else:
#             for i in list_:
#                 print(i.replace('\n', ''))
           

# read_last(9, 'article.txt')
'-------------------------------------------------------------------------'
# 7)
# def longest_words(filename:str):
#     with open(filename,'r') as file:
#         listData=file.readlines()
#         listData1=[]
#         for x in listData:
#             if '\n' in x:
#                 x=x.replace('\n','')
#             else:
#                 pass
#             if ' ' in x:
#                 var=x.split()
#                 listData1.extend(var)
#             else:
#                 listData1.append(x)
#         maximum=[]
#         for j in listData1:
#             if len(j)==len(max(listData1,key=len)):
#                 maximum.append(j)
#             else:
#                 pass
#         if len(maximum)==1:
#             print(maximum[0])
#         else:
#             print(maximum)
# longest_words('article.txt')
'-------------------------------------------------------------------------'
# 8)

'-------------------------------------------------------------------------'
# 9)

'-------------------------------------------------------------------------'
# 10)

'-------------------------------------------------------------------------'
# 11)

'-------------------------------------------------------------------------'
# 12)

'-------------------------------------------------------------------------'
# 13)

'-------------------------------------------------------------------------'
# 14)

'-------------------------------------------------------------------------'
'JSON'
# 1)
# import json

# file1 = open('task1.json')
# python_obj = json.loads(file1.read())
# file1.close()

# with open('task1.py', 'w') as file2:
#     file2.write(str(python_obj))
'-------------------------------------------------------------------------'
# 2)
# import json

# with open("task2.json","r") as file:
#     json_obj = file.read()
#     python_obj = json.loads(json_obj)

# print(json_obj)
'-------------------------------------------------------------------------'
# 3)
# import json

# python_obj = None
# json_obj = json.dumps(python_obj)

# print(json_obj)
'-------------------------------------------------------------------------'
# 4)
# import json

# json_obj = "null"
# python_obj = json.loads(json_obj)

# print(python_obj)
'-------------------------------------------------------------------------'
# 5)
# import json

# users = [
#     {
#         'name': 'John',
#         'last_name': 'Snow',
#         'age': 26,
#         'has_car': True,
#     },
#     {
#         'name': 'Sam',
#         'last_name': 'Bolt',
#         'age': 4,
#         'has_car': False,
#     }
# ]

# json_users = json.dumps(users)

# print(json_users)
'-------------------------------------------------------------------------'
# 6)
# import json

# json_products = '[{"title":"iphone","price":700,"rating":4.8},{"title":"asus","price":1300,"rating":3.9},{"title":"macbook pro","price":1500,"rating":4.9},{"title":"samsung","price":150,"rating":5.0}]'

# file = json.loads(json_products)
# for x in file:
#     if x["rating"] > 4:
#         print(x['title'])
'-------------------------------------------------------------------------'
# 7)
# import json

# with open('db.json') as file:
#     dict_ = json.load(file)
#     for product in dict_:
#         product["description"] = "..."
#     js_dict = json.dumps(dict_)

# with open('new_db.json', 'w') as f1:
#     f1.write(js_dict)
'-------------------------------------------------------------------------'
# 8)
# import json

# with open('db.json') as file:
#     list_ = json.load(file)
#     for product in list_:
#         for k in product.keys():
#             if product[k] == 3:
#                 list_.remove(product)
#     js_dict = json.dumps(list_)
            
# with open('new_db.json', 'w') as f1:
#     f1.write(js_dict)
'-------------------------------------------------------------------------'
# 9)
# import json

# def create_new(id: int, title: str, description: str, price: int, rating:float) -> None:
#     dict_={'id':id, 'title':title, 'description':description, 'price':price, 'rating':rating}
#     with open('db.json') as file:
#         res = json.load(file)
#         res.append(dict_)
#     with open('new_db.json', 'w') as f:
#         f.write(json.dumps(res))
        
# create_new(10, 'assa', 'asd', 12, 25.0)
'-------------------------------------------------------------------------'
# 10)
# import json

# def get_sorted(json_filename: str) -> list[dict]:
#     with open (json_filename) as file:
#         res = json.load(file)
#         res.sort(key = lambda x: x['rating'], reverse = True)
#     return res

# print(get_sorted('json_filename.json'))
'-------------------------------------------------------------------------'
# 11)

'-------------------------------------------------------------------------'
# 12)
# import json

# def search(name: str):
#     with open('db.json') as file:
#         python_list = json.load(file)
#         list_ = []
#     for k in python_list:
#         if name in k['title']:
#             list_.append(k)
#     return list_
                
# print(search('sus'))
'-------------------------------------------------------------------------'
# 13)
# import json

# def filter_by_price(price: int):
#     with open('db.json') as file:
#         python_list = json.load(file)
#         list_ = []
#         for k in python_list:
#             if k["price"] >= price:
#                 list_.append(k)
#         return list_
        
# print(filter_by_price(1000))
'-------------------------------------------------------------------------'
# 14)

'-------------------------------------------------------------------------'
'Html(Заголовки)'
# 1)
# <h1>Breaking Bad</h1>
# <h2>Storyline</h2>
# <br>
# <h2>Episodes</h2>
# <h2>Cast</h2>
'-------------------------------------------------------------------------'
# 2)
# <h1>
#   Breaking Bad
# </h1>
# <br>
# <br>
# <h2>
#   Storyline
# </h2>
# <br>
# <h2>
#   Episodes
# </h2>
# <br>
# <h2>
#   Cast
# </h2>
# <br>
'-------------------------------------------------------------------------'
# 3)
# <!-- The IMDB series card -->
# <h1>Breaking Bad</h1>
# <br>
# <br>
# <h2>Storyline</h2>
# <br>
# <h2>Episodes</h2>
# <br>
# <h2>Cast</h2>
# <br>
'-------------------------------------------------------------------------'
# 4)
# <!-- The IMDB series card -->
# <h1>Breaking Bad</h1>
# <p>
#     A high school chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine in order to secure his family's future.
# </p>
# <br>
# <br>
# <h2>Storyline</h2>
# <p>
#   When chemistry teacher Walter White is diagnosed with Stage III cancer and given only two years to live, he decides he has nothing to lose. He lives with his teenage son, who has cerebral palsy, and his wife, in New Mexico. Determined to ensure that his family will have a secure future, Walt embarks on a career of drugs and crime. He proves to be remarkably proficient in this new world as he begins manufacturing and selling methamphetamine with one of his former students. 
# </p>
# <br>
# <h2>Episodes</h2>
# <br>
# <h2>Cast</h2>
# <br>
'-------------------------------------------------------------------------'
# 5)
# <!-- The IMDB series card -->
# <h1>Breaking Bad</h1>
# <span><em>TV Series</em></span> <span><strong>2008-2013</strong></span>
# <p>  A high school chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine in order to secure his family's future.
# </p>
# <br>
# <br>
# <h2>About</h2>
# <br>
# <h2>Storyline</h2>
# <p>
#   When chemistry teacher Walter White is diagnosed with Stage III cancer and given only two years to live, he decides he has nothing to lose. He lives with his teenage son, who has cerebral palsy, and his wife, in New Mexico. Determined to ensure that his family will have a secure future, Walt embarks on a career of drugs and crime. He proves to be remarkably proficient in this new world as he begins manufacturing and selling methamphetamine with one of his former students.
# </p>
# <br>
# <h2>Episodes</h2>
# <br>
# <h2>Cast</h2>
# <br>
'-------------------------------------------------------------------------'
# 6)
# <!-- The IMDB series card -->
# <h1>Breaking Bad</h1>
# <span><em>TV Series</em></span> <span><strong>2008-2013</strong></span>
# <p>
#     A high school chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine in order to secure his family's future.
# </p>
# <br>
# <br>
# <h2>Storyline</h2>
# <p>
#     When chemistry teacher <strong>Walter White</strong> is diagnosed with Stage III cancer and given only two years to live, he decides he has nothing to lose. He lives with his teenage son, who has cerebral palsy, and his wife, in <i>New Mexico</i>. Determined to ensure that his family will have a secure future, Walt embarks on a career of drugs and crime. He proves to be remarkably proficient in this new world as he begins manufacturing and selling methamphetamine with one of his former students.
# </p>
# <br>
# <h2>Episodes</h2>
# <br>
# <h2>Cast</h2>
# <br>
'-------------------------------------------------------------------------'
# 7)
# <!-- The IMDB series card -->
# <div>
#     <h1>Breaking Bad</h1>
#     <span><em>TV Series</em></span> <span><strong>2008-2013</strong></span>
#     <p> 
#  A high school chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine in order to secure his family's future. 
#  </p>
#     <br>
#     <br>
#     </div>

# <div>
#     <h2>Storyline</h2>
#     <p>
#         When chemistry teacher <strong>Walter White</strong> is diagnosed with Stage III cancer and given only two years to live, he decides he has nothing to lose. He lives with his teenage son, who has cerebral palsy, and his wife, in <em>New Mexico</em>. Determined to ensure that his family will have a secure future, Walt embarks on a career of drugs and crime. He proves to be remarkably proficient in this new world as he begins manufacturing and selling methamphetamine with one of his former students.
#     </p>
#     <br>
# </div>

# <div>
# <h2>Episodes</h2>
# <br>
# </div>

# <div>
# <h2>Cast</h2>
# <br>
# </div>
'-------------------------------------------------------------------------'
# 8)
# <!-- The IMDB series card -->
# <div>
#     <h1>Breaking Bad</h1>
#     <span><em>TV Series</em></span> <span><strong>2008-2013</strong></span>
#     <p>
#         A high school chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine in order to secure his family's future.
# </p>
#     <br>
#     <br>
# </div>

# <div>
#     <h2>Storyline</h2>
    # <p>
#         When chemistry teacher <strong>Walter White</strong> is diagnosed with Stage III cancer and given only two years to live, he decides he has nothing to lose. He lives with his teenage son, who has cerebral palsy, and his wife, in <em>New Mexico</em>. Determined to ensure that his family will have a secure future, Walt embarks on a career of drugs and crime. He proves to be remarkably proficient in this new world as he begins manufacturing and selling methamphetamine with one of his former students.
#     </p>
#     <br>
# </div>

# <div>
#     <h2>Episodes</h2>
#     <h3>Season 1</h3>
#     <ol>
#         <li>Pilot</li>
#         <li>Cat's in the Bag...</li>
#         <li>..And the Bag's in the River</li>
#     </ol>
#     <h3>Season 2</h3>
#     <ol>
#         <li>Seven Thirty-Seven</li>
#         <li>Grilled</li>
#         <li>Bit by a Dead Bee</li>
#     </ol>
#     <br>
# </div>

# <div>
#     <h2>Cast</h2>
#     <br>
# </div>
'-------------------------------------------------------------------------'
# 9)
# <!-- The IMDB series card -->
# <div>
#     <h1>Breaking Bad</h1>
#     <span><em>TV Series</em></span> <span><strong>2008-2013</strong></span>
#     <ul>
#         <li>Thriller</li>
#         <li>Drama</li>
#     </ul>
#     <p>
#         A high school chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine in order to secure his family's future.
#     </p>
#     <br>
#     <br>
#   </div>

# <div>
#     <h2>Storyline</h2>
#     <p>
#         When chemistry teacher <strong>Walter White</strong> is diagnosed with Stage III cancer and given only two years to live, he decides he has nothing to lose. He lives with his teenage son, who has cerebral palsy, and his wife, in <em>New Mexico</em>. Determined to ensure that his family will have a secure future, Walt embarks on a career of drugs and crime. He proves to be remarkably proficient in this new world as he begins manufacturing and selling methamphetamine with one of his former students.
#     </p>
#     <br>
# </div>

# <div>
#     <h2>Episodes</h2>
#     <h3>Season 1</h3>
#     <ol>
#         <li>Pilot</li>
#         <li>Cat's in the Bag...</li>
#         <li>..And the Bag's in the River</li>
#     </ol>
#     <h3>Season 2</h3>
#     <ol>
#         <li>Seven Thirty-Seven</li>
#         <li>Grilled</li>
#         <li>Bit by a Dead Bee</li>
#     </ol>
#     <br>
# </div>

# <div>
#     <h2>Cast</h2>
#     <ul>
#         <li>Bryan Cranston</li>
#         <li>Aaron Paul</li>
#         <li>Bob Odenkirk</li>
#         <li>Giancarlo Esposito</li>
#     </ul>
#     <br>
# </div>
'-------------------------------------------------------------------------'
# 10)
# <!-- The IMDB series card -->
# <div>
#     <img alt="poster" src="https://m.media-amazon.com/images/M/MV5BNTEwMDhmNmUtNGJmNi00NGUwLTkxOWQtNzI1NDUwZTFkMThkXkEyXkFqcGdeQXVyNjg0Nzk2Nzc@._V1_FMjpg_UX480_.jpg" width="400" height="226" />
#     <h1>Breaking Bad</h1>
#     <span><em>TV Series</em></span> <span><strong>2008-2013</strong></span>
#     <ul>
#         <li>Thriller</li>
#         <li>Drama</li>
#     </ul>
#     <p>
#         A high school chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine in order to secure his family's future.
#     </p>
#     <br>
#     <br>
# </div>

# <div>
#     <h2>Storyline</h2>
#     <p>
#         When chemistry teacher <strong>Walter White</strong> is diagnosed with Stage III cancer and given only two years to live, he decides he has nothing to lose. He lives with his teenage son, who has cerebral palsy, and his wife, in <em>New Mexico</em>. Determined to ensure that his family will have a secure future, Walt embarks on a career of drugs and crime. He proves to be remarkably proficient in this new world as he begins manufacturing and selling methamphetamine with one of his former students.
#     </p>
#     <br>
# </div>

# <div>
#     <h2>Episodes</h2>
#     <h3>Season 1</h3>
#     <ol>
#         <li>Pilot</li>
#         <li>Cat's in the Bag...</li>
#         <li>..And the Bag's in the River</li>
#     </ol>
#     <h3>Season 2</h3>
#     <ol>
#         <li>Seven Thirty-Seven</li>
#         <li>Grilled</li>
#         <li>Bit by a Dead Bee</li>
#     </ol>
#     <br>
# </div>

# <div>
#     <h2>Cast</h2>
#     <ul>
#         <li>Bryan Cranston</li>
#         <li>Aaron Paul</li>
#         <li>Bob Odenkirk</li>
#         <li>Giancarlo Esposito</li>
#     </ul>
#     <br>
# </div>

# <div>
#     <h2>Photos</h2>
#     <img src="https://m.media-amazon.com/images/M/MV5BMjE1OTMwNTA5NV5BMl5BanBnXkFtZTgwMDkzOTA1NjM@._V1_FMjpg_UX320_.jpg" alt="school" width="320" height="240"/>
#     <img src="https://m.media-amazon.com/images/M/MV5BMjQ5MTc3NDg3MF5BMl5BanBnXkFtZTgwNTI2MTU5NTM@._V1_FMjpg_UX320_.jpg" alt="snow" width="320" height="240"/>
# </div>
'-------------------------------------------------------------------------'
# 11)
# <!-- The IMDB series card --><div>
#     <img alt="poster" src="https://m.media-amazon.com/images/M/MV5BNTEwMDhmNmUtNGJmNi00NGUwLTkxOWQtNzI1NDUwZTFkMThkXkEyXkFqcGdeQXVyNjg0Nzk2Nzc@._V1_FMjpg_UX480_.jpg" width="400" height="226" />
#     <a href="https://www.imdb.com/title/tt0903747"><h1>Breaking Bad</h1></a>
#     <span><em>TV Series</em></span> <span><strong>2008-2013</strong></span>
#     <ul>
#         <li>Thriller</li>
#         <li>Drama</li>
#     </ul>
#     <p>
#         A high school chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine in order to secure his family's future.
#     </p>
#     <br>
#     <br>
# </div>

# <div>
#     <h2>Storyline</h2>
#     <p>
#         When chemistry teacher <strong>Walter White</strong> is diagnosed with Stage III cancer and given only two years to live, he decides he has nothing to lose. He lives with his teenage son, who has cerebral palsy, and his wife, in <em>New Mexico</em>. Determined to ensure that his family will have a secure future, Walt embarks on a career of drugs and crime. He proves to be remarkably proficient in this new world as he begins manufacturing and selling methamphetamine with one of his former students.
#     </p>
#     <br>
# </div>

# <div>
#     <h2>Episodes</h2>
#     <h3>Season 1</h3>
#     <ol>
#         <li>Pilot</li>
#         <li>Cat's in the Bag...</li>
#         <li>..And the Bag's in the River</li>
#     </ol>
#     <h3>Season 2</h3>
#     <ol>
#         <li>Seven Thirty-Seven</li>
#         <li>Grilled</li>
#         <li>Bit by a Dead Bee</li>
#     </ol>
#     <br>
# </div>

# <div>
#     <h2>Cast</h2>
#     <ul>
#         <li><a href="https://www.imdb.com/name/nm0186505/">Bryan Cranston</a></li>
#         <li><a href="https://www.imdb.com/name/nm0666739/">Aaron Paul</a></li>
#         <li><a href="https://www.imdb.com/name/nm0644022/">Bob Odenkirk</a></li>
#         <li><a href="https://www.imdb.com/name/nm0002064/">Giancarlo Esposito</a></li>
#     </ul>
#     <br>
# </div>

# <div>
#     <h2>Photos</h2>
#     <img alt="school" width="320" height="240" src="https://m.media-amazon.com/images/M/MV5BMjE1OTMwNTA5NV5BMl5BanBnXkFtZTgwMDkzOTA1NjM@._V1_FMjpg_UX320_.jpg" />
#     <img alt="snow" width="320" height="240" src="https://m.media-amazon.com/images/M/MV5BMjQ5MTc3NDg3MF5BMl5BanBnXkFtZTgwNTI2MTU5NTM@._V1_FMjpg_UX320_.jpg" />
# </div>
'-------------------------------------------------------------------------'
# 12)
# <!-- The IMDB series card -->
# <div>
#     <img alt="poster" src="https://m.media-amazon.com/images/M/MV5BNTEwMDhmNmUtNGJmNi00NGUwLTkxOWQtNzI1NDUwZTFkMThkXkEyXkFqcGdeQXVyNjg0Nzk2Nzc@._V1_FMjpg_UX480_.jpg" width="400" height="226" />
#     <a href="https://www.imdb.com/title/tt0903747"><h1>Breaking Bad</h1></a>
#     <span><em>TV Series</em></span> <span><strong>2008-2013</strong></span>
#     <ul>
#         <li>Thriller</li>
#         <li>Drama</li>
#     </ul>
#     <p>A high school chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine in order to secure his family's future.</p>
#     <br>
#     <br>
# </div>
# <span><a href="#storyline">Storyline</a></span>
# <span><a href="#episodes">Episodes</a></span>
# <span><a href="#cast">Cast</a></span>
# <span><a href="#photos">Photos</a></span>
# <div id="storyline">
#     <h2>Storyline</h2>
#     <p>
#         When chemistry teacher <strong>Walter White</strong> is diagnosed with Stage III cancer and given only two years to live, he decides he has nothing to lose. He lives with his teenage son, who has cerebral palsy, and his wife, in <em>New Mexico</em>. Determined to ensure that his family will have a secure future, Walt embarks on a career of drugs and crime. He proves to be remarkably proficient in this new world as he begins manufacturing and selling methamphetamine with one of his former students.
#     </p>
#     <br>
# </div>

# <div id="episodes">
#     <h2>Episodes</h2>
#     <h3>Season 1</h3>
#     <ol>
#         <li>Pilot</li>
#         <li>Cat's in the Bag...</li>
#         <li>..And the Bag's in the River</li>
#     </ol>
#     <h3>Season 2</h3>
#     <ol>
#         <li>Seven Thirty-Seven</li>
#         <li>Grilled</li>
#         <li>Bit by a Dead Bee</li>
#     </ol>
#     <br>
# </div>

# <div id="cast">
#     <h2>Cast</h2>
#     <ul>
#         <li><a href="https://www.imdb.com/name/nm0186505/">Bryan Cranston</a></li>
#         <li><a href="https://www.imdb.com/name/nm0666739/">Aaron Paul</a></li>
#         <li><a href="https://www.imdb.com/name/nm0644022/">Bob Odenkirk</a></li>
#         <li><a href="https://www.imdb.com/name/nm0002064/">Giancarlo Esposito</a></li>
#     </ul>
#     <br>
# </div>

# <div id="photos">
#     <h2>Photos</h2>
#     <img alt="school" width="320" height="240" src="https://m.media-amazon.com/images/M/MV5BMjE1OTMwNTA5NV5BMl5BanBnXkFtZTgwMDkzOTA1NjM@._V1_FMjpg_UX320_.jpg" />
#     <img alt="snow" width="320" height="240" src="https://m.media-amazon.com/images/M/MV5BMjQ5MTc3NDg3MF5BMl5BanBnXkFtZTgwNTI2MTU5NTM@._V1_FMjpg_UX320_.jpg" />
# </div>
'-------------------------------------------------------------------------'
'CSS(унив. селектор)'
# 1)
'style.css'
# * {
#     text-decoration: none;
# }
'-------------------------------------------------------------------------'
# 2)
'style.css'
# h1{
#     color: red;
# }
# h2{
#     color: green;
# }
'-------------------------------------------------------------------------'
# 3)
'index.html'
# class="season2"

'style.css'
# .season1 {
#     color: orange; 
# }
# .season2 {
#     color: violet;
# }
'-------------------------------------------------------------------------'
# 4)
'index.html'
# class="season1 bold"
# class="season2 italic"

'style.css'
# .bold {
#     font-weight: bold;
# }
# .italic {
#     font-style: italic;
# }
'-------------------------------------------------------------------------'
# 5)
'index.html'
# id="walter"
# id="jesse"
# id="saul"
# id="gus"

'style.css'
# #walter {
#     color: darkviolet;
# }
# #jesse {
#     color: darkblue;
# }
# #saul {
#     color: darkgreen;
# }
# #gus {
#     color: darkred;
# }
'-------------------------------------------------------------------------'
# 6)
'index.html'
# style="name"

'style.css'
# a[href*="title"] {
#     text-transform: lowercase;
# }
# a[href*="name"] {
#     text-transform: uppercase;
# }
'-------------------------------------------------------------------------'
'Как открывать и создавать venv'
# cd /Desktop/makers
# python3 -m venv venv
# . venv/bin/activate
# pip install -r requirementes.txt
# pip freeze
# code .
'-------------------------------------------------------------------------'
'Parsing(парсинг)'
# 1)
# from bs4 import BeautifulSoup
# import requests
# import csv

# source = requests.get('https://stackoverflow.com/questions').status_code
# print(source)
'-------------------------------------------------------------------------'
# 2)
# from bs4 import BeautifulSoup
# import requests
# import csv

# source = requests.get('http://www.example.com/').text
# my_page = BeautifulSoup(source, 'lxml')

# print('h1:', my_page.h1.text)
# print('p:', my_page.p.text)
# print('a:', my_page.a.get('href'))
'-------------------------------------------------------------------------'
# 3)
# from bs4 import BeautifulSoup
# import requests
# import csv

# source = requests.get('https://www.wikipedia.org/').text
# my_page = BeautifulSoup(source, 'lxml')
# blog_lang = my_page.find('div', class_ = 'central-featured-lang lang4')

# print(blog_lang.text)
'-------------------------------------------------------------------------'
# 4)

'-------------------------------------------------------------------------'
# 5)

'-------------------------------------------------------------------------'
# 6)

'-------------------------------------------------------------------------'
'ООП(Объектно-ориентированное программирование)'
# 1)
# class Song:
#     def __init__ (self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
        
#     def show_title(self):
#         return f'Название этой песни {self.title}'
        
#     def show_author(self):
#         return f'Автор этой песни {self.author}'
        
#     def show_year(self):
#         return f'Эта песня вышла в {self.year} году'

# song = Song(title = 'Happy', author = 'Pharrell Williams', year = 2013)
        
# print(song.show_title())
# print(song.show_author())
# print(song.show_year())
'-------------------------------------------------------------------------'
# 2)
# class Circle:
#     color = 'Синий'
#     pi = 3.14
#     def __init__(self, radius):
#         self.radius = radius
        
#     def get_area(self):
#         return self.pi*(self.radius**2)

# circle = Circle(radius=13)
# circle.color = 'green'
# print(circle.color)

# print(circle.get_area())
'-------------------------------------------------------------------------'
# 3)
# class BankAccount:
#     def __init__(self):
#         self.balance = 0
        
#     def withdraw(self, amount):
#         self.balance -= amount
#         print(f'Ваш баланс: {self.balance} сом')
        
#     def deposit(self, amount):
#         self.balance += amount
#         print(f'Ваш баланс: {self.balance} сом')
        
# account = BankAccount()
# account.deposit(1000)
# account.withdraw(500)
'-------------------------------------------------------------------------'
# 4)
# class Taxi:
#     def __init__(self, name, cost, cost_km):
#         self.name = name
#         self.cost = cost
#         self.cost_km = cost_km
        
#     def get_total_cost(self, km):
#         self.cost = self.cost_km * km + self.cost
#         return f'Такси {self.name}, стоимость поездки: {self.cost} сом'

# taxi1 = Taxi(name = 'Namba', cost = 29, cost_km = 15)
# taxi2 = Taxi(name = 'Yandex', cost = 25, cost_km = 17)
# taxi3 = Taxi(name = 'Jorgo', cost = 28, cost_km = 15)
        
# print(taxi1.get_total_cost(10))
# print(taxi2.get_total_cost(6))
# print(taxi3.get_total_cost(14))
'-------------------------------------------------------------------------'
# 5)
# class Phone:
#     def __init__(self, name, last_name, phone):
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone
    
#     def get_info(self):
#         print(f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}')

# contact = Phone('John', 'Snow', +996707707707)
# contact.get_info()
'-------------------------------------------------------------------------'
# 6)
# class Salary:
#     percent = 8
#     def __init__(self, salary, experience):
#         self.salary = salary
#         self.experience = experience

#     def count_percent(self):
#         return self.salary * self.percent / 100 * self.experience

# obj = Salary(10000, 10)
# print(obj.count_percent())
'-------------------------------------------------------------------------'
# 7)
# import datetime
# class Nobel:
#     def __init__(self, category, year, winner):
#         self.category = category
#         self. year = year
#         self. winner = winner

#     def get_year(self):
#         a = datetime.datetime.now()
#         result = a.year - self.year
#         return f'выиграл {result} лет(года) назад'

# winner1 = Nobel("Литература", 1971, "Пабло Неруда") 
# print(winner1.category, winner1.year, winner1.winner) 
# print(winner1.get_year())

  
# winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ") 
# print(winner2.category, winner2.year, winner2.winner) 
# print(winner2.get_year())
'-------------------------------------------------------------------------'
# 8)
# class Password:
#     def __init__(self, password):
#         self.password = password
        
#     def __str__(self) -> str:
#         return '*' * len(self.password)
    
#     def validate(self):
#         if not len(self.password) == 12 and len(self.password) < 15:
#             return f'Password should be longer than 8, and less than 15'
#         if not any(map(lambda i: i.isdigit(), self.password)):
#             return f'Password should contain numbers too'
#         if not any(map(lambda i: i.isalpha(), self.password)):
#             return f'Password should contain letters as well'
#         if not any(map(lambda i: i in ['@', '#', '&', '$', '%', '!', '~', '*'], self.password)):
#             return f'Your password should have some symbols'
#         return f'Ваш пароль сохранен.'
            
            
# password = Password('beil4ik@play')
# print(password.validate())
# print(password)
'-------------------------------------------------------------------------'
# 9)
# class Math:
#     def __init__(self, number):
#         self.number = number
        
#     def get_factorial(self):
#         self.factorial = 1
#         for i in range(2, self.number+1):
#             self.factorial = self.factorial*i
#         return self.factorial
            
#     def get_sum(self):
#         number = [int(x)for x in str(self.number)]
#         suma = sum(number)
#         return suma
        
#     def get_mul_table(self):
#         s = ''
#         for i in range(10):
#             s += f'{self.number} x {i+1} = {self.number * (i+1)}' + '\n'
#         return s
            
# number1 = Math(11)
# print(number1.get_factorial())
# print(number1.get_sum())
# print(number1.get_mul_table())
'-------------------------------------------------------------------------'
# 10)
# class ToDo:
#     def __init__(self, string):
#         self.todo = string
#     instances = dict()
        
#     def give_priority(self, priority):
#         ToDo.instances[priority] = self.todo
        
#     def list_of_tasks(self):
#         return sorted(ToDo.instances.items())
        
# var1 = ToDo('сходить в кино')
# var1.give_priority(2)
# var2 = ToDo('выгулять собаку')
# var2.give_priority(3)
# var3 = ToDo('сделать домашку')
# var3.give_priority(1)
# print(var3.list_of_tasks())
'-------------------------------------------------------------------------'
'ООП(Наследование)'
# 1)
# class Class1:

#     def first(self):
#         pass

#     def second(self):
#         pass

# class Class2(Class1):

#     def third(self):
#         pass

#     def fourth(self):
#         pass

# obj = Class2()
# obj.first()
# obj.second()
# obj.third()
# obj.fourth()
'-------------------------------------------------------------------------'
# 2)
# class A:

#     def method1(self):
#         print(f'Основной функционал')

# class B(A):
#     def method1(self):
#         super().method1()
#         print(f'Дополнительный функционал')

# obj = B()
# obj.method1()
'-------------------------------------------------------------------------'
# 3)
# class MyString(str):
#     def __init__(self, stroka1):
#         self.stroka1 = stroka1

#     def append(self, stroka2):
#         self.stroka2 = stroka2
#         self.stroka1 = self.stroka1 + self.stroka2
#         return self.stroka1

#     def pop(self):
#         last_w = self.stroka1[-1]
#         self.stroka1 = self.stroka1[:-1]
#         # print(self.stroka1)
#         return last_w
    
#     def __str__(self) -> str:
#         return self.stroka1
    

# example = MyString('String')
# example.append('hello') #можно и print(example.append('hello'))
# print(example.pop())
# print(example)
'-------------------------------------------------------------------------'
# 4)
# class MyDict(dict):

#     def get(self, key):
#         result = 'Are you kidding?'
#         return dict.get(self, key, result)

# obj_dict = MyDict({'some_title': 2})
# print(obj_dict.get('some'))
'-------------------------------------------------------------------------'
# 5)
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def display(self):
#         return f"name:{self.name}, age:{self.age}"
    
# class Student(Person):
#     def __init__(self, name, age, faculty):
#         super().__init__(name, age)
#         self.faculty = faculty
    
#     def display_student(self):
#         get_info = super().display()
#         return get_info + f", faculty:{self.faculty}"
    
# obj_student = Student('Rick', 21, 'science')
# print(obj_student.display())
# print(obj_student.display_student())
'-------------------------------------------------------------------------'
# 6)
# class ContactList(list):
#     def __init__(self, list_):
#         self.list_ = list_

#     def search_by_name(self, name):
#         a = []
#         for i in self.list_:
#             if name in i:
#                 a.append(i)
#         return a

# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan'])
# print(all_contacts.search_by_name('Olya'))
'-------------------------------------------------------------------------'
# 7)
# class SmartPhones:
#     def __init__(self, name, color, memory):
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.battery = 0

#     def __str__(self):
#         return f"{self.name} {self.memory}"

#     def charge(self, number):
#         self.battery += number
    
# class Iphone(SmartPhones):
#     def __init__(self, name, color, memory, ios):
#         super().__init__(name, color, memory)
#         self.ios = ios

#     def send_imessage(self, string):
#         return f"sending {string} from {self.name} {self.memory}"


# class Samsung(SmartPhones):
#     def __init__(self, name, color, memory, android):
#         super().__init__(name, color, memory)
#         self.android = android

#     def show_time(self):
#         import datetime
#         return datetime.datetime.now().time()


# phone = SmartPhones('generic', 'blue', '128GB') 
# print(phone) 

# print(phone.battery) 
# phone.charge(20) 
# print(phone.battery) 

# iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
# print(iphone7)
# print(iphone7.send_imessage('hello'))

# samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
# print(samsung21.show_time())
'-------------------------------------------------------------------------'
# 8)
# class CustomError(Exception):
#     def __init__(self, message):
#         self.message = message
        
# capitals_error = CustomError('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ')

# def check_letters(str_):
#     if str_.islower():
#         raise capitals_error
#     else:
#         return f'ВСЕ ОТЛИЧНО! {str_}'
        
# print(check_letters("HELLO"))
'-------------------------------------------------------------------------'
'ООП(Множественное наследование и миксины)'
# 1)
# class Auto:
#     def ride(self):
#         print('Riding on a ground')

# class Boat:
#     def swim(self):
#         print('Floating on water')

# class Amphibian(Auto, Boat):
#     pass

# obj = Amphibian()
# obj.ride()
# obj.swim()
'-------------------------------------------------------------------------'
# 2)
'1 решение'
# class RadioMixin:
#     def play_music(self):
#         class_ = 'title'
#         print(f'Песня называется {class_}')

# class Auto(RadioMixin):
#     pass

# class Boat(RadioMixin):
#     pass

# class Amphibian(Auto, Boat):
#     pass

# auto = Auto()
# boat = Boat()
# obj = Amphibian()
# obj.play_music()

'2 решение'
# class RadioMixin:
#     def play_music(self, title):
#         print(f'Песня называется {title}')

# class Auto(RadioMixin):
#     pass

# class Boat(RadioMixin):
#     pass

# class Amphibian(Auto, Boat):
#     pass

# auto = Auto()
# boat = Boat()
# obj = Amphibian()
# auto.play_music('Shape of you')
# boat.play_music('Believer')
# obj.play_music('Dancin')
'-------------------------------------------------------------------------'
# 3)
'1 решение'
# import datetime

# class Clock:
#     def current_time(self):
#         dt_new = datetime.datetime.today().strftime('%H:%M:%S')
#         print(dt_new)

# class Alarm:
#     def on(self):
#         pass

#     def off(self):
#         pass

# class AlarmClock(Clock, Alarm):
#     def alarm_on(self):
#         print('Будильник включён')

# clock = AlarmClock()
# clock.current_time()
# clock.alarm_on()

'2 решение'
# class Clock:
#     def current_time(self):
#         import datetime
#         dt_new = datetime.datetime.today().strftime('%H:%M:%S')
#         print(dt_new)

# class Alarm:
#     @staticmethod
#     def on():
#         print('Будильник включён')

#     @staticmethod
#     def off():
#         print('Будильник выключен')

# class AlarmClock(Clock, Alarm):
#     @staticmethod
#     def alarm_on():
#         Alarm.on() #Alarm.off()

# clock = AlarmClock()
# clock.current_time()
# clock.alarm_on()
'-------------------------------------------------------------------------'
# 4)
# from abc import ABC, abstractmethod

# class Coder(ABC):
#     count_code_time = 0

#     @abstractmethod
#     def get_info(self):
#         pass

#     @abstractmethod
#     def coding(self, hours):
#         pass

# class Backend(Coder):
#     def __init__(self, experience, languages_backend):
#         self.experience = experience
#         self.languages_backend = languages_backend

#     def get_info(self):
#         return f"{self.languages_backend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование"

#     def coding(self, hours):
#         self.count_code_time += hours

# class Frontend(Coder):
#     def __init__(self, experience, languages_frontend):
#         self.experience = experience
#         self.languages_frontend = languages_frontend

#     def get_info(self):
#         return f"{self.languages_frontend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование"

#     def coding(self, hours):
#         self.count_code_time += hours

# class Fullstack(Backend, Frontend):
#     pass


# a = Backend('Junior', 'Python')
# b = Frontend('Middle', 'JavaScript')
# c = Fullstack('Senior', 'Python and JS')

# a.coding(12)
# b.coding(45)
# c.coding(17)
# print(a.get_info())
# print(b.get_info())
# print(c.get_info())
'-------------------------------------------------------------------------'
# 5)
# class Square:
#     def __init__(self, side):
#         self.side = side
        
#     def get_area(self):
#         return self.side * self.side
    
# class Triangle:
#     def __init__(self, height, base):
#         self.height = height
#         self.base = base
        
#     def get_area(self):
#         return int(0.5*self.base*self.height)
    
# class Pyramid(Triangle, Square):
#     def __init__(self, height, base):
#         super().__init__(height, base)
        
#     def get_volume(self):
#         return int(1/3*self.base**2*self.height)
    
# obj = Square(3)
# obj2 = Triangle(3,5)
# obj3 = Pyramid(10,10)
# print(obj.get_area())
# print(obj2.get_area())
# print(obj3.get_volume())
'-------------------------------------------------------------------------'
# 6)
# class CreateMixin:
#     def create(self, key, todo):
#         if key in self.todos.keys():
#             return 'Задача под таким ключом уже существует'
#         self.todos[key] = todo
#         return self.todos
            
# class DeleteMixin:
#     def delete(self, key):
#         delete_ = self.todos.pop(key, 'нет такого ключа')
#         if 'нет такого ключа' == delete_:
#             return delete_
#         return delete_
            
# class UpdateMixin:
#     def update(self, key, new_value):
#         self.todos[key] = new_value
#         return self.todos
        
# class ReadMixin:
#     def read(self):
#         res = [x for x in self.todos.items()]
#         return sorted(res)
    
# class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
#     todos = {}
#     def set_deadline(self, deadline):
#         import datetime
#         time_ = datetime.datetime.now().strftime('%d/%m/%Y')
#         deadline = deadline.split('/')
#         time_ = time_.split('/')
#         deadline = list(map(int, deadline))
#         time_ = list(map(int, time_))
#         time_ = sum((time_[0], time_[1]*30, time_[2]*365))
#         deadline = datetime.date(deadline[2], deadline[1], deadline[0])
#         time_ = datetime.date.today()
#         return (deadline - time_).days
    
# task = ToDo() 
# print(task.set_deadline('31/12/2022'))
# print(task.create(1, 'todo'))
# print(task.delete(3))
# print(task.update(1, 'todo'))
# print(task.read())
# print(task.create(1, 'Do housework'))
# print(task.create(1, 'Do housework'))
# print(task.create(2, 'Go for a walk'))
# print(task.update(1, 'Do homework'))
# print(task.delete(2))
# print(task.read())
# print(task.set_deadline('31/12/2021'))
'-------------------------------------------------------------------------'
# 7)
# class Game:
#     def __init__(self, type, name):
#         self.type = type
#         self.name = name
#         self.extensions = []
    
#     def get_description(self, description):
#         return f'{self.name} это {description} в жанре песочницы с элементами выживания и открытым миром.'
    
#     def get_extensions(self):
#         res = ' '.join(self.extensions)
#         return res if res else 'Нет подключенных расширений'
    
# class ExtensionMixin(Game):
#     def add_extension(self, extension):
#         self.extensions.append(extension)
#         return f'Добавлено новое расширение {extension} для игры {self.name}'
    
#     def remove_extension(self, del_extension): 
#         if del_extension in self.extensions:
#             self.extensions.remove(del_extension)
#             return f'{del_extension} был отключен от {self.name}'
#         else:
#             return 'Такого расширения нет в списке.'

# obj1 = Game()
# print(obj1.get_description('Minecraft', 'инди-игра'))
# print(obj1.get_extensions())

# obj = ExtensionMixin()
# print(obj.add_extension('Multiverse-Core', 'Minecraft'))
# print(obj.remove_extension('Multiverse-Core', 'Minecraft'))
'-------------------------------------------------------------------------'
# 8)
# class FlyMixin:
#     def fly(self):
#         print('я могу летать')
        
# class WalkMixin:
#     def walk(self):
#         print('я могу ходить')
        
# class SwimMixin:
#     def swim(self):
#         print('я могу плавать')
        
# class Human(WalkMixin, SwimMixin):
#     pass
        
# class Fish(SwimMixin):
#     pass
    
# class Exocoetidae(SwimMixin, FlyMixin):
#     pass
    
# class Duck(SwimMixin, WalkMixin, FlyMixin):
#     pass

# obj = Human()
# obj.swim()
# obj.walk()
# obj.swim()
'-------------------------------------------------------------------------'
'ООП(Инкапуляция)'
# 1)
# class A:
#     def public(self):
#         return 'Public method'

#     def _protected(self):
#         return 'Protected method'

#     def __private(self):
#         return 'Private method'

#     def print_protected(self):
#         self._protected()
        
#     def print_private(self):
#         self.__private()

# obj1 = A()
# print(obj1.public())
# print(obj1._protected())
# print(obj1._A__private())
'-------------------------------------------------------------------------'
# 2)
# class A:
#     def method1(self):
#         return f'Hello World'

# class B(A):
#     pass

# b1 = B()
# print(b1.method1())
'-------------------------------------------------------------------------'
# 3)
# class Car:
#     __speed = 0
    
#     def set_speed(self, meaning):
#         self.__speed = meaning
#         return self.__speed

#     def show_speed(self):
#         return self.__speed

# car1 = Car()
# print(car1.show_speed())
# car1.set_speed(20)
# print(car1.show_speed())
'-------------------------------------------------------------------------'
# 4)
# class Car:
#     __speed = 0
#     @property
    
#     def speed(self):
#         return self.__speed
#     @speed.setter
        
#     def speed(self, new):
#         self.__speed = new
#         return self.__speed
        
# car1 = Car()
# print(car1.speed)
# car1.speed = 20
# print(car1.speed)
'-------------------------------------------------------------------------'
# 5)
# class Person:
#     name = "John"
#     _phone_number = "+996 557 55 17 57"
#     __card_number = "9999 9999 9999 9999"

#     @property
#     def number(self):
#         return self.__card_number

# john = Person()
# print(john.name)
# print(john._phone_number)
# print(john.number)
'-------------------------------------------------------------------------'
# 6)
# class Person:
#     def __init__(self, name, _phone_number, __сard_number):
#         self.name = name
#         self._phone_number = _phone_number
#         self.__card_number = __сard_number

#     @property
#     def number(self):
#         return self.__card_number

# john = Person("John", "+996 557 55 17 57", "9999 9999 9999 9999")
# print(john.name)
# print(john._phone_number)
# print(john.number)
'-------------------------------------------------------------------------'
# 7)
# class Person:
#     name = "John"
#     _phone_number = "+996 557 55 17 57"
#     __card_number = "9999 9999 9999 9999"

#     @property
#     def get_number(self):
#         return self.__card_number

#     def set_number(self):
#         self.__card_number = None
#         return self.__card_number

# john = Person()
# john.name = None
# john._phone_number = None
# print(john.name)
# print(john._phone_number)
# print(john.set_number())
'-------------------------------------------------------------------------'
# 8)
# class Person:
#     def __init__(self, name, phone_number, card_number):
#         self.name = self.__validate_name(name)
#         self._phone_number = phone_number
#         self.__card_number = card_number
        
#     def __validate_name(self, name):
#         if len(name) < 2:
#             return "John"
#         else:
#             return name.title()
        
#     def get_card_number(self):
#         return self.__card_number
    
#     def set_card_number(self, card_number):
#         self.__card_number = card_number
        
# sam = Person("SAM", "+996 557 55 17 57", "9999 9999 9999 9999")
# print(sam.name)
# print(sam._phone_number)
# print(sam.get_card_number())
'-------------------------------------------------------------------------'
# 9)

'-------------------------------------------------------------------------'
# 10)

'-------------------------------------------------------------------------'
# 11)
# class Game:
#     __level = 0
#     def __init__(self, name):
#         self.name = self.__validate_name(name)

#     def set_level(self, level):
#         if self.name == 'Tolik':
#             self.__level = level
#         else: print(f"{self.name} ты не Tolik!")

#     def __validate_name(self, name):
#         return name.title()

# game = Game('Raychel')
# game.set_level(5)
# print(game._Game__level)
# game2 = Game('TOLIK')
# game2.set_level(5)
# print(game._Game__level)
'-------------------------------------------------------------------------'
# 12)

'-------------------------------------------------------------------------'
# 13)

'-------------------------------------------------------------------------'
# 14)

'-------------------------------------------------------------------------'
# 15)

'-------------------------------------------------------------------------'
# 16)
# class Person:
#     def __init__(self):
#         self.__name = None
#         self.__last_name = None
#         self.__age = None
#         self.__email = None

#     @property
#     def name(self):
#         return self.__name
    
#     @name.setter
#     def name(self, value):
#         self.__name = value
    
#     @property
#     def last_name(self):
#         return self.__last_name

#     @last_name.setter
#     def last_name(self, value):
#         self.__last_name = value
    
#     @property
#     def age(self):
#         return self.__age
    
#     @age.setter
#     def age(self, value):
#         self.__age = value


#     @property
#     def email(self):
#         return self.__email
    
#     @email.setter
#     def email(self, value):
#         self.__email = value

# john = Person()

# print(john.name) # None
# print(john.last_name) # None
# print(john.age) # None
# print(john.email) # None
# john.name = 'John'
# john.last_name = 'Snow'
# john.age = 30
# john.email = 'johnsnow@gmail.com'
# print(john.name) # John
# print(john.last_name) # Snow
# print(john.age) # 30
# print(john.email) # johnsnow@gmail.com
'-------------------------------------------------------------------------'
# 17)

'-------------------------------------------------------------------------'
'Могут спросить на стажировке!'
# def func():
#     print("Hello world")
#     return func

# func()()()()()
'-------------------------------------------------------------------------'
'ООП(Полиморфизм)'
# 1)
# a = 'Hello world!'
# b = [1, 2, 3, 4]
# c = {1:'a', 2: {'a': 1, 'b': 2}, 3:'c'}

# lst = [a, b, c]
# for x in lst:
#     print(len(x))
'-------------------------------------------------------------------------'
# 2)
# class Dog:

#     def voice(self):
#         print('Гав')

# class Cat:

#     def voice(self):
#         print('Мяу')

# barsik = Cat()
# rex = Dog()

# def to_pet(golos):
#     golos.voice()

# to_pet(barsik)
# to_pet(rex)
'-------------------------------------------------------------------------'
# 3)
# class Person:
#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name

#     def get_info(self):
#         print(f'Привет, меня зовут {self.name} {self.last_name}')

# class Employee(Person):
#     def __init__(self, name, last_name, work, status):
#         super().__init__(name, last_name)
#         self.work = work
#         self.status = status

#     def get_info(self):
#         print(f'Привет, меня зовут {self.name} {self.last_name}, я работаю в компании {self.work} на должности {self.status}')

# class Student(Person):
#     def __init__(self, name, last_name, university, course):
#         super().__init__(name, last_name)
#         self.university = university
#         self.course = course

#     def get_info(self):
#         print(f'Привет, меня зовут {self.name} {self.last_name}, я учусь в {self.university} на {self.course} курсе')

# def get_human_info(func1):
#     return func1.get_info()

# person = Person('Sultan', 'Katana')
# employee = Employee('Sultan', 'Katana', 'Makers', 'ментор')
# student = Student('Sultan', 'Katana', 'КГТУ', 3)

# get_human_info(employee)
# get_human_info(student)
# get_human_info(person)
'-------------------------------------------------------------------------'
# 4)
# from abc import ABC, abstractmethod
# from math import pi

# class Shape(ABC):

#     @abstractmethod
#     def get_area(self):
#         pass

# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
    
#     def get_area(self):
#         return self.base * self.height * 0.5

# class Square(Shape):
#     def __init__(self, length):
#         self.length = length

#     def get_area(self):
#         return self.length ** 2


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def get_area(self):
#         return pi * self.radius ** 2

# triangle = Triangle(5, 5)
# square = Square(5)
# circle = Circle(10)

# print(triangle.get_area())
# print(square.get_area())
# print(circle.get_area())
'-------------------------------------------------------------------------'
# 5)
# class OS:
#     def __init__(self, version):
#         self.version = version

# class Windows(OS):
#     def copy(self, text):
#         return f'скопирован текст "{text}" горячими клавишами CTRL + C'

# class MacOS(OS):
#     def copy(self, text):
#         return f'скопирован текст "{text}" горячими клавишами COMMAND + C'

# class Linux(OS):
#     def copy(self, text):
#         return f'скопирован текст "{text}" горячими клавишами CTRL + SHIFT + C'
    
# win = Windows('10')
# mac = MacOS('Big Sur')
# lin = Linux('Ubuntu')

# print(win.copy('Полиморфизм — одна из основных парадигм ООП'))
# print(mac.copy('Полиморфизм - разное поведение одного и того же метода в разных классах'))
# print(lin.copy('На самом деле одинаковым является только имя метода, его исходный код зависит от класса'))
'-------------------------------------------------------------------------'
# 6)
# class Language:
#     def __init__(self, level, type) -> None:
#         self.lvl = level
#         self.type = type

# class Python(Language):
#     def write_function(self, func_name, arg):
#         return f"def {func_name}({arg}):"

#     def create_variable(self, var_name, value):
#         if isinstance(value, str):
#             return f"{var_name} = '{value}'"
#         else:
#             return f"{var_name} = {value}"

# class JavaScript(Language):
#     def write_function(self, func_name, arg):
#         return f"function {func_name}({arg}) {{    }};"

#     def create_variable(self, var_name, value):
#         if isinstance(value, str):
#             return f"let {var_name} = '{value}';"
#         else:
#             return f"let {var_name} = {value};"
# py = Python('Intermediate', 'Backend')
# print(py.write_function('get_code', 'a')) 
# print(py.create_variable('name', 'John'))

# js = JavaScript('Advanced', 'Frontend')
# print(js.write_function('validate', 'form'))
# print(js.create_variable('password', 'john@123'))
'-------------------------------------------------------------------------'
# 7)
# class Money:
#     def __init__(self, country, symbol):
#         self.country = country
#         self.symbol = symbol
        
# class Dollar(Money):
#     rate = 84.80
    
#     def exchange(self, amount):
#         return f"$ {amount} равен {Dollar.rate * amount} сомам"
    
# class Euro(Money):
#     rate = 98.40
    
#     def exchange(self, amount):
#         return f"€ {amount} равен {Euro.rate * amount} сомам"
    
    
# dol = Dollar('Alaska', '$')
# eu = Euro('France', '€')
# print(dol.exchange (100))
# print(eu.exchange (80))
'-------------------------------------------------------------------------'
# 8)
# class Planet:
#     def __init__(self, orbit):
#         self.orbit = orbit

# class Mercury(Planet):
#     def get_age(self, earth_age):
#         return f'на Меркурии ваш возраст составляет {int(earth_age * 365 / self.orbit)} лет'

# class Venus(Planet):
#     def get_age(self, earth_age):
#         return f'на Венере ваш возраст составляет {round(earth_age * 365 / self.orbit * 365)} дней'

# class Jupiter(Planet):
#     def get_age(self, earth_age):
#         return f'на Юпитере ваш возраст составляет {round(earth_age * 365 // self.orbit * 365 * 24)} часов'

# mercury = Mercury(88)
# venus = Venus(225)
# jupiter = Jupiter(12)
# print(venus.get_age(20))
# print(jupiter.get_age(20))
# print(mercury.get_age(20))
'-------------------------------------------------------------------------'
'psql на терминале'
# bayel@bayel:~$ psql
# psql (14.6 (Ubuntu 14.6-0ubuntu0.22.04.1))
# Type "help" for help.

# bayel=# \c weather_db
# You are now connected to database "weather_db" as user "bayel".
# weather_db=# CREATE TABLE table1 (
# weather_db(# num int,
# weather_db(# name varchar(50));
# CREATE TABLE
# weather_db=# CREATE TABLE table1 (
# weather_db(# num int,
# weather_db(# value varchar(50));
# ERROR:  relation "table1" already exists
# weather_db=# CREATE TABLE table2 (
# weather_db(# num int,
# weather_db(# value varchar(50));
# CREATE TABLE
# weather_db=# INSERT INTO table1 VALUES
# weather_db-# (1, a)
# weather_db-# (1, a),
# weather_db-# (2, b),
# weather_db-# (3, c);
# ERROR:  syntax error at or near "("
# LINE 3: (1, a),
#         ^
# weather_db=# INSERT INTO table1 VALUES
# weather_db-# (1, 'a'),
# weather_db-# (2, 'b'),
# weather_db-# (3, 'c');
# INSERT 0 3
# weather_db=# INSERT INTO table2 (num, value) VALUES
# weather_db-# (1, 'xxx'),
# weather_db-# (3, 'yyy'),
# weather_db-# (5, 'zzz');
# INSERT 0 3
# weather_db=# SELECT * FROM table1;
#  num | name 
# -----+------
#    1 | a
#    2 | b
#    3 | c
# (3 rows)

# weather_db=# SELECT * FROM table2;
#  num | value 
# -----+-------
#    1 | xxx
#    3 | yyy
#    5 | zzz
# (3 rows)

# weather_db=# SELECT * FROM table1 JOIN table2;
# ERROR:  syntax error at or near ";"
# LINE 1: SELECT * FROM table1 JOIN table2;
#                                         ^
# weather_db=# SELECT * FROM table1 CROSS JOIN table2;
#  num | name | num | value 
# -----+------+-----+-------
#    1 | a    |   1 | xxx
#    1 | a    |   3 | yyy
#    1 | a    |   5 | zzz
#    2 | b    |   1 | xxx
#    2 | b    |   3 | yyy
#    2 | b    |   5 | zzz
#    3 | c    |   1 | xxx
#    3 | c    |   3 | yyy
#    3 | c    |   5 | zzz
# (9 rows)

# weather_db=# SELECT * FROM table1 CROSS JOIN table1;
# ERROR:  table name "table1" specified more than once
# weather_db=# SELECT * FROM table2 CROSS JOIN table1;
#  num | value | num | name 
# -----+-------+-----+------
#    1 | xxx   |   1 | a
#    1 | xxx   |   2 | b
#    1 | xxx   |   3 | c
#    3 | yyy   |   1 | a
#    3 | yyy   |   2 | b
#    3 | yyy   |   3 | c
#    5 | zzz   |   1 | a
#    5 | zzz   |   2 | b
#    5 | zzz   |   3 | c
# (9 rows)

# weather_db=# SELECT * FROM table1;
#  num | name 
# -----+------
#    1 | a
#    2 | b
#    3 | c
# (3 rows)

# weather_db=# SELECT * FROM table2;
#  num | value 
# -----+-------
#    1 | xxx
#    3 | yyy
#    5 | zzz
# (3 rows)

# weather_db=# SELECT * FROM table1 INNER JOIN table2 ON table1.num = table2.num;
#  num | name | num | value 
# -----+------+-----+-------
#    1 | a    |   1 | xxx
#    3 | c    |   3 | yyy
# (2 rows)

# weather_db=# SELECT * FROM table1, table2 WHERE table1.num = table2.num;
#  num | name | num | value 
# -----+------+-----+-------
#    1 | a    |   1 | xxx
#    3 | c    |   3 | yyy
# (2 rows)

# weather_db=# SELECT * FROM table1 INNER JOIN table2 USING(num);
#  num | name | value 
# -----+------+-------
#    1 | a    | xxx
#    3 | c    | yyy
# (2 rows)

# weather_db=# SELECT * FROM table1 AS t1 FULL JOIN table2 AS t2 ON t1.num = t2.num;
#  num | name | num | value 
# -----+------+-----+-------
#    1 | a    |   1 | xxx
#    2 | b    |     | 
#    3 | c    |   3 | yyy
#      |      |   5 | zzz
# (4 rows)

# weather_db=# SELECT * FROM table1 AS t1 LEFT JOIN table2 AS t2 ON t1.num = t2.num;
#  num | name | num | value 
# -----+------+-----+-------
#    1 | a    |   1 | xxx
#    2 | b    |     | 
#    3 | c    |   3 | yyy
# (3 rows)

# weather_db=# SELECT * FROM table1 AS t1 RIGHT JOIN table2 AS t2 ON t1.num = t2.num;
#  num | name | num | value 
# -----+------+-----+-------
#    1 | a    |   1 | xxx
#    3 | c    |   3 | yyy
#      |      |   5 | zzz
# (3 rows)

# weather_db=# SELECT * FROM table1 AS t1 LEFT JOIN table2 AS t2 ON t1.name = t2.name;
# ERROR:  column t2.name does not exist
# LINE 1: ...OM table1 AS t1 LEFT JOIN table2 AS t2 ON t1.name = t2.name;
#                                                                ^
# HINT:  Perhaps you meant to reference the column "t1.name".
# weather_db=# SELECT * FROM table1 AS t1 LEFT JOIN table2 AS t2 ON t1.name = t2.value;
#  num | name | num | value 
# -----+------+-----+-------
#    1 | a    |     | 
#    2 | b    |     | 
#    3 | c    |     | 
# (3 rows)

# weather_db=# SELECT * FROM table1 AS t1 right join table2 AS t2 ON t1.name = t2.value;
#  num | name | num | value 
# -----+------+-----+-------
#      |      |   1 | xxx
#      |      |   3 | yyy
#      |      |   5 | zzz
# (3 rows)

# weather_db=# SELECT * FROM table1 AS t1 LEFT JOIN table2 AS t2 ON t1.num = t2.num AND t2.value='xxx';
#  num | name | num | value 
# -----+------+-----+-------
#    1 | a    |   1 | xxx
#    2 | b    |     | 
#    3 | c    |     | 
# (3 rows)

# weather_db=# CREATE TABLE singer (
# weather_db(# id serial PRIMARY KEY,
# weather_db(# name varchar(50) NOT NULL,
# weather_db(# last_name varchar(50) NOT NULL,
# weather_db(# age int CHECK(age > 0));
# CREATE TABLE
# weather_db=# CREATE TABLE song(
# weather_db(# id serial PRIMARY KEY,
# weather_db(# title varchar(100),
# weather_db(# owner int REFERENCES singer(id),
# weather_db(# feat int,
# weather_db(# CONSTRAINT fk_feat FOREIGH KEY (feat) REFERENCES singer(id));
# ERROR:  syntax error at or near "FOREIGH"
# LINE 6: CONSTRAINT fk_feat FOREIGH KEY (feat) REFERENCES singer(id))...
#                            ^
# weather_db=# CREATE TABLE song(
# id serial PRIMARY KEY,
# title varchar(100),
# owner int REFERENCES singer(id),
# feat int,FOREIGH KEY (feat) REFERENCES singer(id));
# ERROR:  type "key" does not exist
# LINE 5: feat int,FOREIGH KEY (feat) REFERENCES singer(id));
#                          ^
# weather_db=# CREATE TABLE song(
# id serial PRIMARY KEY,
# title varchar(100),
# owner int REFERENCES singer(id),
# feat int,                                          
# FOREIGH KEY (feat) REFERENCES singer(id));
# ERROR:  type "key" does not exist
# LINE 6: FOREIGH KEY (feat) REFERENCES singer(id));
#                 ^
# weather_db=# CREATE TABLE song(
# id serial PRIMARY KEY,
# title varchar(100),
# owner int REFERENCES singer(id),
# feat int,                                          
# CONTSTRAINT fk_feat FOREIGH KEY (feat) REFERENCES singer(id));
# ERROR:  syntax error at or near "FOREIGH"
# LINE 6: CONTSTRAINT fk_feat FOREIGH KEY (feat) REFERENCES singer(id)...
#                             ^
# weather_db=# create table song(
# id serial PRIMARY KEY,
# title varchar(100),
# owner int  REFERENCES singer(id),
# feat int,
# FOREIGN KEY (feat) REFERENCES singer(id));
# CREATE TABLE
# weather_db=# \dt
#         List of relations
#  Schema |  Name   | Type  | Owner 
# --------+---------+-------+-------
#  public | cities  | table | bayel
#  public | singer  | table | bayel
#  public | song    | table | bayel
#  public | table1  | table | bayel
#  public | table2  | table | bayel
#  public | weather | table | bayel
# (6 rows)

# weather_db=# \d singer
#                                      Table "public.singer"
#   Column   |         Type          | Collation | Nullable |              Default               
# -----------+-----------------------+-----------+----------+------------------------------------
#  id        | integer               |           | not null | nextval('singer_id_seq'::regclass)
#  name      | character varying(50) |           | not null | 
#  last_name | character varying(50) |           | not null | 
#  age       | integer               |           |          | 
# Indexes:
#     "singer_pkey" PRIMARY KEY, btree (id)
# Check constraints:
#     "singer_age_check" CHECK (age > 0)
# Referenced by:
#     TABLE "song" CONSTRAINT "song_feat_fkey" FOREIGN KEY (feat) REFERENCES singer(id)
#     TABLE "song" CONSTRAINT "song_owner_fkey" FOREIGN KEY (owner) REFERENCES singer(id)

# weather_db=# \d singer
#                                      Table "public.singer"
#   Column   |         Type          | Collation | Nullable |              Default               
# -----------+-----------------------+-----------+----------+------------------------------------
#  id        | integer               |           | not null | nextval('singer_id_seq'::regclass)
#  name      | character varying(50) |           | not null | 
#  last_name | character varying(50) |           | not null | 
#  age       | integer               |           |          | 
# Indexes:
#     "singer_pkey" PRIMARY KEY, btree (id)
# Check constraints:
#     "singer_age_check" CHECK (age > 0)
# Referenced by:
#     TABLE "song" CONSTRAINT "song_feat_fkey" FOREIGN KEY (feat) REFERENCES singer(id)
#     TABLE "song" CONSTRAINT "song_owner_fkey" FOREIGN KEY (owner) REFERENCES singer(id)

# weather_db=# \d song
#                                     Table "public.song"
#  Column |          Type          | Collation | Nullable |             Default              
# --------+------------------------+-----------+----------+----------------------------------
#  id     | integer                |           | not null | nextval('song_id_seq'::regclass)
#  title  | character varying(100) |           |          | 
#  owner  | integer                |           |          | 
#  feat   | integer                |           |          | 
# Indexes:
#     "song_pkey" PRIMARY KEY, btree (id)
# Foreign-key constraints:
#     "song_feat_fkey" FOREIGN KEY (feat) REFERENCES singer(id)
#     "song_owner_fkey" FOREIGN KEY (owner) REFERENCES singer(id)

# weather_db=# INSERT INTO singer(name, last_name, age) VALUES
# weather_db-# ('Ed', 'Sheeran', 30),
# weather_db-# ('Marsha1', 'Eminem', 35),
# weather_db-# ('Imagine', 'Dragons', 10);
# INSERT 0 3
# weather_db=# SELECT * FROM singer;
#  id |  name   | last_name | age 
# ----+---------+-----------+-----
#   1 | Ed      | Sheeran   |  30
#   2 | Marsha1 | Eminem    |  35
#   3 | Imagine | Dragons   |  10
# (3 rows)

# weather_db=# INSERT INTO song(title, owner) VALUES
# weather_db-# ('Shape of you', 1),
# weather_db-# ('mockinbird', 2);
# INSERT 0 2
# weather_db=# INSERT INTO song(title, owner, feat) VALUES
# weather_db-# ('river', 2, 1);
# INSERT 0 1
# weather_db=# SELECT * FROM song;
#  id |    title     | owner | feat 
# ----+--------------+-------+------
#   1 | Shape of you |     1 |     
#   2 | mockinbird   |     2 |     
#   3 | river        |     2 |    1
# (3 rows)

# weather_db=# SELECT song.id, song.title, s.name || " " || s.last_name AS performer, s.age, song.feat FROM singer AS s, song WHERE s.id = song.owner;
# ERROR:  column " " does not exist
# LINE 1: SELECT song.id, song.title, s.name || " " || s.last_name AS ...
#                                               ^
# weather_db=# SELECT song.id, song.title, s.name || ' ' || s.last_name AS performer, s.age, song.feat FROM singer AS s, song WHERE s.id = song.owner;
#  id |    title     |   performer    | age | feat 
# ----+--------------+----------------+-----+------
#   1 | Shape of you | Ed Sheeran     |  30 |     
#   2 | mockinbird   | Marsha1 Eminem |  35 |     
#   3 | river        | Marsha1 Eminem |  35 |    1
# (3 rows)

# weather_db=# SELECT song.id, song.title, s.name || ' ' || s.last_name AS performer, s.age, song.feat FROM singer AS s, song WHERE s.id = song.owner;
'-------------------------------------------------------------------------'
'PostgreSQL'
# 1)
# SELECT plaintext FROM wordform LIMIT 10;
'-------------------------------------------------------------------------'
# 2)
# SELECT plaintext FROM wordform WHERE plaintext LIKE 'a%';
'-------------------------------------------------------------------------'
# 3)
# SELECT title, genretype FROM work WHERE genretype = 'p';
'-------------------------------------------------------------------------'
# 4)
# SELECT AVG(totalparagraphs) FROM work WHERE genretype = 't';
'-------------------------------------------------------------------------'
# 5)
# SELECT title FROM work WHERE totalwords > (SELECT AVG(totalwords) FROM work);
'-------------------------------------------------------------------------'
# 6)
# SELECT character.charname, speechcount, work.title FROM character LEFT JOIN character_work ON character.charid = character_work.charid LEFT JOIN work ON character_work.workid = work.workid;
'-------------------------------------------------------------------------'
# 7)

'-------------------------------------------------------------------------'
# 8)

'-------------------------------------------------------------------------'
# 9)

'-------------------------------------------------------------------------'
# 10)

'-------------------------------------------------------------------------'
# 11)

'-------------------------------------------------------------------------'
# 12)

'-------------------------------------------------------------------------'
# 13)

'-------------------------------------------------------------------------'
# 14)

'-------------------------------------------------------------------------'
# 15)

'-------------------------------------------------------------------------'
'Интерактив 2:'


'Files'

# Режим работы с файлами:
# 1. r/r+ (read)
# 2. w/w+ (write)
# 3. a/a+ (append)

# data = file.readlines() # считывает все строки и записывает их в список
# print(file.readline()) # печатает 1 строку
# print(file.read()) # читает файл с того места, где остановился курсор


# file.tell() - возвращает индекс где находится указатель/курсор
# file.seek(index) - перемещает курсор на индекс, который вы передали


# writelines() работает аналогично write(), однако в аргументы данная функция принимает уже не одну строку, а список состоящий из строк.


'JSON'

# JSON -- JavaScript Object Notation.
# Единый формат хранение и передачи  данных между приложениями, сайтами, сервисами и языками програмирования через сеть интернет.
# <failname>.json #файл в  формате JSON

# Json.dump -> метод записывет патйтон данные в файл  в формате JSON паралеьные сделав серализации

# Json.dumps-> метод записывет патйтон данные в строку в формате JSON паралеьнно сделав серализации

# json.load-> метод котрый счистывает файл в формате Json и переводит его в PY object

# json.loads-> метод котрый счистывает текст формате Json и переводит его в PY object


'ООП'

# Класс -> Это описание того, как должен выглядеть объект, то есть в классе мы описываем какими свойствами (данными) и поведением(функциями)должен обладать объект

# Объект -> это сущность которую мы создаем от класса , у объекта есть состояние свойства(данных)

# Целью создание было связать данные(атрибуты) с функциями(методы), которые использовали их

# Свойствами (атрибуты) называют обычные переменные внутри класса, в которых хранятся данные определенного объекта

# Методы - это обычные функции которые описывают поведение объекта функции внутри класса называют методами


'ПРИНЦИПЫ ООП:'

# 1. Наследование - позволяет принимать родительские методы и атрибуты для дочернего класса
# Множественное наследование - это когда класс наследование от двух или более классов

# 2. Инкапсуляция 
#  ⁃ Связь данных с методами, которые должны управлять этими атрибутами.
#  ⁃ Механизм языка, который позволяет ограничить доступ к определенным компонентам класса.
#  ⁃ Один класс - одна задача.

#  3 уровня доступа в питоне:
#   1. Публичный (public) - number, print_number
#   2. Защищенный (_protected, parent/child) - _number, наследуется только на 1 класс
#   3. Приватный (__private) - доступен только в текущем классе, не наследуется

'GETTER & SETTER'
#  Они используются для получения и установки значений в защищенные атрибуты, чтобы избежать прямого доступа к защищенному атрибуту, и еще с помощью сеттеров и гетторов можно добавлять логику проверки при получении данных


# 3. Полиморфизм (len(), + (__add__))
#  ⁃ способность метода обрабатывать данные разных типов (объектов от класса). Обычно это реализуется путем создания базового класса и наличия двух или более подклассов, которые все реализуют (переопределяют) методы с одинаковой сигнатурой (названием).
#  ⁃ Широко распрастраненное определение: "Один интерфейс - много реализаций".


# 4. Абстракция
# (Абстрактный класс) - его можно рассматривать как набор методов, которые должны быть реализованы во всех дочерних классах, которые будут унаследованы от абстрактного класса.

# Абстрактный метод - это метод, у которого есть объявление, но нет реализации.

# 5. Композиции
# (сильная связь) - это когда стена не существует отдельно от комнаты, она создается при создании комнаты и полностью управляется классом Комнаты.
# Сравнение со стенами в комнате, не могут существовать друг без друга.

# 6. Агрегация
# (слабая связь) - это когда экземпляр двигателя создается где-то в другом месте и передается в класс Автомобиля в качестве параметра.
# Сравнение с двигателем и кузовом авто, они могут существовать порознь и использоваться с другими составляющими.


'Магические методы (dunder - duble underscore)- методы, у которых два нижних подчеркивания в начале и в конце. Магия в том, что мы их не вызываем напрямую, а они вызываются в определенный момент либо они вызываются определенными операторами или функциями.'

# Конструктор -> __new__(cls)
# Инициализатор -> __init__(self)
# Вызываются, когда создаем объект

# Дандер методы строкового отображения объектов 
# str -> для отображения строки которую будут видеть пользователи
# repr -> строковую информацию о том, как создать объект
# len --> len(obj)
# repr --> repr(obj)
# iter - вызывается, когда итерируем объект

'МЕТОДЫ:'
# Cуществует 3 вида методов:
# 1) class methods - методы, которые принимают первым аргументом параметр CLS (ссылка на класс). Нужна они для создания объектов или изменения атрибутов класса. Для того, чтобы создать класс метод нужно воспользоваться декоратором classmethod.

# 2) instance methods - обычные методы, которые принимают первым аргументом ключевое слово self (ссылка на объект). Нужны они для того, чтобы внутри метода мы могли работать с атрибутами объекта.

# 3) static methods - это функции внутри класса, которые не взаимодействуют ни с классом, ни с объектом. Находятся они внутри класса, потому что их используют только внутри класса, так как вне они бесполезны. 

'MIXINS:'
# Микисны это классы которые будут использоваться для наследоавния, но от этих миксинов не создают объекты 
# Для чего:
# 1 вы хотите предоставить множество доп методов для класса
# 2 вы хотите использовать одну конкретенцию во множестве разных классов
'-------------------------------------------------------------------------'
'Django'

'1'
# {
#     "title": "go to coffee",
#     "body": "I want coffee from Torro",
#     "deadline": "2023-04-01",
#     "user": "Sultan Katana",
#     "status": "todo"
# }

'2'
# {
#     "title": "finish project",
#     "deadline": "2023-03-10",
#     "user": "John Snow",
#     "status": "doing"
# }

'3'
# {
#     "title": true,
#     "deadline": "2023-03-10",
#     "user": "John Snow",
#     "status": "todo"
# }

'4'

'-------------------------------------------------------------------------'


'-------------------------------------------------------------------------'


'-------------------------------------------------------------------------'


'-------------------------------------------------------------------------'


'-------------------------------------------------------------------------'


'-------------------------------------------------------------------------'


'-------------------------------------------------------------------------'


'-------------------------------------------------------------------------'


'-------------------------------------------------------------------------'


'-------------------------------------------------------------------------'


'-------------------------------------------------------------------------'


'-------------------------------------------------------------------------'


'-------------------------------------------------------------------------'


'-------------------------------------------------------------------------'


'-------------------------------------------------------------------------'


'-------------------------------------------------------------------------'


'-------------------------------------------------------------------------'


'-------------------------------------------------------------------------'


'-------------------------------------------------------------------------'


'-------------------------------------------------------------------------'


'-------------------------------------------------------------------------'


'-------------------------------------------------------------------------'


'-------------------------------------------------------------------------'


'-------------------------------------------------------------------------'


'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
'-------------------------------------------------------------------------'
