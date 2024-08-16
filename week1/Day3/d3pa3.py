#Print the smallest and biggest strings in the list of N strings. 

'''
alogritham:
1. Input = N numbers of strings from the user
2. Find the smallest and largest strings 
3. Print the modified list

'''
# Accept N strings from the user
strings = input("Enter the strings separated by spaces: ").split()

#Find the smallest and biggest strings using min() and max()
smallest = min(strings)
largest = max(strings)

# Print the results
print("Smallest string:", smallest)
print("Biggest string:", largest)