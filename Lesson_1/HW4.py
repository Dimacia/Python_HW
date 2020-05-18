# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции

number = int(input("Введите целое положительное число"))
max = 0
i = 0
next_digit = 0
while True:
    i += 1
    next_digit = number % (10 ** i) // (10 ** (i - 1))
    if next_digit == 0:
        break
    if max < next_digit:
        max = next_digit
    if max == 9:
        break
print(f"Самая большая цифра в числе {number} - {max}")
