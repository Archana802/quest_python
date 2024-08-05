# Program to create 2D Array, that is, a Matrix(using List) and add it to another Matrix and print the sum Matrix.



rows = int(input('Enter number of rows of the Matrix1: '))
columns = int(input('Enter number of columns of the Matrix1: '))

matrix1 = []
for i in range(rows):
    print(f'Enter {columns} numbers of Row-{i+1}')
    row_numbers = [] # List that stores numbers of a specific row
    for j in range(columns): # To read numbers of a row
        row_numbers.append(int(input()))
    matrix1.append(row_numbers)

rows = int(input('Enter number of rows of the Matrix2: '))
columns = int(input('Enter number of columns of the Matrix2: '))

matrix2 = []
for i in range(rows):
    print(f'Enter {columns} numbers of Row-{i+1}')
    row_numbers = [] # List that stores numbers of a specific row
    for j in range(columns): # To read numbers of a row
        row_numbers.append(int(input()))
    matrix2.append(row_numbers)


print('Matrix1 is:')
for row in matrix1:
    for number in row:
        print('%3s'%(number), end='')
    print()


print('Matrix2 is:')
for row in matrix2:
    for number in row:
        print('%3s'%(number), end='')
    print()



sum_matrix = []

for i in range(len(matrix1)):

    row_numbers = []

    for j in range(len(matrix1[0])):

        row_numbers.append(matrix1[i][j] + matrix2[i][j])

    sum_matrix.append(row_numbers)



print('Sum Matrix is:')

for row in sum_matrix:

    for number in row:

        print('%3s'%(number), end='')

    print()