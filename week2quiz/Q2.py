"""
Write a code to demonstrate use of inheritance and polymorphism using below example:
1. Eatable
1.1 Vegetarian
1.2 Non-Vegetarian

properties to be used: carbs, fat, protein, isPeelable, isBoneless def describe(self):
        base_description = super().describe()
        peelable = "Peelable" if self.isPeelable else "Not Peelable"
        return f"Vegetarian - {base_description}, {peelable}"

Place appropriate properties in parent class or child class and assign the values in __init__ 
"""

class Eatable:
    def __init__(self,carbs,fat, protein):
        self.carbs = carbs
        self.fat = fat
        self.protein = protein

class vegetarian(Eatable): #for inheritance
    def __init__(self,carbs,fat, protein, isPeelable):
        super().__init__(carbs,fat, protein)
        self.isPeelable = isPeelable
    
    def food(self):   #for polymorphism
        if self.isPeelable == True:
            print('The food item is peelable')
        else:
            print('The food item is not peelable')   

class nonVegetarian(Eatable): 
    def __init__(self,carbs,fat, protein, isBoneless):
        super().__init__(carbs,fat, protein) 
        self.isBoneless = isBoneless  

    def food(self):   #for polymorphism
        if self.isBoneless == True:
            print('The food item is boneless')
        else:
            print('The food item has bones')