# Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление.
# Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.


def division(a, b):
    result = a / b
    return result


x = float(input("Введите делимое число"))
y = float(input("Введите делитель"))
""" if y == 0:
     print("Ошибка: деление на ноль")
 else:
     print(division(x, y))"""
try:
    print(division(x, y))
except ZeroDivisionError:
    print("Не делите на ноль!")