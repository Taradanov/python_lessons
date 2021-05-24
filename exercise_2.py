def user_info(name='не указан', family='не указан', year='не указан',
              city='не указан', email='не указан', phone_number='не указан'):

    print(f'Имя:{name}, Фамилия:{family}, год рождения:{year},'
          f' город проживания:{city}, почта:{email}, телефон:{phone_number}.')


if __name__ == '__main__':
    user_info(family='Попов', name='Василий')
