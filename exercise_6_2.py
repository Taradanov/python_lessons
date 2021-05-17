import itertools

if __name__ == '__main__':

    list_of_numbers = [1, 2, 3, 4, 5]
    number = 0
    max_number = 1000
    for i in itertools.cycle(list_of_numbers):
        if number >= max_number:
            break
        number += 1
        print(i)
