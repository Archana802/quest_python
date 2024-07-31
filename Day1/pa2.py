#ASSIG4 check a letter is vowel or not.

letter = input('enter a letter to check whether the letter is vowel or consonant - ')
vowels = "AEIOUaeiou"
if letter in vowels:
    print('letter',letter,'is vowel')
else:
    print('letter',letter,'is consonant')