month_list = ('зима',
              'Февраль',
              'весна',
              'весна',
              'весна',
              'лето',
              'лето',
              'лето',
              'осень',
              'осень',
              'осень',
              'зима',
              )
month_dict = {1: 'зима',
              2: 'зима',
              3: 'зима',
              4: 'весна',
              5: 'весна',
              6: 'лето',
              7: 'лето',
              8: 'лето',
              9: 'осень',
              10: 'зима',
              11: 'зима',
              12: 'зима',
              }

number_of_month = input('Введите номер месяца: ')

if number_of_month.isdigit():

    number_of_month_digit = int(number_of_month)
    if 0 < number_of_month_digit < 13:
        print(month_list[number_of_month_digit-1])
        print(f'Из list-a:  {number_of_month_digit}-ый месяц это {month_list[number_of_month_digit-1]}')
        print(f'Из словаря: {number_of_month_digit}-ый месяц это {month_dict.get(number_of_month_digit)}')
