if __name__ == '__main__':
    with open('text_for_ex4_in.txt', mode='r', encoding='utf-8') as file_input_data,\
            open('text_for_ex4_out.txt', mode="w", encoding='utf-8') as file_output_data:

        NUMERALS = {
            "one": "Один",
            "two": "Два",
            "three": "Три",
            "four": "Четыре",
            # "five": "Пять",
            # "six": "Шесть",
            # "seven": "Семь",
            # "eight": "Восемь",
            # "nine": "Девять",
            # "zero": "Ноль",
        }

        while True:
            text = file_input_data.readline()
            if not text:
                break
            for substring in text.split(' '):
                number = NUMERALS.get(substring.casefold())
                if number:
                    text = text.replace(substring, number)
            file_output_data.write(text)
