# pow(a, b) - a в степени b print(pow(2, -3))
# min([2, 4])
# max()
# sum() 2**-3 = 1/(2*2*2)


def my_func(number, negative_power):
    i = 0
    result = 1
    while i in range(negative_power * -1):
        result *= number
        i += 1
    return 1 / result


x = int(input("Введите действительное положительное число для возведения в степень"))
y = int(input("Введите целое отрицательное число-показатель степени "))
print(pow(x, y))
print(x ** y)

print(my_func(x, y))
