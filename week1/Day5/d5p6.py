#promotion

'''''
Algorithm:
1. input = number of N customers whose bills are selected 
2. put a loop for N Bills- bill1, bill2,...
3. check each bill if it square or not
4. if it is perfect square, add the count
5. get the count of perfect squares

'''''
import math

num_of_list = int(input('Enter the number of customers whose bills are considered:'))
bill_amount = []
count_of_perfect_squares = 0

print(f'Enter the bill amounts of {num_of_list} customers :')
for i in range(len(str(num_of_list))):
    amount = int(input())
    bill_amount.append(amount)
print(f'Customer bill amounts are: {bill_amount}')
    

for i in range(N):
    root = math.isqrt(bill_amount[i])
    if(root * root == bill_amount[i]):
        count_of_perfect_squares += 1
    
print(f'Count of perfect squares of {num_of_list} bills is {count_of_perfect_squares}')

    








