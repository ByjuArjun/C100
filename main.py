class Car():

    def __init__(self, brand, model, year, color):
        self.brand=brand
        self.model=model
        self.year=year
        self.color=color
    
    def info(self):
        print("The brand is", self.brand)
        print("The model is", self.model)
        print("The year is", self.year)
    
    def type(self):
        car1=int(input("Enter Your Amount of Miles Traveled"))
        car2=int(input("Enter your Amount of Gas Refilled"))
        total = car1/car2
        print("Your Mileage Is:", total)

c1=Car("Mercedes", "Amg", 2024, "Black")
c1.info()
c1.type()

c2=Car("BMW", "M4", 2023, "Blue")
c2.info()
c2.type()