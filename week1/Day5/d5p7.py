#Grid Path

'''
Algorithm:
1. Input = enter the rows and 2 columns
2. create the 2D matrix
3. enter the elements into the 2D
4. check the position with maximum of each list of 2D
5. Take the sum of the maximum in each iteration
6. Print the output as the sum

'''
###################################################################
rows = int(input('Enter number of rows of the Matrix: ')) 
columns = 2

two_D = []
for i in range(rows):
    print(f'Enter {columns} elements of Row-{i+1}')
    row_numbers = [] # List that stores numbers of a specific row

    for j in range(columns): # To read numbers of a row
        row_numbers.append(int(input()))
    two_D.append(row_numbers)


for row in two_D:
    for number in row:
        print('%3s'%(number), end='')
    print()

#######################################################################


sum_of_max_element = 0
previous_max_element = 0

for i in range(1,len(two_D)):
    current_max_element = max(two_D[i])
    if current_max_element > previous_max_element:
        sum_of_max_element += current_max_element
        previous_max_element = current_max_element
        





print(f'{sum_of_max_element} is the sum of possible outcomes')

    


