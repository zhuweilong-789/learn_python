# 整数类型
age = 18
sum = 1_000_000  # 下划线可以用于分隔数字，提高可读性

# 浮点数类型
height = 1.75
weight = 70.5

# 字符串
name = "张三"
'''
1. 字符串通过+拼接
2. 字符串通过%格式化输出
    %s 字符串
    %d 整数
    %f 浮点数
3. 通过fString方式格式化输出
    格式：f'字符串{变量}'
'''
print('姓名' + name)
print('默认浮点数精度为6位%f' % weight)
print(f'姓名{name}，年龄{age}岁')

# 布尔类型
'''
布尔类型，只有 True 和 False 两个值
运算符，
    比较运算符：==, !=, >, <, >=, <=
    逻辑运算符：and, or, not
'''
is_student = True
is_girl = False

# 空值, 类似js的null
none_value = None

# python上的字符串数据是存储在堆上， js返回的结果也是一样的
age1 = 100
age2 = age1
age1 = 200
print(age1) # 200
print(age2) # 100
