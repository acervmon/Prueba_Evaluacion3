class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def determinant_recursive(self):
        return self._determinant_recursive(self.matrix)

    def _determinant_recursive(self, matrix):
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        
        determinant = 0
        for i in range(len(matrix)):
            sub_matrix = [row[:i] + row[i+1:] for row in matrix[1:]]
            determinant += (-1) ** i * matrix[0][i] * self._determinant_recursive(sub_matrix)
        
        return determinant

    def determinant_iterative(self):
        a, b, c, d, e, f, g, h, i = self.matrix[0] + self.matrix[1] + self.matrix[2]
        return a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)


if __name__ == "__main__":
    matrix = []
    for _ in range(3):
        row = []
        for _ in range(3):
            num = int(input("Enter a number: "))
            row.append(num)
        matrix.append(row)

    matrix_obj = Matrix(matrix)

    print("Determinant (Recursive):", matrix_obj.determinant_recursive())
    print("Determinant (Iterative):", matrix_obj.determinant_iterative())
