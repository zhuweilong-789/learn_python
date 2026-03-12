# 函数的基本使用
def welcome():
    print("欢迎来到Python世界")

welcome()

# 定义一个空函数
def empty_func():
    # 相当于现在没想好函数的实现，先定义一个空函数
    pass

# python的函数可以返回多个值，但实际是返回了一个元组
def func():
    return 1, 2, 3

a, b, c = func() 
print(a, b, c) # 1 2 3
t = func()
print(t) # (1, 2, 3)




