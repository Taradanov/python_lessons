import itertools


if __name__ == '__main__':
    start_from = 200
    finish_to = 5000

    for i in itertools.count(start_from):
        if i >= finish_to:
            break
        print(i)