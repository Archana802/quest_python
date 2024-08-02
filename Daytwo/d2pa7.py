#7. Print the Fibo series of n terms with 1st 2 terms as 1 and 2. - Done


number = int(input('Enter the limit:')) 

first_term = 1
second_term = 2
nth_term = 0

if number == 1 :
    nth_term = 1
elif number == 2 :
    nth_term = 2
else:
    nth_term = 0
    count = 2
    print('Tth Fibo series is ')
    print(first_term)
    print(second_term)
    while count <= number:
        nth_term = first_term + second_term
        count += 1
        first_term = second_term
        second_term = nth_term
        print(nth_term)

if number <= 0:  

    print ("Please enter a positive integer, the given number is not valid")