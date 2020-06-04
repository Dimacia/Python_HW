"""Создать класс TrafficLight (светофор) и определить у него
один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт."""

from time import sleep
from itertools import cycle


class TrafficLight:
    def __init__(self):
        self.TrafficLight_color = color

    def running(self):
        color = 0
        self.TrafficLight_color = color
        for i in cycle("xy"):
            color = "red"
            print(color)
            sleep(7)
            color = "yellow"
            print(color)
            sleep(2)
            color = "green"
            print(color)
            sleep(7)
            color = "yellow"
            print(color)
            sleep(2)


t = TrafficLight()
t.running()
