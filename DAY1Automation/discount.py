"""
* Name
* Age
15% discount for all product for senior citizen

* Gender
male senior citizen (60 and above)
female senior citizen (45 and above)
 
100 rupees nyka, fastrack, if female (<45)
100 coupon on titan, fastrack, if male (<60)
----
*Occupation: Working, Student (PIN code should be local) 
College: 500 coupon on books
Working: NA
----
*Residence: Hosteller, Localite (Hostel name should be valid)
Hosteller: Groceries
Localite: NA
"""

age = int(input("Enter age: "))
gender = input("Enter gender: \n1. Male\n2. Female\n3. Other\nEnter any number:")
occupation = input("Enter Ocupation: \n1. working\n2. Student \n3. other\nEnter any number:")
resident = input("Enter Residency: \n1. Hosteller\n2. Localite \nEnter any number:")
PinCodes = [123, 456, 789]
HostelNames = ['ABC', 'CDE', 'EFG', 'HIJ']



if gender == '1'and '3':   #for male and others
    if age >= 60:
        print(" 15% Senior citizen discount applied, thank you for shopping", "\n")
    else :
        print("100 voucher Fastrack & Titan!!!!!, thank you for shopping", "\n")
        if occupation == '2': # type: ignore #for student
            pin_code = int(input('Enter your pincode:'))
            if pin_code in PinCodes: #only applicable if student in local pincode
                print('500 coupon on Books!!!!!','\n')
                if resident == '1': #for Hosteller
                    hostel_name = input('Enter hostel name:') #only applicable if hostelname in the list
                    if hostel_name.upper() in HostelNames:
                         print('250/- Discount on Groceries !!!!!',"\n")
        elif resident == '1': #checking hostelname for working male and others
            hostel_name = input('Enter hostel name:') #name of hostel
            if hostel_name.upper() in HostelNames:
                print('250/- Discount on Groceries !!!!!',"\n")
        


elif gender == '2':  #for female
    if age >= 45:
        print(" 15% Senior citizen discount applied, thank you for shopping", "\n")
    else :
        print("100/- Discount on Nykaa & fastrack!!!!!, thank you for shopping", "\n")
        if occupation == '2': # type: ignore #for student
            pin_code = int(input('Enter your pincode:')) #to check if the pincode in the list
            if pin_code in PinCodes:
                print('500 coupon on Books!!!!!','\n')
                if resident == '1': #for hostellers in the list of hostel names
                    hostel_name = input('Enter hostel name:')
                    if hostel_name.upper() in HostelNames:
                         print('250/- Discount on Groceries !!!!!',"\n")
    
        elif resident == '1': #hostellers in working as occupation
            hostel_name = input('Enter hostel name:')
            if hostel_name.upper() in HostelNames:
                print('250/- Discount on Groceries !!!!!',"\n")

    print('Thank you for shopping','\n') #if none of the condition validates
else:
    print('Thank you for shopping','\n') 