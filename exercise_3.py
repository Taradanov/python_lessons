if __name__ == '__main__':
    with open('text_for_ex3.txt', mode='r', encoding='utf-8') as file_1:
        number_of_lines = 0
        summ_salary = 0
        while True:
            text = file_1.readline()
            if not text:
                break
            number_of_lines += 1

            employee = text.split(' ')
            salary = int(employee[1])
            if salary < 20_000:
                print(f'Зарплата менее 20 000: {employee[0]}')
            summ_salary += salary
        print(f'Средняя зарплата {summ_salary / number_of_lines}')
