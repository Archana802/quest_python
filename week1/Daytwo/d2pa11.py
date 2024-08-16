#11.Print a hollow square of n line with the diagonals - Done


number_of_lines = int(input('Enter the number of lines: ')) #Input in interger form to enter the number of lines for square

for i in range(number_of_lines): #taking the loop for x-coordinates

    for j in range(number_of_lines): #taking the loop for y-coordinates

        if i == 0 or i == number_of_lines-1 or j == 0 or j == number_of_lines-1 or i == j or j == number_of_lines-i-1:
            #conditions for printing the square and diagonals
            print('* ', end='') 

        else:

            print('  ', end='')

    print()


