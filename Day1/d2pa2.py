#Find biggest digit in a number

input_number = int(input('Enter a number to find the biggest digit in it:'))

number = str(input_number)
biggest_digit = 0

for digit in number:
    if int(digit) > biggest_digit:
        biggest_digit = int(digit)
 
print('Biggest digit in the number is ' + str(biggest_digit))
    