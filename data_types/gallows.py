from random import choice

gallows = (
    """
    +----+
    |    |
    |
    |
    |
    |
    |
    ==========
    """, 
    """
    +----+
    |    |
    |    0
    |
    |
    |
    |
    ==========
    """, 
    """
    +----+
    |    |
    |    0
    |    |
    |
    |
    |
    ==========
    """,
    """
    +----+
    |    |
    |    0
    |   /|
    |
    |
    |
    ==========
    """,
    """
    +----+
    |    |
    |    0
    |   /|\\
    |
    |
    |
    ==========
    """,
    """
    +----+
    |    |
    |    0
    |   /|\\
    |   /
    |
    |
    ==========
    """,
    """
    +----+
    |    |
    |    0
    |   /|\\
    |   / \\
    |
    |
    ==========
    """
)

max_incorrect = len(gallows)
words = ('makers', 'bootcamp', 'hangman', 'книга', 'пукерс', 'виселица')

word = choice(words)
so_far = '*' * len(word)
wrong = 0
used = []

while wrong < max_incorrect and so_far != word:
    print(gallows[wrong])
    print('\nВы использовали следующие буквы:\n', used)
    print('\nНа данный момент слово выглядит вот так:\n', so_far)

    guess = input('\nВведите букву: ')

    while guess in used:
        print('Вы уже угадали эту букву', guess)
        guess = input('Введите букву: ')

    used.append(guess)

    if guess in word:
        print('\nДа! Буква \'' + guess + '\' есть в слове!')

        new = ''
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]

        so_far = new
    else:
        print('\nИзвините, такой буквы \'' + guess + '\' нет в слове.')
        wrong += 1

if wrong == max_incorrect:
    print('\nВас повесили! Вы проиграли!')
else:
    print('\nВы угадали слово! Поздравляю!')

print('\nЗагаданное слово было:', word)