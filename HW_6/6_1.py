"""
coding=utf-8
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.  Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.

"""

from itertools import cycle
import time


class TrafficLight:
    __color = {"red": 3, "yellow": 1, "green": 3}

    def running(self) -> object:
        print(type(self.__color))
        tmp_ind = 0
        for el in cycle(self.__color.keys()):
            if tmp_ind > 10:
                print("done!")
                break
            print(el)
            tmp_ind += 1
            time.sleep(self.__color.get(el))


tl_obj = TrafficLight()
tl_obj.running()
