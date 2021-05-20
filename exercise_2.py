
if __name__ == '__main__':
    with open('text_for_ex2.txt', mode='r') as file_1:

        number_of_lines = 0
        word_count = 0

        while True:

            text = file_1.readline()

            if not text:
                break

            if text == '\n':
                continue

            number_of_lines += 1

            list_of_words = text.split(sep=' ')
            list_without_empty_string = [el for el in list_of_words if el]
            word_count += len(list_without_empty_string)

        print(f'Количество строк: {number_of_lines}')
        print(f'Количество слов: {word_count}')
