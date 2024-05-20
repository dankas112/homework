def test(n, *args, hota='under', kek=False, **kwargs):
    print(f' (hota, kek) : {hota, kek} - это переменные с заднаныыми значениями по умолчанию, '
          f'которые будут изменены, только если указать именно их изменение;'
          f' (n) : {n} - принимает в себя 1е значение до args,'
          f' (args) : {args} - принимает в себя все значенния после n, объениняя их в 1 список'
          f'(kwargs) : {kwargs} - принимает в себя все переменные со значениями, которых нет в функции')


test(5, True, 'Инокентий', 'efw', hota='near', basa='фундамент', number='число')


def factorial(n, s=0):
    if n != 0:
        return n + factorial(n-1)
    else:
        return 0


print(factorial(10))
