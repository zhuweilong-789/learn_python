# 函数参数的使用
def order(num, price):
    print(f"您点了{num}份商品，单价{price}元，总价{num * price}元")

order(2, 10)

# 关键字参数，这样调用函数，参数的顺序可以任意，其实和js中函数的解构赋值很像
order(price=10, num=2)

# 限制传参方式， 具体规则：/前面的参数只能按位置传参，*后面的参数只能按关键字传参
def order_restrict(num, price, /, age, *, name):
    print(f"您点了{num}份商品，单价{price}元，总价{num * price}元")
    print(f"您的姓名是{name}，您的年龄是{age}岁")
order_restrict(2, 10, 18, name="张三") # age可以是位置参数，也可以是关键字参数
order_restrict(2, 10, age=18, name="张三")


# 默认参数
def order_default(num, price=10):
    print(f"您点了{num}份商品，单价{price}元，总价{num * price}元")

order_default(2) # 没有传price参数，默认使用10元
order_default(2, 15) # 传了price参数，使用传进来的15元

# 可变参数
def order_var(num, *prices):
    print(f"您点了{num}份商品，单价{prices}元，总价{num * sum(prices)}元")

order_var(2, 10, 15) # 10和15是可变参数，传进来的参数会被打包成一个元组
order_var(2, 10, 15, 20) # 10, 15, 20是可变参数，传进来的参数会被打包成一个元组


 # 关键字可变参数
def order_kwargs(num, **kwargs):
    print(f"您点了{num}份商品，单价{kwargs}元，总价{num * sum(kwargs.values())}元")

order_kwargs(2, a=10, b=15) # a=10, b=15是关键字可变参数，传进来的参数会被打包成一个字典
order_kwargs(2, a=10, b=15, c=20) # a=10, b=15, c=20是关键字可变参数，传进来的参数会被打包成一个字典