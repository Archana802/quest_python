#9Harsha - Only character

data_with_character = input('Enter the character with special character: ')

#special_characters = "!@#$%^&*()_+-={}[]|\\:;\"'<>,.?/~`"

def remove_special_characters(string):
    data_without_specialchacters = ''.join(char for char in string if char.isalpha())
    return data_without_specialchacters


data_without_specialchacters = remove_special_characters(data_with_character)
print(data_without_specialchacters)  
