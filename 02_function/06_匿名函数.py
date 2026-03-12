# 匿名函数，也叫lambda函数，是一种没有函数名的函数，通常用于简单的函数场景
# 语法：lambda 参数列表: 表达式
# 例如：lambda x, y: x + y 表示一个接受两个参数x和y，返回它们的和的函数
# 例如：lambda x: x * x 表示一个接受一个参数x，返回它的平方的函数

sum = lambda x, y: x + y
print(sum(1, 2)) # 3
