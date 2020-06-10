"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц)
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно
— первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д."""


class Matrix:
    def __init__(self, lists_list):
        self.lists_list = lists_list

    def __str__(self):
        for row in self.lists_list:
            print(" ".join(map(str, row)))
        return ""

    def __getitem__(self, idx):
        return self.lists_list[idx]

    def __add__(self, other):
        result = []
        numbers = []
        try:
            for i in range(len(self.lists_list)):
                for j in range(len(self.lists_list[0])):
                    summed_el = self.lists_list[i][j] + other[i][j]
                    numbers.append(summed_el)
                    if len(numbers) == len(self.lists_list[i]):
                        result.append(numbers)
                        numbers = []
            return Matrix(result)
        except IndexError:
            return "Ошибка: разные размерности матриц"


m_1 = Matrix([[1, 1, 1], [1, 1, 1]])
m_2 = Matrix([[1, 2, 3], [4, 5, 6]])
print(m_1)
print(m_2)

print(m_1 + m_2)
