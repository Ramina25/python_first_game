# импорт библиотеки в системуа
import random

# присвоение переменной значений кортежа
words_list = ('линейка', 'карандаш', 'ластик', 'ручка',
              'пенал', 'циркуль', 'корректор')

# реализация рандомного выбора из переменной words_list
secret_word = random.choice(words_list)
# print(secret_word)

# слово secret_word из рандомного выбора, скрытое от пользователя звездочками
users_word = ['*'] * len(secret_word)
# print(''.join(users_word))
#
# users_word[2] = 'у'
# print(''.join(users_word))

# присвоение переменной алфавита в виде кортежа
kirill = 'абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
print('Загадано слово из канцелярии. Допустимо 7 ошибок')

# счетчик ошибок
errors_counter = 0

while True:
    letter = input('введите ОДНУ букву: ').lower()  # берем введеную букву
    if len(letter) != 1 or not letter in kirill:  # фильтрация ввода - только одна буква, только кириллица
        continue
    if letter in secret_word:  # проверка: есть ли буква из переменной letter в загаданном слове secret_word
        for pos, sym in enumerate(secret_word):  # присвоение каждой букве позиции из загаданного слова
            # print(pos, sym)
            if sym == letter:  # в случае если sym совпал с введенной буквой
                users_word[pos] = sym  # звездочку меняем на конкретный символ
        if '*' not in users_word:  # проверка, что слово угадано, нет звездочек в слове игрока
            print('вы выйграли! :)')
            print('\t\tбыло загадано слово', secret_word.upper())
            yes = input('сыграем еще? для согласия, введи + : ')
            if yes == '+':
                errors_counter = 0
                secret_word = random.choice(words_list)
                users_word = ['*'] * len(secret_word)
                continue
            else:
                print('до встречи')
                break
    else:
        errors_counter += 1  # если игрок не угадал, к счетчику прибавляется единица
        print('\tошибок допущено: ', errors_counter)
        if errors_counter == 8:  # условие на количество ошибок
            print('вы проиграли :(')
            yes = input('сыграем еще? для согласия, введи + : ')
            if yes == '+':
                errors_counter = 0
                secret_word = random.choice(words_list)
                users_word = ['*'] * len(secret_word)
                continue
            else:
                print('до встречи')
                break

    print(''.join(users_word))  # выводит угаданные части слова вместе со скрытыми под звездочками

print(input('для выхода нажмите любую клавишу: '))
