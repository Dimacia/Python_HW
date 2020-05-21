# Реализовать структуру «Рейтинг»,
# представляющую собой невозрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.


rating = [8, 7, 7, 7, 2, 2, 0]
user_rating = (input("Enter rating"))
if user_rating.isdigit():
    user_rating = float(user_rating)
    i = 0
    for value in rating:
        if user_rating <= value:
            i += 1
    rating.insert(i, user_rating)
else:
    print("Please try again and write a proper number")
print(rating)
