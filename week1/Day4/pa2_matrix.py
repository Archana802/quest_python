'''
#2.Accept a string of space separated numbers and
store them as a matrix (list of lists) of n rows.Now print the matrix row-wise. - Done.
'''

def create_matrix_from_string(data, n):
    # Convert the input string into a list of integers
    numbers = list(map(int, data.split()))
    
    # Create the matrix with n rows
    matrix = []
    row_length = len(numbers) // n  # Calculate the number of columns
    
    for i in range(n):
        # Slice the list of numbers to create each row
        row = numbers[i * row_length: (i + 1) * row_length]
        matrix.append(row)
    
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


data = input("Enter space-separated numbers: ")
n = int(input("Enter the number of rows: "))

# Create the matrix
matrix = create_matrix_from_string(data, n)

# Print the matrix row-wise
print("Matrix:")
print_matrix(matrix)
