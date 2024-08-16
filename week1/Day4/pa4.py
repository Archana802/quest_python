#4.Accept N strings and check how many of them posses the string. - Done.

def count_strings_containing_substring(strings, substring):
    count = 0
    for s in strings:
        if substring in s:
            count += 1
    return count


N = int(input("Enter the number of strings: "))
strings = []

# Accept N strings from the user
for _ in range(N):
    string = input("Enter a string: ")
    strings.append(string)

# Accept the substring to check for
substring = input("Enter the substring to search for: ")

# Count how many strings contain the substring
count = count_strings_containing_substring(strings, substring)
print(f"Number of strings containing '{substring}': {count}")
