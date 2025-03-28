# Employee Hierarchy Base class: Employee (name, salary) Derived classes: Manager, Developer 
# Add extra attributes/methods to each child (e.g., project for Developer)

class Employee:
    def __init__(self, name, salary):
        self.name= name
        self.salary= salary
        
    def describe(self):
        print(f" Employee: {self.name}, Salary: {self.salary}")
              
    
class Manager(Employee):
        def __init__(self,name, salary,dept):
            self.name=name
            self.salary=salary
            self.dept=dept
            
        def describe(self):
            print(f" Manager Employee {self.name}, Salary: { self.salary}, Department: { self.dept}")
        
class Developer(Employee):
        def __init__(self,name, salary,dept):
            self.name=name
            self.salary=salary
            self.dept=dept
            
        def describe(self):
            print(f" Developer Employee {self.name}, Salary: { self.salary}, Department: { self.dept}")

manager = Manager("SOWMYA", 80000, "HR")
developer = Developer("PAVAN", 60000, "AI")

manager.describe()
developer.describe()
          
        