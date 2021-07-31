class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return f'{self.nums}'

    def __add__(self, other):
        print('Сложение двух клеток')
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        print('Вычитание клеток')
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 \
            else print('В первой клетке меньше ячеек, вычитание невозможно')

    def __mul__(self, other):
        print('Умножение клеток')
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        print('Целочисленное деление клеток')
        return Cell(self.nums // other.nums)


cell_1 = Cell(25)
cell_2 = Cell(13)
print(cell_1.make_order(6))
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
