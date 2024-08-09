class Person:
    def __init__(self, age, gender):
        self.age = age
        self.gender = gender

class SeniorCitizen(Person):
    def __init__(self, age, gender):
        super().__init__(age, gender)
                
    def senior_citizen_discount(self):
        if (self.gender.lower() == 'male' and self.age >= 60) or (self.gender.lower() == 'female' and self.age >= 45):
            print('15% Senior Citizen Discount Available')
        elif (self.gender.lower() == 'female' and self.age < 45):
            print("₹100 coupon for Nyka, Fastrack")
        elif (self.gender.lower() == 'male' and self.age < 60):
            print("₹100 coupon for Titan, Fastrack")
        else:
            print("No Senior Citizen Discount Available")

class StudentOrWorking(SeniorCitizen):
    def __init__(self, age, gender, occupation, resident):
        super().__init__(age, gender)
        self.occupation = occupation
        self.resident = resident

    def occupation_discount(self):
        if self.occupation == '2' and ((self.age < 60 and self.gender.lower() == 'male') or (self.age < 45 and self.gender.lower() == 'female')):  # Student
            pin_code = int(input('Enter your pincode: '))
            if pin_code in PinCodes:
                print('₹500 coupon on Books!!!!!')
                if self.resident == '1':  # Hosteller
                    hostel_name = input('Enter hostel name: ')
                    if hostel_name.upper() in HostelNames:
                        print('₹250 Discount on Groceries !!!!!')
            else:
                print("No discount based on pincode.")
        elif self.resident == '1'and ((self.age < 60 and self.gender.lower() == 'male') or (self.age < 45 and self.gender.lower() == 'female')):  # Hosteller
            hostel_name = input('Enter hostel name: ')
            if hostel_name.upper() in HostelNames:
                print('₹250 Discount on Groceries !!!!!')
        else:
            print("No additional discount available.")


age = int(input("Enter age: "))
gender = input("Enter gender (Male or Female): ")
occupation = input("Enter Occupation: \n1. Working\n2. Student \n3. Other\nEnter any number: ")
resident = input("Enter Residency: \n1. Hosteller\n2. Localite\nEnter any number: ")

PinCodes = [123, 456, 789]  # Sample PIN codes
HostelNames = ['ABC', 'CDE', 'EFG', 'HIJ']  # Sample hostel names

customer1 = StudentOrWorking(age, gender, occupation, resident)
customer1.senior_citizen_discount()
customer1.occupation_discount()
