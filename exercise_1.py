def add_substrings_in_file():
    with open('exercise_1.txt', mode='a+') as file_1:
        while True:
            substring = input()
            if not substring:
                break
            file_1.write(substring + '\n')


if __name__ == '__main__':
    add_substrings_in_file()
