def int_func(str_: str):
    return str_[0].capitalize() + str_[1:]


input_string = input('Введите строку: ')
print(' '.join([int_func(el) for el in input_string.split(' ')]))
