class Person:
    def __init__(self, name, age, gender):
        self.name = name  # 公共属性
        self._age = age  # 受保护属性,子类可以访问
        self.__gender = gender  # 私有属性，只能在类的内部访问

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

p = Person("张三", 18, "男")
print(p.age)
p.age = 20
print(p.age)