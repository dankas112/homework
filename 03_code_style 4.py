# -*- coding: utf-8 -*-

# блоки кода

num1 = 10
num2 = 29

if num1 < 0:
    print('Х меньше нуля')
    result = num1 ** 2 + num2
else:
    print('Х больше нуля')
    result = num1 - num2
print('Результат', result)

# ср. с С++

# if (x < 0) { printf('Меньше нуля\n'); z = x**2 + y; } else { printf('Больше нуля\n'); z = x - y; } printf('Получается\n', z)

# вложенные блоки кода

name = input('Enter your name >>>')
if name == 'Ola':
    opponent = 'Ola'
else:
    if name == 'Sofi':
        opponent = 'Sofi'
    else:
        if name == 'Katy':
            opponent = 'Katy'
        else:
            opponent = 'anonymous'
print(f'Hi, {opponent}!')

# оператор pass

if num1 < 0:
    if num2 > 0:
        result = -num1 + num2
    else:
        result = -num1 - num2
else:
    result = num1 + num2

# соглашения о стиле кода
# PEP8 (Python Enhancement Proposal 8) - описан "правильный" стиль программирования в пайтон
# https://www.python.org/dev/peps/pep-0008/

# 4 пробела на каждый уровень отступа

if num1 < 0:
    if num2 > 0:
        pass
    else:
        print('направо!')
else:
    print('стой!')

# Максимальная длина строки

my_poem = ['Варкалось, хливкие шорьки пырялись по наве', 'И хрюкотали зелюки как мюмзики в мове',
           'О бойся Бармаглота, сын! Он так свирлеп и дик', 'А в глуше рымит исполин - Злопастный Брандашмыг!', ]

# пробелы в операторах

num1 = 2
num2 = num1 * num1 + 1
is_big = num1 >= 3000

num1 = my_poem[-1]
print(num1)
my_list = [2, 3, 4, 5, 6]

# reformat кода

num1 = 3
num2 = 8

if num1 == 3:
    print(42)
if num1 < 0:
    if num2 > 0:
        print('налево!')
    else:
        print('направо!')
else:
    print(
        'стой!')

# названия переменных

my_pets = 34
if my_pets > 10:
    print('I need more space for my pets!')

my_favorite_pets = ['cat', 'wolf', 'ostrich']
if 'lion' in my_favorite_pets:
    print('Wow!')

MyFavoritePetsAndBirds = ['cat', 'wolf', 'ostrich']
# но такой стиль используется для названий классов


# рекомендации PEP8

# b (одиночная маленькая буква)
# B (одиночная заглавная буква)
# но лучше использовать только такие однобуквенные имена
#   i j k - для циклов
#   x y z - для координат

# никогда не используйте в названиях переменных одиночные l, I, O  !
num1 = 34
num2 = 43
if num1 > num2:
    print()

num3 = 9
if num3 > 0:
    print()

# lowercase (слово в нижнем регистре)
# lower_case_with_underscores (слова из маленьких букв с подчеркиваниями)
# UPPERCASE (заглавные буквы)
# UPPERCASE_WITH_UNDERSCORES (слова из заглавных букв с подчеркиваниями)

# CapitalizedWords (слова с заглавными буквами, или CapWords, или CamelCase).
#   Замечание: когда вы используете аббревиатуры в таком стиле, пишите все буквы аббревиатуры заглавными —
#   HTTPServerError лучше, чем HttpServerError.

# mixedCase (отличается от CapitalizedWords тем, что первое слово начинается с маленькой буквы)
# Capitalized_Words_With_Underscores (слова с заглавными буквами и подчеркиваниями — уродливо!)


# автоматическое переименование в PyCharm и подсказки - вам не нужно набирать длинные названия переменных

ss = ['cat', 'wolf', 'ostrich']
if 'lion' in ss:
    print('Wow!')

# В каждой уважающей себя компании есть style guide (стайл-гайд) - руководство по стилю написания кода.
# Практически все они основываются на PEP8, с небольшими исключениями, принятыми в этой команде.
# Как пример стайл-гайда небольшой компании рекомендую почитать
# https://github.com/best-doctor/guides/blob/master/guides/python_styleguide.md
