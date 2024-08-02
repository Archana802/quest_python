#3. Accept N strings and count the number of palindromes in it. - Done.

def is_palindrome(s):
    # A palindrome reads the same forward and backward
    return s == s[::-1]

def count_palindromes(strings):
    palindrome_count = 0
    for s in strings:
        if is_palindrome(s):
            palindrome_count += 1
    return palindrome_count

# Example usage:
N = int(input("Enter the number of strings: "))
strings = []

# Accept N strings from the user
for _ in range(N):
    string = input("Enter a string: ")
    strings.append(string)

# Count the number of palindromes
palindrome_count = count_palindromes(strings)
print(f"Number of palindromes: {palindrome_count}")
