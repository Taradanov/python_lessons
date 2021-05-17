from functools import reduce


def multiply(a, b):
    return a * b


if __name__ == '__main__':
    new_list = [el for el in range(100, 1001, 2)]

    print(new_list)

    print(reduce(multiply, new_list))
