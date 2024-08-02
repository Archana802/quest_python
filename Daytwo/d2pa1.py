#Find sum of Even placed digits in a number - done

input_number = int(input('Enter a number to find sum of even digits in it: '))
digits = str(input_number)
total_sum = 0

for i in range(1, len(digits), 2): 
        total_sum +=int(digits[i])
    
print('sum of Even placed digits in a number is ' + str(total_sum))
