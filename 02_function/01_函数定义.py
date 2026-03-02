# 函数定义， 位置参数
def add(a, b):
    return a + b

# 关键字参数
def add_keyword(a=1, b=2):
    print(a + b)  

add_keyword()

# 限制传参方式， 具体规则：/前面的参数只能按位置传参，*后面的参数只能按关键字传参
def add_restrict(a, b, /, c, d, *args, e=1, f=2, **kwargs):
    print(a, b, c, d, args, e, f, kwargs)

add_restrict(1, 2, 3, 4, 5, 6, 7, e=10, f=20, g=30, h=40)



