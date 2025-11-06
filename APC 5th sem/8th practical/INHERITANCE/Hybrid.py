class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def info(self):
        print("name of student is:", self.name)
        print("roll number of " + self.name + " is " + str(self.roll))

class Exam(Student):
    def endsem(self):
        print(self.name + " have completed exam of endsem")

class Project:
    def __init__(self, marks):
        self.marks = marks

class Result(Project, Exam):
    def __init__(self, name, roll, marks):
        Student.__init__(self, name, roll)  # Initialize Student part
        Project.__init__(self, marks)       # Initialize Project part
    
    def res(self):
        print(f"{self.name} is passed in exam with {self.marks} marks")

# Creating object and calling methods
obj = Result("sarvesh", 42, 90)
obj.info()
obj.endsem()
obj.res()