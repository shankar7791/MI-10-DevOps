class BMI :
    def __init__(self):
        self.weight = float(input("What is your weight? (Kg) : "))
        self.height = float(input("What is your height? (Mtr) "))

    def calculate(self):
        obj = self.weight/(self.height*self.height)
        print("Your BMI is : ", obj)

a = BMI()
a.calculate()
