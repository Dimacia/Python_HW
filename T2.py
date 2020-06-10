"""Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property."""
from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Clothes(MyAbstractClass):
    def __init__(self, size=1):
        self.size = size

    @property
    def consumption_Coat(self, param):
        pass

    @property
    def consumption_Suit(self, param):
        pass

    @property
    def consumption(self):
        return self.consumption_Coat + self.consumption_Suit


class Coat(Clothes):
    @property
    def consumption(self):
        result = round(self.size / 6.5 + 0.5)
        Clothes.consumption_Coat = result
        return f"На Пальто уйдёт {round(self.size / 6.5 + 0.5)} м ткани"


class Suit(Clothes):
    @property
    def consumption(self):
        result = round(2 * self.size + 0.3)
        Clothes.consumption_Suit = result
        return f"На Пальто уйдёт {round(result)} м ткани"


clothes = Clothes()
coat = Coat(42)
print(coat.consumption)
suit = Suit(160)
print(suit.consumption)
print(f"Общий расход ткани = {clothes.consumption} м")
