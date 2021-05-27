# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.is_police = is_police
        self.name = name
        self.speed = speed
        self.color = color

    def go(self):
        print(f'{self} {self.name} поехал')

    def stop(self):
        print(f'{self} {self.name} остановился')

    def turn(self, direction):
        if direction == 'left':
            print(f'{self} повернул налево')
        elif direction == 'right':
            print(f'{self} повернул направо')
        else:
            print('рулевое сломалось')

    def show_speed(self):
        print(f'Скорость {self} {self.name} составляет {self.speed}')


class TownCar(Car):
    def __str__(self):
        return 'Городской автомобиль'

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        super(TownCar, self).show_speed()
        if self.speed > 60:
            print(f'Автомобиль {self} {self.name} превысил скорость')


class SportCar(Car):
    def __str__(self):
        return 'Спорткар'

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class WorkCar(Car):
    def __str__(self):
        return 'Рабочий автомобиль'

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        super(WorkCar, self).show_speed()
        if self.speed > 40:
            print(f'{self} {self.name} превысил скорость')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

    def __str__(self):
        return 'Полицейский автомобиль'


p_car = PoliceCar(200, 'black', "Cop's car")
p_car.go()
p_car.turn('left')

town_car = TownCar(100, 'red', 'Тачка Боба')
town_car.go()
town_car.show_speed()
town_car.stop()
