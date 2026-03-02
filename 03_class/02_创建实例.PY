class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 实例方法
    def speak(self):
        print(f"我是{self.name}，我今年{self.age}岁")
        
p1 = Person("张三", 18)
p1.speak()
