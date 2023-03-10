# 1) %s

# name_1 = input('Введите своё имя: ')
# name_2 = input('Введите своё имя: ')
# print('Привет, меня зовут')

# 2) .format

# name = input('Введите своё имя: ')
# age = 25
# result = Привет, моё имя {}, 

# 3) f'строки'

# name = input('Введите своё имя: ')

#  result = f'Привет, {name}, как твои дела?'
#  print(result)


'==========================Экранирование строк==============================='

"""
\n - перенос строки
\t - горизонтальная табуляция
\v - вертикальная табуляция
"""

# print('hello world\nmy name is Anton\nI\'m Sabina\'s mom')
# print('hello world\n\tmy name is Gustaph')
# print('Hello world\vSup')
# print('Hello world\n\tSup')

'===================================Методы строк==================================='

# print(dir(str)) #dir - вывод список методов

'REPLASE'
#str.replase(старое значение, новое значение, кол-во) - это метод строк, который меняет старое значение на новое, если указать количество, то поменяет столько сколько раз мы указали кол-во

# text = 'ha ha ha ha'
# result = text.replace('a','o', 2) # ho ho ha ha
# print(result)

'STRIP'
#str.strip() - метод строк, который убирает пробелы в начале в конце строки

# text = '    hello world     '
# result = text.strip()
# print(text)
# print(result)

# print(len(text))
# print(len(result))

#str.rstrip - убирает пробелы справа(в конце)
# text = '    hello world       '
# result = text.rstrip() # убирает справа все пробелы
# print(result) #'hello world     '
# print(len(result)) # 15

# str.lstrip - убирает пробелы слева(в начале)
# text = '    hello world       '
# result = text.lstrip() # убираeт слевa все пробелы
# print(result) # '    hello world'
# print(len(result)) # 17

'ISDIGIT, ISNUMERIC, ISDECIMAL'
#str.isdigit()
#str.isnumeric() - эти методы строк, которые проверяют являются ли наша строка полностью из чисел
#str.isdecimal()

# text = '25'
# print(text.isdigit()) # True
# print(text.isnumeric()) # True
# print(text.isdecimal()) # True

# age = input('Введите свой возраст: ')
# print(age.isdigit())


'ISALPHA'
#str.isalpha() - это метод строк, который проверяет состоит ли наша строка только из латиницы или киррилицы'

# text = 'hello  world'
# print(text.isalpha()) #False, так как пробел это не киррилица или латиница

# text_2 = 'helloworld'
# print(text_2.isalpha()) #True, так как вся строка состоит из латиницы


'ISALNUM'
#str.isalnum() - это метод, который проверяет состоит наша строка полностью из чисел и символов латинского или киррильского алфавита

# text = 'abdc25'
# print(text.isalnum()) #True, так как строка состоит из латиницы и чисел

# text_2 = 'abcdfs    25'
# print(text_2.isalnum()) #False, так как есть символы(пробелы, плюс, равно и т.д.)


# text_3 = '12312'
# print(text_3.isalnum()) #True


'ISLOWER, ISUPPER'
#str.islower - метод строк, который проверяет на нижний регистр(с маленькой буквы)
#str.isupper - метод строк, который проверяет на верхний регистр(с большой буквы)

# text = 'makers'
# print(text.islower()) #True
# print(text.isupper()) #False
 
# text2 = 'MaKeRs'
# print(text2.islower()) #False
# print(text2.isupper()) #False


'ISTITLE'
#str.istitle - это метод строк, который проверяет начинается ли каждое слово с верхнего регистра(с большой буквы)

# name = 'sultan talaibekov'
# name2 = 'Sultan Talaibekov'
# print(name.istitle()) #False
# print(name2.istitle()) #True

# text = 'Sultan talaibekov'
# print(text.istitle()) #False


'INDEX'
#str.index(values, start, end) - это метод строк, который возвращает индекс заданного значения(values)

# text = 'makers bootcamp'
# print(text.index('a', 7)) # 12, ищет в слове bootcamp


'COUNT'
# str.count(values, start) - это метод строк, который считает сколько у нас значений(values) есть в строке

# text = 'codingiseasyisdasdasfirfgifgh'
# print(text.count('i')) #5, начинает искать от начала до конца

# print(text.count('i', 5)) #4, начинает искать с 5 индекса до конца

# print(text.count('i', 5, 9)) #1 начинает искать с 5 индекса до 9(не включительно)


'FIND'
# str.find(values, start, end) - это метод строк, такой же как и метод строк str.index(смотрите выше), но он выведет ошибку, если значение (values) нету в строке, он просто вернёт индекс -1

# text = 'makers bootcamp'
# print(text.find('z')) # распечатает -1

# text = 'makers bootcamp'
# print(text.index('z')) #распечатает ValueError(not found)


'SWAPCASE'
#str.swapcase() - это метод строк, который меняет на противоположный регистр (а->A), (A->a) (makers)->(MAKERS) (mAkErs)->(MaKeRS)

# text = 'codingiseasy'
# print(text.swapcase()) #CODINGISEASY

# text2 = 'CODINGISEASY'
# print(text2.swapcase()) #codingiseasy

# text3 = 'CodinGisEASy'
# print(text3.swapcase()) #cODINgISeasY

# text4 = input('Enter your text: ')
# print(text4.swapcase())


'CAPITALIZE'
#str.capitalize() - это метод строк, который меняет первую букву строки на верхний регистр, остальные на нижний

# text = 'hi, My Name is Anton' #Hi, my name is Anton
# print(text.capitalize())


'TITLE'
#str.title() - это метод строк, который переводит начало каждого слова в строке в верхний регистр

# text = 'hi my name is ghustaph'
# print(text.title()) #Hi My Name Is Ghustaph

'SPLIT'
# #str.split(разделитель) - это метод строк, который строку переводит в лист при помощи разделителя

# text = input('Введите числа через запятую: ')
# print(text.split(',')) #['13', '24', '54', '45']

# text2 = 'Hi my name is Ghustaph'
# print(text2.split()) #['Hi', 'my', 'name', 'is', 'Ghustaph']


'JOIN'
#'соеденитель'.join(list) - это метод строк, который соеденят элементы листа

# list_ = ['12', '23', '54', '25']

# print(' '.join(list_))



