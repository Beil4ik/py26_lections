'-------------------------------------------------------------------------'
# obj = ['John', 'Snow', 24, 500, '+996709890980', 'Winterfell'] 
# obj = {'name': 'John', 'last_name': 'Snow', 'age':24, 'cash': 500, 'phone_number': '+996709890980'}
# print(obj['name'])
# print(obj['cash'])

#dict()- Словарь-> упорядочная коллекция элементов (python 3.7-> ordered). Каждый элемент внутри словаря содержится в паре ключ:значение

# Ключи должны быть неизменяемым типом данных( str, int,tuple etc.),тогда как значениями могут выступить любые типы данных.

# thisdict = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
# print(thisdict)
# print(type(thisdict))


# ассоциативный массив, hash table, object(js)
#structure == dictionary(py)
'-------------------------------------------------------------------------'

# user_info = {'fisrt_name': 'john', 'last_name': 'Snow', 'age': 23, 'email': 'John@73gamil.com', 'role': 'modertor '}
# print(user_info)
# print(user_info.get('first_name'))#none
'-------------------------------------------------------------------------'

# user_info = {'fisrt_name': 'john', 'last_name': 'Snow', 'age': 23, 'email': 'John@73gamil.com', 'role': 'modertor '}
# print(dir(dict))

# print(user_info.values())
# print(user_info.keys())
# print(user_info.items())
# print(user_info)

# for key, value in user_info.items():
#     print(key, value)
'-------------------------------------------------------------------------'

#Решение четного не четного
# dict_ ={1: 15, 2: 11, 3: 18, 4:5, 5: 21}
# for key, value in dict_.items():
#     if key % 2 == 0:
#         print(key, 'Чётное') 
#     else:
#         print(key, 'Нечётное')
#         dict_[key] = value ** 2

# print(dict_)


# a = (1, 2,)
# print(a, type(a))

# num1, num2 = a
# print(num1)
# print(num2)
'-------------------------------------------------------------------------'

# изменения словаря
# dict_ = {'name': 'John', 'age': 24}
# print(dict_)
# dict_['age'] = 23
# dict_['address'] = 'Winterfell'
# print(dict_)


# dict_ = {'name': 'John', 'age': 24}
# print(dict_)
# dict_.update({'age': 18, 'address': 'Winterfell'})
# print(dict_)

'-------------------------------------------------------------------------'

# fromkeys - быстрое создание словаря из ключей
# keys = ['one', 'two', 'three']

# new_dict = dict.fromkeys(keys, 'value')
# print(new_dict)

# dict_ = {}
# ls = list(range(1, 101))

# new_dict = dict_.fromkeys(ls, 'value')
# print(new_dict)

'-------------------------------------------------------------------------'

# setdefault - работает также, как и метод get(), но если нет такого ключа, то он создаст новый

# dict_ = {'name': 'John', 'age': 24}
# print(dict_)
# print(dict_.setdefault('age'))
# print(dict_.setdefault('name'))
# print(dict_.setdefault('address', 'Moscow str.'))
# print(dict_)

'-------------------------------------------------------------------------'

# удаление из словаря
# pop(key) - удаляет элемент по ключу

# dict_ = {'name': 'John', 'last_name': 'Snow', 'address': 'Winterfell'}
# print(dict_)
# removed = dict_.pop('address')
# print(removed)
# print(dict_)

'-------------------------------------------------------------------------'

# popitem() - удаляет последний элемент 
# dict_ = {'name': 'John', 'last_name': 'Snow', 'address': 'Winterfell'}
# print(dict_)
# removed = dict_.popitem()
# print(dict_)
# print(removed)
'-------------------------------------------------------------------------'
# dict_ = {'name': 'John', 'last_name': 'Snow', 'address': 'Winterfell'}
# print(dict_)
# removed = dict_.popitem()
# print(dict_)
# key, value = removed
# print(key, value)

'-------------------------------------------------------------------------'

# roles = {
#     0: 'Moderator',
#     1: 'Admin',
#     2: 'Customer',
#     3: 'Vendor'
# }

# users = {
#     '1': {'username': 'JohnSnow', 'role': roles[1]},
#     '2': {'username': 'JamieLanister', 'role': roles[2]},
#     '3': {'username': 'Mufasa', 'role': roles[3]}
# }
# # print(users['1']['role'])

# product = {
#     'id': 1,
#     'title': 'Iphone 14 Pro Max',
#     'description': 'Lorem Ipsum',
#     'price': 200
# }
# i = '1'
# while i == '1' or i == '2':
#     i = input('Введите что хотите сделать:\nЕсли хотите просмотреть товар, то нажмите1\nЕсли хотите изменить товар, то нажмите  2\nЕсли хотите выйти, то нажмите 3 или что-то другое\nВаш выбор: ')

#     if i == '1':
#         print(product)
#     elif i == '2':
#         id_user = input('\nВведите ваш id: ')
#         if not users.get(id_user):
#              print('Нет такого юзера!')
#         elif users.get(id_user)['role'] == roles[1]:
#             print(users.get(id_user))

#             choice = input('Введите что изменить(title, description, price): ')
#             new = input(f'Введите новое значение {choice}: ')
#             product.update({choice: new})
#             print('Updated!')
#         else:
#             print('Сорри, только админ может редактировать! У тебя нет разрешения!')

'---------------------------------------------------------------------------------------'

