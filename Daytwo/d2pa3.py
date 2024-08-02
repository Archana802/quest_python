#3. Find 2nd smallest digit in a number

input_number = int(input('Enter a number to find the 2nd smallest digit in it:'))

number = str(input_number)
smallest_digit = 0

for digit in number:
    if int(digit) < smallest_digit:
        smallest_digit = int(digit)

number.remove(str(smallest_digit))
 
print('Biggest digit in the number is ' + str(smallest_digit))
    


