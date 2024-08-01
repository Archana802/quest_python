#Print the smallest and biggest elements in the list of N numbers. - Done

'''
alogritham:
1. Input = N numbers of elements from the user
2. form elements into a list
3. Find the smallest and largest elemts
4. Print the modified list

'''

numbers = list(map(int, input("Enter the numbers separated by spaces: ").split()))
#Accept N numbers from the user

# Find the smallest and biggest elements
smallest = min(numbers)
largest = max(numbers)

#Print the results
print("Smallest element:", smallest)
print("Biggest element:", largest)