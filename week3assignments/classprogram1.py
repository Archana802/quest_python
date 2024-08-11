PinCodes = [123, 456, 789]  # Sample PIN codes
HostelNames = ['ABC', 'CDE', 'EFG', 'HIJ']  # Sample hostel names


class Person:
    def __init__(self, age, gender, resident):
        self.age = age
        self.gender = gender
        self.resident = resident

    def senior_citizen_discount(self):
        if (self.gender.lower() == 'male' and self.age >= 60) or (self.gender.lower() == 'female' and self.age >= 45):
            print('15% Senior Citizen Discount Available')
        else:
            return False
     
    def hostel_discount(self):
        if self.resident == '1'and (self.gender.lower() == 'female' and self.age < 45) or (self.gender.lower() == 'male' and self.age < 60) :  # Hosteller
            hostel_name = input('Enter hostel name: ')
            if hostel_name.upper() in HostelNames:
                print('₹250 Discount on Groceries !!!!!') 

    def youngsters_discount(self):    
        if (self.gender.lower() == 'female' and self.age < 45):
            print("₹100 coupon for Nyka, Fastrack")
        elif (self.gender.lower() == 'male' and self.age < 60):
            print("₹100 coupon for Titan, Fastrack")
        

class WorkingPeople(Person):
    def __init__(self, age, gender, resident):
        super().__init__(age, gender, resident)

'''
    def hostel_discount(self):
        if self.resident == '1'and (self.gender.lower() == 'female' and self.age < 45) or (self.gender.lower() == 'male' and self.age < 60) :  # Hosteller
            hostel_name = input('Enter hostel name: ')
            if hostel_name.upper() in HostelNames:
                print('₹250 Discount on Groceries !!!!!')
'''

"""class SeniorCitizen(Person):
    def __init__(self, age, gender, resident):
        super().__init__(age, gender, resident)
        """


class Student(Person):
    def __init__(self, age, gender, resident, occupation):
        super().__init__(age, gender, resident)
        self.occupation = occupation

    def student_discount(self):
        if self.occupation == '2' and (self.gender.lower() == 'female' and self.age < 45) or (self.gender.lower() == 'male' and self.age < 60):  # Student
            pin_code = int(input('Enter your PIN code: '))
            if pin_code in PinCodes:
                print('₹500 coupon on Books!!!!!')
                


# Input collection
age = int(input("Enter age: "))
gender = input("Enter gender (Male or Female): ")
occupation = input("Enter Occupation: \n1. Working\n2. Student \n3. Other\nEnter any number: ")
resident = input("Enter Residency: \n1. Hosteller\n2. Localite\nEnter any number: ")

# Creating the appropriate customer object
if occupation == '2':  # Student
    customer = Student(age, gender, resident, occupation)
elif occupation == '1':  # Working
    customer = WorkingPeople(age, gender, resident)
#else:  #  SeniorCitizen 
#   customer = SeniorCitizen(age, gender, resident)


# Applying Discounts
if isinstance(customer, Student):
    customer.student_discount()
    customer.hostel_discount()
    customer.youngsters_discount()
elif isinstance(customer, WorkingPeople):
    customer.youngsters_discount()
    customer.hostel_discount()
customer.senior_citizen_discount()


