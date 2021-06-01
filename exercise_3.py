class MyExeption(Exception):

    def __init__(self):
        self.data_list = []

    def add_elements(self):
        while True:
            input_data = input()
            if input_data.lower() == 'stop':
                break
            if input_data.isdigit():
                self.data_list.append(int(input_data))
            else:
                print(f'Невозможно преобразовать в число:{input_data}')


my_exeption = MyExeption()
my_exeption.add_elements()
print(my_exeption.data_list)
