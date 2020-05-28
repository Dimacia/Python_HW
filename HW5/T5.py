"""Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

original_text = "30 2 10"

with open("text_5.txt", "w+", encoding="utf-8") as text5:
    text5.write(original_text)
    num_list = original_text.split()
    print(sum(map(int, num_list)))
