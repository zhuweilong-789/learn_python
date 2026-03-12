def welcome():
    print("欢迎来到Python世界")

print(type(welcome)) # <class 'function'>

# 函数可以动态添加属性
welcome.name = "欢迎函数"
print(welcome.name) # 欢迎函数

# 可变参数和不可变参数，实际就是内存分析相关的知识点
a = "李四"
def setName(name):
    name = "张三"
    print(name) # 张三

setName(a)
print(a) # 李四

# 函数作为参数

# 函数作为返回值

# 三元表达式
a = 10
b = 20
c = a if a > b else b 
print(c) # 20
