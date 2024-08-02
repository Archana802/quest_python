#List Slicing:



numbers = [2, 9, 7, 5, 3, 13, 19, 17, 29]
print(numbers) # we get the complete list

print(numbers[0]) # we get the 1st element

print(numbers[-1]) # we get the last element Hence, we see that -ve indexing is possible in Python

print(numbers[-2]) # we get last but element from the list

print(numbers[:]) # we get the complete list
#Here, we have written nothing before the colon and hence it is treated as 0, which means start from the beginning of the list. Here also have not written anything after the colon, which means it is treated as UP TO END OF THE LIST. 

print(numbers[:3]) # Start from index 0 and access elements up to index 3-1 which is 2.

print(numbers[1:-1]) # Start from index 1 (2nd element) and access elements up to last but element, because -1 is the index of last element and we must not include it.

print(numbers[1:8:2]) # start from index 1 and access upto index 8-1 and increment each time by 2 elements. So o/p is [9, 5, 3, 19]

print(numbers[::3]) # start from biginning and go up to end of the list with increment of 3

print(numbers[8:1:-2]) #Start from index 8, go up to index 2 with  decrement of 2 (or increment of -2)

print(numbers[::-1]) # Since the increment is negative, we understand that we have to move in reverse (meaning from the end to towards the start). 
#The area within the list we have to access is all the elements, because nothing is specified before and after the 1st colon :
