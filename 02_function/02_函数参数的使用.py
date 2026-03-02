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