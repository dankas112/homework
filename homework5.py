fruits = ['apple', 'waterlemon', 'orange', 'lime', 'banana']
print(f'список: {fruits}')
print(f'первый элемент: {fruits[0]}, последний элемент: {fruits[-1]}')
print(f'элементы с 3го по 5й: {fruits[2:6]}')
fruits[2] = 'apple'
print(f'измененный список: {fruits}')
print('_______________')
my_dict = {'car': 'машина', 'code': 'код', 'hat': 'шляпа', 'rain': 'дождь'}
print(f'словарь: {my_dict}')
print('перевод: ', my_dict.get('car'))
my_dict['car'] = 'автомобиль'
my_dict['close'] = 'закрывать'
print(f'измененный словарь: {my_dict}')
