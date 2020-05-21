# Для списка реализовать обмен значений соседних элементов,т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().


input_str = input("Введите строку, которую нужно перепутать")
input_list = list(input_str)
# print(input_str)
if len(input_list) % 2 > 0:  # есть нечетное число - выносим отдельно и убираем
    last_symbol = input_list[-1]
print(input_list)
odd = input_str[::2]  # доставать с шагом
even = input_str[1::2]
# print(even)
# print(odd)

result_list = []
i = 0
while len(even) > i:
    result_list.append(even[i])
    result_list.append(odd[i])
    i += 1
if len(input_list) % 2 > 0:
    result_list.append(last_symbol)
print(result_list)
