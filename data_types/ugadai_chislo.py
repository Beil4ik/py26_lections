from random import randint

x = randint(1, 10)
user_num = 0
popytki = 0

while True:
    print('Я загадал число от от 1 до 10, угадайте его :)')
    user_num = int(input('Ваша догадка: '))
    popytki += 1
    if user_num == x:
        print('Молодец, ты угадал число!\nКоличество твоих попыток: ' + str(popytki) + '\nСпасибо за игру!')
        break

randint = input('Хотите продолжить(yes/no)? ')