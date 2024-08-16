#mirror


##############################################

def is_right_rotation(word1, word2):
    combined_word = word1 + word1
    if word2 in combined_word:
        print('True')
    else:
        else('False')
    

#############################################
def rotate_string_right(s, index):
    n = len(s)
    # Rotate right by slicing
    return s[-index:] + s[:-index]

#############################################

original_string = input('Enter the word to check: ')
letter = input('the rotation should start: ')
index = original_string.find(letter)

rotated_string = rotate_string_right(original_string, index)
print(rotated_string)

is_right_rotation(original_string, rotated_string)



