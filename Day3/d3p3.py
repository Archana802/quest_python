#to find the nth prime number


#Program to check if a number is Prime

import math



def check_if_prime(num):

    for i in range(2, math.ceil(math.sqrt(num))+1):

        if num % i == 0:

            return False

    return True



input_number = int(input('Enter the number N, to print Nth Prime number: '))



j = 0

if input_number == 1:

    j = 2

elif input_number == 2:

    j = 3

else:

    count = 2

    j = 4 #Number in J is checked if Prime or not

    while count <= input_number:

        if check_if_prime(j):

            count += 1

        if count == input_number:

            break

        j += 1

print(f'{input_number}th Prime number is {j}')
































'''
1. enter the position of which prime no. needed
2. code for writing the prime number till that position.
    
'''
'''
position = int(input('enter the position: '))

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def print_primes_up_to_n(n):
    for i in range(2, n + 1):
        if is_prime(i):
            print(i, end=' ')
    print()
'''
