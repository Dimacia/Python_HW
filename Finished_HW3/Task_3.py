# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

season_dict = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето", 7: "Лето", 8: "Лето", 9: "Осень",
               10: "Осень", 11: "Осень", 12: "Зима"}
month_list = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь",
              "Октябрь", "Ноябрь", "Декабрь"]

try:
    input_number = int(input("Введите число от 1 до 12"))
    if input_number < 1 or input_number > 12:
        print("Убедитесь что вы ввели число от 1 до 12, если ошибка повторится - обратитесь в поддержку")
    for key in season_dict:
        if key == input_number:
            print(f"{input_number}-й месяц это {month_list[key - 1]}, сезон - {season_dict[key]}")
            break
except (NameError, ValueError):
    print("Убедитесь что вы ввели число от 1 до 12, если ошибка повторится - обратитесь в поддержку")
