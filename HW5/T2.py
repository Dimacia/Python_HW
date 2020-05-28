"""Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""

# файл text1.txt создан первой задачей
count_lines = 0
count_symbols = 0
with open("text1.txt", "r", encoding="utf-8") as file:
    for line in file:
        count_lines += 1
        for symbol in line:
            count_symbols += 1
        print(f"Количество символов в {count_lines}-й строке: {count_symbols - 1}")
        count_symbols = 0
    print(f"Количество строк, не считая последней пустой: {count_lines}")

