''''
find Nth term of the series: 1 2 2 3 3 5 5 7 8 11 13 13
odd position elements: 1 2 3 5 8          (N//2 +1)th term  o(n)
even Position elements: 2 3 5 7 11         N/2th term     o(n square) - Done.

'''


# Function to generate the nth Fibonacci number
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b
    
# Function to generate the nth prime number
def nth_prime(n):
    count = 0
    num = 2
    while True:
        if is_prime(num):
            count += 1
            if count == n:
                return num
        num += 1

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


# Function to find the Nth term of the series
def find_nth_term(N):
    if N % 2 == 1:  # Odd position
        return fibonacci(N // 2 + 1)
    else:  # Even position
        return nth_prime(N // 2)


N = int(input("Enter the value of N: "))
print(f"The {N}th term of the series is: {find_nth_term(N)}")
