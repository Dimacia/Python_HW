"""Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

with open("text_3.txt", "r", encoding="utf-8") as data:
    counter = 0
    income = 0
    print("Сотрудники с окладом меньше 20000:")
    for line in data:
        counter += 1
        string_list = (line.split(" "))
        income += (float(string_list[1]))
        if (float(string_list[1])) < 20000.0:
            print(string_list[0])
    print(f"Средний доход сотрудников: \n{income} / {counter} = {income / counter}")
