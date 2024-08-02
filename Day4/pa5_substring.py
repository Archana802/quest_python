'''
#5. Accept N main strings and N sub main strings into lists and
check create a list of numbers of Os and 1s where 0 represents that the substring at
respective index is not a substring of the main string
'''


def check_substring_presence(main_list, sub_list):
    presence = []
    
    
    for main, sub in zip(main_list, sub_list):
        if sub in main:
            presence.append(1)
        else:
            presence.append(0)
    
    return presence


main_list = ['andhra pradesh', 'kerala', 'maharashtra', 'haryana']
sub_list  = ['pradesh', 'south', 'rashtra', 'punjab']


presence = check_substring_presence(main_list, sub_list)
print(f"Presence: {presence}")
