class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join('\t'.join([str(i) for i in line]) for line in self.data)

    def __add__(self, other):
        try:
            matrix = [[int(self.data[line][item]) + int(other.data[line][item]) for item in range(len(self.data[line]))]
                      for line in range(len(self.data))]
            return Matrix(matrix)
        except IndexError:
            return f'Ошибка размера матрицы'


matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_2 = [[10, 11, 12], [13, 14, 15], [16, 17, '18']]

a = Matrix(matrix_1)
b = Matrix(matrix_2)
print(a)
print()
print(b)
print()

sum_matrix = a + b
print(sum_matrix)
