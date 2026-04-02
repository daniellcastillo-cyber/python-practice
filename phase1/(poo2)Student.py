
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []


    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        return round(sum(self.grades) / len(self.grades), 2)
    
    def get_status(self):
        if self.get_average() >= 60:
            return "passed"
        else:
            return "failed"


student = Student('Daniel')
student.add_grade(80)
student.add_grade(75)
student.add_grade(90)
print(student.get_average())
print(student.get_status())