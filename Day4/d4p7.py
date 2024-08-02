#Relational operators in list


l1 = [3, 6, 10]
l2 = [1, 2, 4, 12]

''''
if l1 > l2:
    print('List1 is bigger')
else:
    print('List2 is bigger')
    '''

if l1.__gt__(l2):
    print('List1 is bigger')
else:
    print('List2 is bigger')



'''

For readability purpose we use 6 R.oprs

> < >= <= != ==

However we can perform any of the 6 operations using:  > and ==

'''
