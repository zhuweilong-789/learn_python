'''
引入模块的方式

1. 直接引入模块
import pay
pay.wechant_pay(100)

2. 引入模块的某个函数
from pay import wechant_pay
wechant_pay(100)

3. 引入模块的所有函数
from pay import *
wechant_pay(100)
ali_pay(100)
info()

通过别名引入
import pay as p
import order as o

p.wechant_pay(100)
o.create_order(1000)

'''