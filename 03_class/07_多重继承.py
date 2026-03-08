class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print(f"我是{self.name}，我今年{self.age}岁")

class Worder():
  def __init__(self, job):
    self.job = job

class Student(Person, Worder):
    def __init__(self, name, age, job, student_id):
        Person.__init__(self, name, age)  
        Worder.__init__(self, job)
        self.student_id = student_id

s = Student("张三", 18, "教师", "2023001")
print(s.__dict__)

    