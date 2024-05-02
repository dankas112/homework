x = 38 # 1 screenshot

print('дратути!')
if x < 0:
    print('меньше нуля')
print('дотвидания')



a, b = 10, 5 # 2 screenshot

if a > b:
    print('a > b')

if a > b and a > 0:
    print('успех')

if (a > b) and (a > 0 or b < 1000):
    print('успех')

if 5 < b and b < 10:
    print('успех')



if '34' > '123': # 3 screenshot (между собой можно сравнивать что угодно)
    print('успех')

if '123' > '12':
    print('успех')

if [1, 2] > [1, 1]:
    print('успех')



if '6' > 5: # 4 screenshot (нельзя сравнивать разные типы)
    print('успех')

if [5, 6] > 5:
    print('успех')

if '6' != 5:
    print('успех')