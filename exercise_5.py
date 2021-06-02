
def summ():
    summ = 0
    while True:
        input_str = input('Введите строку чисел через пробел, или "exit" для отмены: ')
        for substr in input_str.split(' '):
            if substr == 'exit':
                return summ
            if substr.isdigit():
                summ += int(substr)
        print(summ)

print(summ())
