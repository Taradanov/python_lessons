class DivByZero(Exception):
    def __init__(self, txt):
        self.txt = txt


class UserData:

    def __init__(self, dividend, divider):
        self.divider = divider
        self.dividend = dividend

    def divide(self):
        if self.divider == 0:
            raise DivByZero('Ошибка деления на 0')
        return self.dividend/self.divider

user_data = UserData(100, 0)
try:
    print(user_data.divide())
except DivByZero as e:
    print(e.txt)
