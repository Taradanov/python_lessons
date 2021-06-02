
def main():
    rating_list = []

    while True:
        rating = input('Введите рейтинг или 0 для выхода: ')

        if rating == '0':
            return

        if rating.isdigit():
            rating_int = int(rating)
        else:
            print('Вы ввели не число')
            continue

        if len(rating_list) == 0:
            rating_list.append(rating_int)
            continue

        inser_made = False

        for i in range(0,len(rating_list)):
            if rating_list[i] < rating_int:
                rating_list.insert(i, rating_int)
                inser_made = True
                break

        if not inser_made:
            rating_list.append(rating_int)

        print(rating_list)


main()