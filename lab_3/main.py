def multiply_vector_matrix(vector, matrix):
    vector_size = len(vector)
    matrix_rows, matrix_cols = len(matrix), len(matrix[0])

    if vector_size != matrix_rows:
        raise ValueError("Vector size must be equal to the number of matrix rows.")

    result = [0] * matrix_cols

    for i in range(matrix_cols):
        for j in range(vector_size):
            result[i] += vector[j] * matrix[j][i]

    return result



vector = [3, 4, 7]
matrix = [
    [1, 7, 3],
    [2, 2, 2],
    [7, 3, 7]
]

resultly = multiply_vector_matrix(vector, matrix)

print("Vector:")
print(vector)
print("\nMatrix:")
for row in matrix:
    print(row)
print("\nResult of vector-matrix multiplication:")
print(resultly)

matrix_string = ""
for row in matrix:
    for element in row:
        matrix_string += str(element) + " "
    matrix_string += "\n"

try:
    with open("text.txt", 'w') as file:
        file.write(matrix_string)
except FileNotFoundError:
    print("Couldnt create file")
except Exception as e:
    print(f"Error: {e}")
