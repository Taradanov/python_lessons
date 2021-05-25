import itertools
import time


class TrafficLight:
    colors = ['red', 'yellow', 'green']

    TIMEFORREDCOLOR = 7
    TIMEFORYELLOWCOLOR = 2
    TIMEFORGREENCOLOR = 5

    def __init__(self):
        self.__color = self.get_new_color()

    def running(self):
        for new_color in self.get_new_color():
            print(new_color)
            if new_color == 'red':
                time.sleep(TrafficLight.TIMEFORREDCOLOR)
            elif new_color == 'yellow':
                time.sleep(TrafficLight.TIMEFORYELLOWCOLOR)
            elif new_color == 'green':
                time.sleep(TrafficLight.TIMEFORGREENCOLOR)

    def get_new_color(self):

        for i in itertools.cycle(TrafficLight.colors):
            yield i


trafficlight = TrafficLight()
trafficlight.running()
