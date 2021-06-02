
def main():
    l = [el[:10] if len(el) > 10 else el for el in input().split(' ')]
    count = 0
    for el in l:
        count +=1
        print(f'{count}. {el}')


main()