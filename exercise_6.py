def replace_symbols(prep_text):

    prep_text = prep_text.replace(')', ' ')
    prep_text = prep_text.replace('(', ' ')
    prep_text = prep_text.replace('  ', ' ')
    prep_text = prep_text.replace(':', '')

    return prep_text


def add_info(parsed_text, dict):

    split_text = parsed_text.split(' ')

    dict[split_text[0]] = sum([int(el) for el in split_text if el.isdigit()])


if __name__ == '__main__':
    with open('text_for_ex6.txt', mode='r', encoding='utf-8') as file_1:
        new_dict = {}
        while True:

            text = file_1.readline()

            if not text:
                break
            if text == '\n':
                continue

            text = replace_symbols(text)
            add_info(text, new_dict)
        print(new_dict)
