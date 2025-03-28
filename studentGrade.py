#Student Grade Tracker Class: Student Attributes: name, roll_no, marks (dictionary of subject: mark) Method to:Add a subject and mark, 
#Calculate average, Display all details

class Student:
    def __init__(self,name, roll_no):
        self.name=name
        self.roll_no= roll_no
        self.marks = {}
        
    def add_subject(self, subject, marks):
        self.marks[subject]= marks
        print(f"Added {subject }:{marks}")
        
    def calculate_average(self):
        if len(self.marks) == 0:
            return 0
        total=sum(self.marks.values())
        count=len(self.marks)
        return total/count

    def display_details(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}")
        print("Marks:")
        for subject, mark in self.marks.items():
            print(f"{subject}: {mark}")
        print(f"Average: {self.calculate_average()}")


student = Student("Sheeba", 22)
student.add_subject("Math", 85)
student.add_subject("Science", 90)
student.display_details()
