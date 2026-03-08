class Person:
    def __init__(self, name, age):
        # 实例属性
        self.name = name
        self.age = age
    # 实例方法
    def speak(self):
        print(f"我是{self.name}，我今年{self.age}岁")

p1 = Person("张三", 18)
# 通过实例.属性名 = 值 给实例添加的属性就是实例属性
p1.gender = "男"
print(p1.gender)

