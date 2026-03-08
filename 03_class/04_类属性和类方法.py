class Person:
    # 类属性
    country = "中国"
    def __init__(self, name, age):
        # 实例属性
        self.name = name
        self.age = age
    # 实例方法
    def speak(self):
        print(f"我是{self.name}，我今年{self.age}岁")

    @classmethod
    def run(cls):
        print(f"{cls.country}的人都在跑")

    @classmethod
    # 工厂方法： 通过提供一个接口创建一个实例对象
    def create(cls, name, age):
        return cls(name, age)

p = Person.create("张三", 18)
print(p.__dict__)
