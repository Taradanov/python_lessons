def my_func(a1: int, a2: int, a3: int) -> int:
    list_ = [a1, a2, a3]
    list_ = sorted(list_)
    return list_[1] + list_[2]


if __name__ == '__main__':
    print(my_func(5, 2, 8))
