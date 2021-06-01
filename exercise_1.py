class DateTime:
    def __init__(self, data_time_as_string):

        self.day, self.month, self.year = DateTime.get_data_time_as_numbers(data_time_as_string)

    @staticmethod
    def check_data(day, month, year):
        if day > 31 or day == 0:
            raise ValueError('Дата не может быть более 31 или равна нулю')
        if month > 12 or month == 1:
            raise ValueError('Месяц должен иметь номер от 1 до 12')

    @classmethod
    def get_data_time_as_numbers(cls, data_time_as_string: str):

        data_time_as_list = data_time_as_string.split('-')

        data_time_as_list = [int(el) for el in data_time_as_list if el.isnumeric()]

        if len(data_time_as_list) != 3:
            raise ValueError('Ошибка парсинга параметра, возможно дата не соответствует формату')

        cls.check_data(*data_time_as_list)

        return data_time_as_list[0], data_time_as_list[1], data_time_as_list[2],

    def __str__(self):
        return f'{self.day}, {self.month}, {self.year}'


# date_time = DateTime('sdfsdf-wer')
date_time = DateTime('5-10-1230')
# date_time = DateTime('510-1230')
# date_time = DateTime('15-15-1230')
print(date_time)
