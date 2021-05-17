import random

if __name__ == '__main__':

    new_list = [random.randint(0, 1000) for _ in range(0, 100)]

    filtered_list = [el for el in new_list if el % 21 == 0 or el % 20 == 0]

    print(filtered_list)
