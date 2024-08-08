#branch
try:
    branch = input('Enter the Branch:')
    preference = input('Enter the preference (Maths or Art)  :')
    maths = int(input('Enter maths mark:'))
    english = int(input('Enter English mark:'))
    art = int(input('Enter Art mark:'))

except:
    print('Please provide a valid inputs')

"""
marks_dict = dict[marks]
print(marks_dict)
list_marks = marks_dict.split(',')
length_of_marks = len(list_marks)
"""
branch_list = ['ECE', 'MECH', 'BCOM']
preference_list = ['MATHS', 'ART']


#branch_list = append.branch # type: ignore
#preference_list = append.preference # type: ignore

if branch.upper() in branch_list:
    if preference.upper() in preference_list:
        if ((maths > 35) and (english > 35) and (art > 35)) :
            if (branch.upper() == 'ECE') :
                if (art > 90) and (english > 90) and (preference.upper() == 'ART'):
                    print('Vacancy in marketing')
            elif (branch.upper() == 'BCOM') :
                if(maths > 90) and (preference.upper() == 'MATHS'):
                    print('Vacancy in Accounting')
            elif (branch.upper() == 'MECH') :
                if (maths > 90) and english > 90 and (preference.upper() == 'MATHS'or 'ART'):
                    print('Vacancy in Sales')
                else:
                    print('Insufficient marks')
            else:
                print('Insufficient marks')
        else:
            print('NO PASS MARK,try again')
    else:
        print('Your preference is not matching')
else:
    print('There is no vacancy for your branch,Try again')

'''
if ((maths < 35) and (english < 35) and (art < 35)):
    print('NO PASS MARK,try again')
'''
