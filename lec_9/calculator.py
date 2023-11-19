class MyMatrix:
    
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]
    
    def __str__(self):
        matrix_str = ""
        for row in self.data:
            matrix_str += ' '.join(str(val) for val in row) + '\n'
        return matrix_str

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must be the same for addition")
        
        result = MyMatrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must be the same for subtraction")
        
        result = MyMatrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix for multiplication")
        
        result = MyMatrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                result.data[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
        return result


matrix_1 = MyMatrix(2, 2)
matrix_1.data = [[1, 1], [3, 7]]

matrix_2 = MyMatrix(2, 2)
matrix_2.data = [[3, 1], [9, 5]]

print("Matrix 1:")
print(matrix_1)

print("Matrix 2:")
print(matrix_2)

matrix_sum = matrix_1 + matrix_2
print("Matrix Sum:")
print(matrix_sum)

matrix_diff = matrix_1 - matrix_2
print("Matrix Difference:")
print(matrix_diff)

matrix_3 = MyMatrix(2, 3)
matrix_3.data = [[1, 2, 3], [4, 5, 6]]

matrix_4 = MyMatrix(3, 2)
matrix_4.data = [[7, 8], [9, 10], [11, 12]]

matrix_product = matrix_3 * matrix_4
print("Matrix Product:")
print(matrix_product)
