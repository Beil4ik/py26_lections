# import json
# class MyBook:
    
#     id = 0
#     country = 'Kyrgyzstan'

#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price

#     def create(self):

#         MyBook.id += 1

#         with open('db.json') as file:
#             list_ = json.load(file)
            
#         with open('db.json', 'w') as file:
#             dict_ = {'id': self.id, 'title': self.title, 'author': self.author, 'price': self.price}
#             list_.append(dict_)
#             list_json = json.dumps(list_)
#             file.write(list_json)

#     @staticmethod
#     def read():
#         with open('db.json') as file:
#             list_json = file.read()
#             list_ = json.loads(list_json)
#             print(list_)

#     @staticmethod
#     def delete(id):
#         with open('db.json') as file:
#             list_ = json.load(file)
#         with open('db.json', 'w') as file:
#             list_2 = list_.copy()
#             for obj in list_2:
#                 if id == obj['id']:
#                     list_.remove(obj)
#                     list_json = json.dumps(list_)
#                     file.write(list_json)

#     @staticmethod
#     def update(id, pole, a):
#         with open('db.json') as file:
#             list_ = json.load(file)
#         with open('db.json', 'w') as file:
#             list_2 = list_.copy()
#             for obj in list_2:
#                 if id == obj['id']:
#                     obj[pole] = a
#                     res = json.dumps(list_2)
#                     file.write(res)

            


# book_1 = MyBook('Katana', 'Sultan', '100$')
# book_1.create()

# book_2 = MyBook('MyLife', 'Aigerim', '200$')
# book_2.create()

# MyBook.delete(1)
# MyBook.update(2, 'title', 'Anton')
# MyBook.read()

'-------------------------------------------------------------------------------------' 
# CLassroom
'Task 1'

# class Human:
#     def __init__(self):
#         print('init worked')
#         self.rachel = 'rachel'
    
#     def method1(self):
#         self.rachel = 'John'
#         print('method1 worked')

# obj = Human()
# print(obj.rachel)
# obj.method1()
# print(obj.rachel)

# import random

# class Sniper:
#     def __init__(self, name):
#         self.name = name
#         self.hp = 100
    
#     def shoot(self, sniper):
#         sniper.hp -= 20

# sniper1 = Sniper(name = 'Beil4ik')
# sniper2 = Sniper(name = 'Nuuman')

# snipers = (sniper1, sniper2)

# while True:
#     shooter = random.choice(snipers)
#     if shooter == sniper1:
#         shot = sniper2
#     else:
#         shot = sniper1

#     shooter.shoot(shot)
#     print(f'Снайпер {shooter.name} стреляет! У {shot.name} осталось {shot.hp} хп')
#     if sniper1.hp == 0:
#         print(f'{sniper1.name} умер! {sniper2.name} выиграл!')
#         break
#     elif sniper2.hp == 0:
#         print(f'{sniper2.name} умер! {sniper1.name} выиграл!')
#         break
#     else:
#         continue

'Task 2'

# class Hogwarts:
#     faculties_hogwarts = {'courage': 'Gryffindor', 'intelligence': 'Ravenclaw', 'justice': 'Hufflepuff', 'ambition': 'Slytherin'}

#     def __init__(self, courage, intelligence, justice, ambition):
#         self.courage = courage
#         self.intelligence = intelligence
#         self.justice = justice
#         self.ambition = ambition
#         self.qualities = locals()
#         # print(self.qualities)

#     def sorting_hat(self):
#         dict_ = {val: key for key, val in self.qualities.items() if type(val) == int}
#         # print(dict_)
#         maximum_point = max(dict_.keys())
#         # print(maximum_point)
#         maximum_quality = dict_[maximum_point]
#         # print(maximum_quality)
#         self.faculty = Hogwarts.faculties_hogwarts[maximum_quality]
#         print(f'{self.faculty}')

# # student1 = Hogwarts(courage = 5, intelligence = 8, justice = 3, ambition = 9)
# # student1.sorting_hat()

# # student2 = Hogwarts(courage = 8, intelligence = 6, justice = 1, ambition = 0)
# # student2.sorting_hat()

# # student3 = Hogwarts(courage = 4, intelligence = 7, justice = 3, ambition = 2)
# # student3.sorting_hat()

# student4 = Hogwarts(courage = 1, intelligence = 7, justice = 10, ambition = 8)
# student4.sorting_hat()


'Task'

'''
1) Создайте класс Languages. В этом классе должен быть атрибут класса, который обозначает количество студентов, изучающих какой-либо язык программирования. От класса Languages создайте два дочерних класса: Python, JavaScript. В них  также должны быть атрибуты, указывающие на количество студентов, изучающих тот или иной язык. При создании объекта-студента от одного из дочерних классов, автоматически количество студентов в классах меняется. Если студент изучает язык Python, то количество студентов должно увеличиться на один и в классе Python и в классе Languages. Аналогично со студентами JavaScript. Далее, в дочерних классах должен быть переопределен метод coding, в классе Python он должен выдавать вам строку “I am Python student. I am coding now.”, а в классе JavaScript - “I am JavaScript student. I am coding now”. Создайте двух студентов от двух дочерних классов. Далее программа сама рандомно выбирает студента и предлагает вам угадать, какого студента она выбрала. После вашего выбора, он вызывает метод coding у загаданного студента и выдает вам результат: если вы отгадали правильно, пишет “Good job!”, если нет - “No bueno :(”
'''
class Languages:

  class Python:
    pass

  class JavaScript:
    pass