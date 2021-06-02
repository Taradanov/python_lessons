
def my_func_1(x, y):
    return 1/x**y

def my_func_2(x, y):
    temp_x = 1
    for i in range(0, y):
        temp_x *= x
    return 1/temp_x

input_x = input('Введите x ')
if not input_x.isdigit():
    raise ValueError('Ошибка преобразования значения к числу')

input_y = input('Введите y (без минуса): ')
if not input_y.isdigit():
    raise ValueError('Ошибка преобразования значения к числу')

x = int(input_x)
y = int(input_y)

print(my_func_1(x, y))
print(my_func_2(x, y))

