""" Пользователь вводит строку из нескольких слов, разделённых пробелами.
 Вывести каждое слово с новой строки.
 Строки необходимо пронумеровать.
 Если в слово длинное, выводить только первые 10 букв в слове."""

string = (input("Enter numbers with spaces between them")).split()

for num, val in enumerate(string, 1):
    print(num, val) if len(val) <= 10 else print(num, (val[:10]))
