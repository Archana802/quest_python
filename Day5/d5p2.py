# Program to create 2D Array, that is, a Matrix(using List) and add it to another Matrix and print the sum Matrix.


rows = int(input('Enter number of rows of the Matrix: ')) #input for row numbwr
columns = int(input('Enter number of columns of the Matrix: ')) #input for column number

matrix1 = [] #creating an empty list to add the inputs
for i in range(rows):
    print(f'Enter {columns} numbers of Row-{i+1}')
    row_numbers = [] # List that stores numbers of a specific row

    for j in range(columns): # To read numbers of a row
        row_numbers.append(int(input()))
    matrix1.append(row_numbers)


for row in matrix1:
    for number in row:
        print('%3s'%(number), end='')
    print()

    