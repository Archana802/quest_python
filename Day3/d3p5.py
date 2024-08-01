#Find sum of the series: 1 - n + n(2) - n(3) + ..... m terms

N = int(input('Enter the value of term:'))
M = int(input('Enter the number of terms:'))
sum_of_terms = 0

for i in range(0,M):
    term = ( N ** i) * ((-1) ** i)
    sum_of_terms += term

print('sum of the series is '+ str(sum_of_terms))
