#!/usr/bin/python3
#!/usr/bin/python3
from prueba import matrix

matrix2 = []
for a in range(len(matrix)):
    row = []  # Create a new row for matrix2
    for b in range(len(matrix[a])):
        row.append(matrix[a][b])  # Copy the element from matrix to matrix2
    matrix2.append(row)  # Append the row to matrix2

print(matrix2)
