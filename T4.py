"""Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""


class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(
            f"{self.name}, цвет: {color}, скорость: {speed}, "
            f"{'Полицейская' if self.is_police == True else 'Не полицейская'}")

    def show_speed(self):
        print(f"Скорость: {self.speed}.")

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} остановилась")

    def turn(self, direction):
        if direction == 0:
            print(f"{self.name} повернула налево")
        elif direction == 1:
            print(f"{self.name} повернула направо")
        elif direction == 2:
            print(f"{self.name} развернулась на 180 градусов")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Скорость: {self.speed}. Превышаете!")
        else:
            print(f"Скорость: {self.speed}")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Скорость: {self.speed}. Превышаете!")
        else:
            print(f"Скорость: {self.speed}")


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super(PoliceCar, self).__init__(speed, color, name, is_police)


police = PoliceCar("Полицейская машина", "синий", 80)
police.go()
police.turn(0)
police.show_speed()
police.stop()
print()

sport = SportCar("Спортивная машина", "красный", 200)
sport.go()
sport.turn(1)
sport.show_speed()
sport.stop()
print()

work = WorkCar("Грузовая машина", "жёлтый", 45)
work.go()
work.turn(1)
work.show_speed()
work.stop()
print()

town = TownCar("Городская машина", "розовый", 65)
town.go()
town.turn(2)
print(town.show_speed())
town.stop()
print()
