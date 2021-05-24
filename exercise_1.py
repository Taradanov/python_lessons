def divide(dividend, divider):
    return dividend/divider


if __name__ == '__main__':

    input_dividend = input('Введите делимое ')
    if not input_dividend.isdigit():
        raise ValueError('Ошибка преобразования делимого к числу')

    input_divider = input('Введите делитель ')
    if not input_divider.isdigit():
        raise ValueError('Ошибка преобразования делителя к числу')

    dividend = int(input_dividend)
    divider = int(input_divider)

    if divider == 0:
        raise ValueError('На ноль делить нельзя')

    print(divide(dividend, divider))
