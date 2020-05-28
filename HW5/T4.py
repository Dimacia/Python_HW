"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("text_4.txt", "r", encoding="utf-8") as file, open("text_4_rus.txt", "w+", encoding="utf-8") as new_file:
    data = file.readlines()  # читаем исходный текст
    for line in data:
        string_list = line.split()  # разбиваем каждую строку на элементы списка
        for key, value in my_dict.items():
            if key == string_list[0]:
                string_list[0] = my_dict[string_list[0]]  # меняем английское слово на русское
                string_list += "\n"  # добавляем перенос строки
        print(string_list)
        result = ' '.join(string_list)  # объединяем списки обратно в строки
        new_file.write(result)
