class Person:
    def __init__(self,name):
        self.name=name

    def info(self):
        print("name of person is:",self.name)

class Student(Person):
    def prof(self):
        print(self.name," is student  ")

obj=Student("sarvesh")
obj.info()
obj.prof()
