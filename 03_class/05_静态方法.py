class Person: 
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  # 静态方法：实际上就是这个类的一个工具方法
  @staticmethod
  def is_adult(age):
    return age >= 18

# 判断年龄是否大于18
print(Person.is_adult(18))