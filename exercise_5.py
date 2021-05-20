import random

if __name__ == '__main__':

    with open('text_for_ex5.txt', mode='w', encoding='utf-8') as data_file:
        for el in [random.randint(0, 1000000) for i in range(0, 10000)]:
            data_file.write(f'{el} ')

    with open('text_for_ex5.txt', mode='r', encoding='utf-8') as data_file:
        substring = data_file.read()
        print(sum([int(el) for el in substring.split(' ') if el and el.isdigit()]))
