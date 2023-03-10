"""
Напишите класс Salary для расчета налогов на заработную плату. У класса должна быть обязательная переменная класса - процент налога от зарплаты - 15%. Объекты класса должны иметь сумму зарплаты и стаж работы в качестве атрибутов. Также у класса должен быть метод расчитывающий сумму налога заплаченного за весь стаж работы. Создайте экземпляр класса и посчитайте сумму вашего налога.
"""

# class Salary:
#     precent = 0.15
#     def __init__(self, sum_salary, experience):
#         self.sum_salary = sum_salary
#         self.work_exp = experience

#     def sum_of_tax(self):
#         res = (self.sum_salary * self.precent) * (self.work_exp * 12)
#         print(f'Сумма налогов составила {res} сомов, за {self.work_exp} лет!')

# sal = Salary(170_000, 11)
# sal.sum_of_tax()

# class Calc:
#     def add(self, a, b):
#         '''Функция суммы'''
#         return a + b
    
#     def sqrt(self, num):
#         '''Функция нахождения квадратного корня'''
#         import math
#         res = math.sqrt(num)
#         return round(res, 2)
    
#     def percent(self, num, percent):
#         '''Функция нахождения процента от числа'''
#         return (num * percent) / 100

#     def super_func(self, string):
#         '''Функция выполняет вычисление в строке'''
#         '1 + 1 + 2 + 3'
#         try:
#             return eval(string)
#         except:
#             return 'Invalid Operation'


# calc = Calc()
# print(calc.add(4, 5)) # 9
# print(calc.sqrt(9)) # 3.0
# print(calc.sqrt(2)) # 1.41
# print(calc.percent(87, 35)) # 30.45
# print(calc.percent(255, 25)) # 63.75
# print(calc.super_func('(5 -7) ** 2 - 10')) # -6
# print(calc.super_func(input('Введите операцию: ')))

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


# class CRUD:
#     __products = []
#     __id = 0

#     def _get_id(self):
#         self.__id += 1
#         return self.__id

#     def _get_product(self, id):
#         for x in self.__products:
#             if x ['id']==id: return x
#         return False

#     def create(self):
#         print('CREATE of product!')
#         title = input('Введите название продукта: ')
#         price = input('Введите цену: ')
#         self.__products.append({
#             'id': self._get_id(),
#             'title': title,
#             'price': price
#         })

    
#     def list_of_products(self):
#         print('Все наши продукты: ')
#         for x in self.__products:
#             print(x['title'])

#     def detail_product(self):
#         print('Detail:')
#         id = int(input('Введите ID  продукта: '))
#         product = self._get_product(id)
#         print(product if product else 'нет такого продукта!!')


#     def update_product(self):
#         print('Update:')
#         id = int(input('Введите ID  продукта: ')) # 5
#         product = self._get_product(id)
#         if not product:
#             print('Нет такого продукта!')
#             return
#         choice = input('Что изменить(title/price): ')
#         index = self.__products.index(product)
#         self.__products[index][choice] = input('Введите новое значение: ')

#     def delete_product(self):
#         print('DELETE:')
#         id = int(input('Введите ID  продукта: '))
#         product = self._get_product(id)
#         if not product:
#             print('Нет такого продукта!')
#             return
#         self.__products.remove(product)
#         print('Удалено!')

# product = CRUD()
# product.create()
# product.create()
# product.list_of_products()
# # product.detail_product()
# # product.detail_product()
# # product.update_product()
# # product.detail_product()
# product.delete_product()
# product.list_of_products()

