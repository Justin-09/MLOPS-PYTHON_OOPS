class Employees:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display(self):        print(f"Name: {self.name}, Salary: {self.salary}")
emp1 = Employees("Alice", 50000)
emp2 = Employees("Bob", 60000)
emp1.display()
emp2.display()  

a = "commited to justin branch"