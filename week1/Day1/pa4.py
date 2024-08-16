#ASSIG5  Check if a number is single digit or not.

number = int(input('enter a number to check whether it is single digit or not: '))
number1 = str(number)
count_of_digits = len(number1)

if (count_of_digits == 1):
    print(number1+ ' is a single digit')
else:
    print(number1 + ' is not a single digit')