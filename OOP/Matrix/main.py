class Matrix:
    def __init__(self, n, m, element):
        pass

    def get_element(self, i, j):
        pass

    def set_element(self, i, j, element):
        pass

    def get_row(self, i) -> list:
        """
        Должен возвращать список - итый ряд в матрице
        """
        pass

    def __str__(self):
        pass

    def get_col(self, j):
        """
        Должен возвращать список - jтый столбец в матрице
        """
        pass

    def find_max_number(self, sravnicatel: function):
        pass

    def transpose(self):
        pass


matrix = Matrix(5, 6, '0')
matrix.set_element(1, 2, 'x')

print(matrix)
