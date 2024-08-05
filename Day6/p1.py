''''
Assignment:
Accept a string of Pairs of Peranthesis and check if they are arranged properly. 
If so, print the number of pairs of peranthesis else print improper arrangement.

((()())) : 4 pairs
(()))   : improper arrangement
'''

def check_parentheses(s):
    open_count = 0
    pairs_count = 0

    for char in s:
        if char == '(':
            open_count += 1  
        elif char == ')':
            if open_count > 0:
                open_count -= 1  
                pairs_count += 1  
            else:
                return "Improper arrangement" 

    
    if open_count == 0:
        return f"{pairs_count} pairs"
    else:
        return "Improper arrangement" 


string_of_parenthesis = input("Enter a string of parentheses: ")
result = check_parentheses(string_of_parenthesis)
print('The arrangement is ' + result)
