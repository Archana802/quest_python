#Accept N numbers from the user and swap the consecutive elements in the list. - Done

'''
alogritham:
1. Input = N numbers from the user
2. form elements into a list
3. swap the elements
4. Print the modified list

'''


numbers = list(map(int, input("Enter the numbers separated by spaces: ").split()))
#Accept N numbers from the user

for i in range(0, len(numbers) - 1, 2): # Swap consecutive elements
    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

# Print the modified list
print("List after swapping consecutive elements:", numbers)