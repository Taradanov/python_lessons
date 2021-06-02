list_of_elements = (True, 1, '1', 1.0, ValueError('Блаблабла'))

for el in list_of_elements:

    if type(el) is bool:
        print('Это булево')

    elif type(el) is str:
        print('Это строка')

    elif type(el) is int:
        print('Это целое число')

    elif type(el) is float:
        print('Это флоат)))')

    elif type(el) is ValueError:
        print('Это ошибка')
