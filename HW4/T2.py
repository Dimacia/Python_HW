"""Представлен список чисел.
Необходимо вывести элементы исходного списка, значения которых
больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
Пример исходного списка:
[300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор."""

result_list = []
counter = -1
check_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
for i in check_list:
    try:
        counter += 1
        if i > check_list[counter - 1] and counter > 0:
            result_list.append(check_list[counter])
    except IndexError:
        continue
print(result_list)

# Вторая часть задания:
new_list = [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]
print(new_list)

# Совсем в одну строку придумал так, но вывод некрасивый:
# new_list = [print(i) for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]

