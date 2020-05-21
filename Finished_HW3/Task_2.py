# Реализовать функцию, принимающую несколько параметров:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой


def input_data(name, surname, year, city, email, phone):
    print(f"{name} {surname}, {year} г.р., город {city}. Почта: {email}, телефон: {phone}")


# в одну строку
my_func = lambda name, surname: print(name + " " + surname)

input_name = str(input("Введите имя"))
input_surname = input("Введите фамилию")
input_year = input("Введите год рождения")
input_city = input("Введите город проживания")
input_email = input("Введите почту")
input_phone = input("Введите телефон")
input_data(surname=input_surname, name=input_name, year=input_year, city=input_city, email=input_email,
           phone=input_phone)

my_func(input_name, input_surname)
