# 类的定义
class Person:
    # 在类中定义的函数叫方法，__INIT__是一个特殊的方法，用来初始化对象, self 是一个特殊的参数，用来指向对象本身
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
p1 = Person("张三", 18)
