# Examples: .isdigit() and .isdecimal()


print("12345".isdecimal())   # True: All characters are decimal digits.
print("123.45".isdecimal())  # False: The period is not a decimal digit.
print("12³".isdecimal())     # False: The superscript '3' (³) is not considered a decimal digit.
print("⅕".isdecimal())       # False: The fraction '⅕' is not a decimal digit.

print("12345".isdigit())     # True: All characters are digits.
print("123.45".isdigit())    # False: The period is not a digit.
print("12³".isdigit())       # True: The superscript '3' (³) is considered a digit.
print("⅕".isdigit())         # False: The fraction '⅕' is not considered a digit.

