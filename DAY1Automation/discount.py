

age = int(input("Enter age: "))
gender = input("Enter gender: \n1. Male\n2. Female\n3. Other\nEnter any number:")
occupation = input("Enter Ocupation: \n1. working\n2. Student \n3. other\nEnter any number:")
resident = input("Enter Residency: \n1. Hosteller\n2. Localite \nEnter any number:")
PinCodes = [123, 456, 789]
HostelNames = ['ABC', 'CDE', 'EFG', 'HIJ']



if gender == '1'and '3':
    if age >= 60:
        print(" 15% Senior citizen discount applied, thank you for shopping", "\n")
    else :
        print("100 voucher Fastrack & Titan!!!!!, thank you for shopping", "\n")
        if occupation == '2': # type: ignore
            pin_code = int(input('Enter your pincode:'))
            if pin_code in PinCodes:
                print('500 coupon on Books!!!!!','\n')
                if resident == '1':
                    hostel_name = input('Enter hostel name:')
                    if hostel_name.upper() in HostelNames:
                         print('250/- Discount on Groceries !!!!!',"\n")
        elif resident == '1':
            hostel_name = input('Enter hostel name:')
            if hostel_name.upper() in HostelNames:
                print('250/- Discount on Groceries !!!!!',"\n")
        
#        print('Thank you for shopping','\n')


elif gender == '2':
    if age >= 45:
        print(" 15% Senior citizen discount applied, thank you for shopping", "\n")
    else :
        print("100/- Discount on Nykaa & fastrack!!!!!, thank you for shopping", "\n")
        if occupation == '2': # type: ignore
            pin_code = int(input('Enter your pincode:'))
            if pin_code in PinCodes:
                print('500 coupon on Books!!!!!','\n')
                if resident == '1':
                    hostel_name = input('Enter hostel name:')
                    if hostel_name.upper() in HostelNames:
                         print('250/- Discount on Groceries !!!!!',"\n")
    
        elif resident == '1':
            hostel_name = input('Enter hostel name:')
            if hostel_name.upper() in HostelNames:
                print('250/- Discount on Groceries !!!!!',"\n")


    print('Thank you for shopping','\n')
else:
    print('Thank you for shopping','\n')