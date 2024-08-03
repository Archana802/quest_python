#9Harsha - Only character

data_with_character = input('Enter the character with special character: ')

#special_characters = "!@#$%^&*()_+-={}[]|\\:;\"'<>,.?/~`"

def remove_special_characters(string):
    cleaned_string = ''.join(char for char in string if char.isalpha())
    return cleaned_string


cleaned_string = remove_special_characters(data_with_character)
print(cleaned_string)  
