# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
# (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
# классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self):
        super(Pen, self).__init__('Ручка')

    def draw(self):
        print('Ручка рисует')


class Pencil(Stationery):
    def __init__(self):
        super(Pencil, self).__init__('Карандаш')

    def draw(self):
        print('Карандаш рисует')


class Handle(Stationery):
    def __init__(self):
        super(Handle, self).__init__('Маркер')

    def draw(self):
        print('Маркер рисует')


pen = Pen()
pen.draw()

pensil = Pencil()
pensil.draw()
