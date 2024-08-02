#6. Print the Pascals triangle of n lines - Done

from math import factorial


number = int(input('enter the number of lines:'))

for i in range(number):
  for j in range(number-i+1):
    print('')
  for j in range(i+1):
    print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
  print()

