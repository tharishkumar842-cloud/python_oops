class Car:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year

    def method1(self):
        print(f"The car's brand is {self.brand}")
        print(f"The car's year is {self.year}")

car1=Car("BMW",1999)
car1.method1()
car2=Car("Audi",2009)
car2.method1()
