"""
Stretch goals:
1. Addition of numbers and concatenate of string, where space is not given in the source string 
but space is printed while displaying.
2. Tell about "file" argument in print method. 
3. How do we round off to nearest close value
"""

try:
    x = input('Enter a Value:')
    y = input('Enter a Value:')

    num1 = int(x)
    num2 = int(y)
    output = num1 + num2

except ValueError:
    output = f"{x} {y}"

print("Result:", output)


'''''
try:
    x = int(input('Enter a Value:'))
    y = int(input('Enter a Value:'))

    print(x+y)
except ValueError:
    X = str(x)
    Y = str(y)
    print(x,y,sep=' ')

except NameError:
    X = str(x)
    Y = str(y)
    print(x,y,sep=' ')

#finally:
#    print(x,y,sep='  ')

'''
