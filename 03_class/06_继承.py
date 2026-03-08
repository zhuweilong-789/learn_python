class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print(f"我是{self.name}，我今年{self.age}岁")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    # 重写父类的方法
    def speak(self):
        # 调用父类的方法
        super().speak() # 先调用父类的方法
        print(f"我是{self.name}，我今年{self.age}岁，我的学号是{self.student_id}")
    


s = Student("张三", 18, "2023001")
print(s.__dict__)