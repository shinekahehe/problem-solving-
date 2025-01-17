class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    
    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
student=Student("Anu", [90, 98, 96, 95, 99])
print("Student name:", student.name)
print("Average:", student.average())
