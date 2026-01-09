class Employee:

    company_name = "TechCorp"       #class variable

    def __init__(self, name, salary):
        self.name = name            # Instance variable
        self.salary = salary        # Instance variable

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Company: {Employee.company_name}")


# Create employee objects
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

# Display details
emp1.display()
emp2.display()
