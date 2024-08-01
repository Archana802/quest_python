#4. Check if a number is Prime


import sys



input_number = int(input('Enter a number to check if it is prime number or not: '))

if input_number in [1 , 2] :
    print(str(input_number)+' is prime number.')

for i in range(3, int(input_number),1):

    if input_number % i == 0:
        print(str(input_number)+' is not prime number.')
    sys.exit

print (str(input_number)+' is prime number.')



#check < input_number: