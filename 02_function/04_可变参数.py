'''
可变位置参数: *args
'''
def func(*args):
    print(args) # 打印的是一个元组

func(1, 2, 3, 4, 5)
'''
可变关键字参数: **kwargs
'''
def fund(**kwargs):
    print(kwargs) # 打印的是一个字典

fund(a=1, b=2, c=3)