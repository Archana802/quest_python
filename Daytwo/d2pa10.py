#10.Print X shape made up of stars of n lines - Done

number_of_lines = int(input('Enter the number of lines: '))#Input in interger form to enter the number of lines for X shape

for i in range(number_of_lines):#taking the loop for x-coordinates

    for j in range(number_of_lines):#taking the loop for y-coordinates

        if  i == j or j == number_of_lines-i-1:#conditions for printing the X shape 

            print('* ', end='')

        else:

            print('  ', end='')

    print()