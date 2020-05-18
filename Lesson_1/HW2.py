# Пользователь вводит время в секундах:
# Переведите время в часы, минуты и секунды
# выведите в формате чч:мм:сс.
# Используйте форматирование строк (f"{}")


def add_zero(time):  # функция по добавлению нуля перед числом если оно однозначное
    if len(str(time)) < 2:
        return "0" + str(time)


time_input = int(input("Введите время в секундах"))
hours = time_input // 3600
mins = time_input % 3600 // 60
secs = time_input % 3600 % 60

# if len(str(hours)) < 2:
#     hours = "0" + str(hours)
# if len(str(mins)) < 2:
#     mins = "0" + str(mins)
# if len(str(secs)) < 2:
#     secs = "0" + str(secs)
print(f"{time_input} секунд в часах будет {add_zero(hours)}:{add_zero(mins)}:{add_zero(secs)}")
