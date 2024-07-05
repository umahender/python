
# Define the matrices
matrix1 = [[1, 2],
           [3, 4]]

matrix2 = [[5, 6],
           [7, 8]]

# Create an empty result matrix
result = [[0, 0],
          [0, 0]]

# Perform matrix multiplication
for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

# Print the result matrix
print("Result Matrix:")
for row in result:
    print(row)