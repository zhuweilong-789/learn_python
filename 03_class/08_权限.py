class Person:
    def __init__(self, name, age, gender):
        self.name = name  # 公共属性
        self._age = age  # 受保护属性,子类可以访问
        self.__gender = gender  # 私有属性，只能在类的内部访问

class Student(Person):
    def __init__(self, name, age, gender, student_id):
        Person.__init__(self, name, age, gender)
        self.student_id = student_id

s = Student("张三", 18, "男", "2023001")
print(s.name)
print(s._age)
#print(s.__gender)