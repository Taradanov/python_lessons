month_list = ('Январь',
              'Февраль',
              'Март',
              'Апрель',
              'Май',
              'Июнь',
              'Июль',
              'Август',
              'Сентябрь',
              'Октябрь',
              'Ноябрь',
              'Декабрь',
              )
month_dict = {1: 'Январь',
              2: 'Февраль',
              3: 'Март',
              4: 'Апрель',
              5: 'Май',
              6: 'Июнь',
              7: 'Июль',
              8: 'Август',
              9: 'Сентябрь',
              10: 'Октябрь',
              11: 'Ноябрь',
              12: 'Декабрь',
              }

number_of_month = input('Введите номер месяца: ')

if number_of_month.isdigit():

    number_of_month_digit = int(number_of_month)
    if 0 < number_of_month_digit < 13:
        print(month_list[number_of_month_digit-1])
        print(month_dict.get(number_of_month_digit))
