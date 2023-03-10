# import random

# ls = ['Plov', 'Manty', 'Kuurdak', 'Lagman', 'Oromo']
# p = 0
# m = 0
# k = 0
# l = 0
# o = 0

# for x in range(0, 1_000):
#     # print(x)
#     choice = random.choice(ls)
#     # print(choice)
#     if choice.lower() == 'plov':
#         p += 1
#     elif choice.lower() == 'manty':
#         m += 1
#     elif choice.lower() == 'kuurdak':
#         k += 1
#     elif choice.lower() == 'lagman':
#         l += 1
#     elif choice.lower() == 'oromo':
#         o += 1
    
# print('Результаты голодных игр:')
# print(f'Plov: {p}\nManty: {m}\nKuurdak: {k}\nLagman: {l}\nOromo: {o}')


'-------------------------------------------------------------------------'
'Виселица'

# from random import choice

# gallows = (
#     """
#     +----+
#     |    |
#     |
#     |
#     |
#     |
#     |
#     ==========
#     """, 
#     """
#     +----+
#     |    |
#     |    0
#     |
#     |
#     |
#     |
#     ==========
#     """, 
#     """
#     +----+
#     |    |
#     |    0
#     |    |
#     |
#     |
#     |
#     ==========
#     """,
#     """
#     +----+
#     |    |
#     |    0
#     |   /|
#     |
#     |
#     |
#     ==========
#     """,
#     """
#     +----+
#     |    |
#     |    0
#     |   /|\\
#     |
#     |
#     |
#     ==========
#     """,
#     """
#     +----+
#     |    |
#     |    0
#     |   /|\\
#     |   /
#     |
#     |
#     ==========
#     """,
#     """
#     +----+
#     |    |
#     |    0
#     |   /|\\
#     |   / \\
#     |
#     |
#     ==========
#     """
# )

# max_incorrect = len(gallows)
# words = ('makers', 'bootcamp', 'hangman', 'книга', 'пукерс', '')

# word = choice(words)
# so_far = '*' * len(word)
# wrong = 0
# used = []

# while wrong < max_incorrect and so_far != word:
#     print(gallows[wrong])
#     print('\nВы использовали следующие буквы:\n', used)
#     print('\nНа данный момент слово выглядит вот так:\n', so_far)

#     guess = input('\nВведите букву: ')

#     while guess in used:
#         print('Вы уже угадали эту букву', guess)
#         guess = input('Введите букву: ')

#     used.append(guess)

#     if guess in word:
#         print('\nДа! Буква \'' + guess + '\' есть в слове!')

#         new = ''
#         for i in range(len(word)):
#             if guess == word[i]:
#                 new += guess
#             else:
#                 new += so_far[i]

#         so_far = new
#     else:
#         print('\nИзвините, буквы \'' + guess + '\' нет в слове.')
#         wrong += 1

# if wrong == max_incorrect:
#     print('\nВас повесили! Вы проиграли!')
# else:
#     print('\nВы угадали слово! Поздравляю!')

# print('\nЗагаданное слово было:', word)
'-------------------------------------------------------------------------'
# from random import randint

# x = randint(1, 10)
# user_num = 0
# popytki = 0

# while True:
#     print('Я загадал число от от 1 до 10, угадайте его :)')
#     user_num = int(input('Ваша догадка: '))
#     popytki += 1
#     if user_num == x:
#         print('Молодец, ты угадал число!\nКоличество твоих попыток: ' + str(popytki) + '\nСпасибо за игру!')
#         break

# randint = input('Хотите продолжить(yes/no)? ')