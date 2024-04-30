immutable_var = 214, 'urban', 5323.14, True, False
print(immutable_var)
print(type(immutable_var))

#immutable_var[0] = 13 :Traceback (most recent call last):
#   File "C:/Users/danii/Desktop/py/pythonProject/homework4.py", line 5, in <module>
#     immutable_var[0] = 13
# TypeError: 'tuple' object does not support item assignment
# потому что элементы в нутри кортежа не подлежат изменению - можно только добавлять и изменять данные внутри включенных в него списков)

mutable_list = ['chin-chopa', 'djArbuz', 123, False, 23.55]
mutable_list.remove(123)
mutable_list.append(False)
mutable_list.extend('02')
mutable_list.reverse()
print(mutable_list)
