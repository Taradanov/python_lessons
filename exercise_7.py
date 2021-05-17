def fact(n):

    if not n > 0:
        raise ValueError

    factorial = 1

    for i in range(1, n + 1):
        factorial *= i
        yield factorial


if __name__ == '__main__':

    func = fact(4)

    print(type(func))

    for el in func:
        print(el)
