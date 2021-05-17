
if __name__ == '__main__':

    old_list =  [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

    new_list = [el for el, key in {el: old_list.count(el) for el in old_list}.items() if key == 1]

    print(new_list)

