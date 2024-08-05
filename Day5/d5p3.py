#sum of two matrices

rows1 = int(input('Enter number of rows of the Matrix1: '))
columns1 = int(input('Enter number of columns of the Matrix1: '))

matrix1 = []
for i in range(rows1):
    print(f'Enter {columns1} numbers of Row-{i+1}')
    row_numbers = [] # List that stores numbers of a specific row
    for j in range(columns1): # To read numbers of a row
        row_numbers.append(int(input()))
    matrix1.append(row_numbers)

rows2 = int(input('Enter number of rows of the Matrix2: '))
columns2 = int(input('Enter number of columns of the Matrix2: '))


matrix2 = []
for i in range(rows2):
    print(f'Enter {columns2} numbers of Row-{i+1}')
    row_numbers = [] # List that stores numbers of a specific row
    for j in range(columns2): # To read numbers of a row
        row_numbers.append(int(input()))
    matrix1.append(row_numbers)


for row1 in matrix1:
    for number in row1:
        print('%3s'%(number), end='')

    print()

for row2 in matrix2:
    for number in row2:
        print('%3s'%(number), end='')

    print()

sum_matrix = []


for i in range(len(matrix1)):
    row_matrix = []
    for j in range(len(matrix1[0])):
        row_numbers.append(matrix1[i][j] + matrix2[i][j])
    sum_matrix.append(row_numbers)

print('Sum Matrix is:')
for row in sum_matrix:
    for number in row:
        print('%3s'%(number), end='')
    print()

