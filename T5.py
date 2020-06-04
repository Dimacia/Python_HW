"""Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
 В каждом из классов реализовать переопределение метода draw.
 Для каждого из классов методы должен выводить уникальное сообщение.
 Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра."""


class Stationery:
    def __init__(self, title="с помощью любого пишущего предмета"):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title}")


stat = Stationery()
stat.draw()
print()

pen_1 = Pen("ручкой")
pen_1.draw()
print()

pencil_1 = Pencil("карандашом")
pencil_1.draw()
print()

handle_1 = Handle("маркером")
handle_1.draw()
print()
