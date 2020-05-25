"""Реализовать скрипт, в котором должна быть предусмотрена
функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу:
(выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами
строки не подойдут, учесть ошибки чтобы не вылетело"""

from sys import argv

name, set_hours, set_rate, set_bonus = argv


def salary(hours, rate, bonus):
    result = hours * rate + bonus
    print(result)


set_hours = int(set_hours)
set_rate = int(set_rate)
set_bonus = int(set_bonus)
salary(set_hours, set_rate, set_bonus)
