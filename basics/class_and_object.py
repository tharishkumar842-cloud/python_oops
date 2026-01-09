class student():

    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no

    def method1(self):
        print(f"Name is {self.name}")
        print(f"Roll number is {self.roll_no}")

s=student("kumar","10")
s.method1()