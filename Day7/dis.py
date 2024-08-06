
 # type: ignore
#Ecommerce discount program 

age = int(input("Enter age: "))
gender = input("Enter gender: \n1. Male\n2. Female\n3. Other\nEnter any number:")

if gender == '1'and '3':
    if age >= 60:
        print(" 15% Senior citizen discount applied, thank you for shopping", "\n")
    else :
        print("100 voucher Fastrack & Titan!!!!!, thank you for shopping", "\n")
elif gender == '2':
    if age >= 45:
        print(" 15% Senior citizen discount applied, thank you for shopping", "\n")
    else :
        print("100/- Discount on Nykaa & fastrack!!!!!, thank you for shopping", "\n")

occupation = input("Enter Ocupation: \n1. working\n2. Student \n3. other\nEnter any number:")

if occupation == '2':
    pin_code = int(input('Enter your pincode:'))
    if pin_code in [123, 456, 789]:
        print('500 coupon on Books!!!!!','\n')
        resident = input("Enter Residency: \n1. Hosteller\n2. Localite \nEnter any number:")
        if resident == '1':
            hostel_name = input('Enter hostel name:')
            if hostel_name in ['ABC', 'CDE', 'EFG', 'HIJ']:
                     print('250/- Discount on Groceries !!!!!',"\n")
        
        print('Thank you for shopping','\n')
else:
    print('Thank you for shopping','\n')

        
    


