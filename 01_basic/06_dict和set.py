# dict, 字典，键值对存储,其实就是js中的对象
d = {'name': '张三', 'age': 18}
print(d['name']) # 张三
print(d['age']) # 18
d2 = dict(name='李四', age=20)
print(d2) # {'name': '李四', 'age' : 20}

# dict常见的方法和使用
# 判断dict是否有某个key, 有以下两种方式
print('name' in d) # True
print(d.get('sex')) # None, 没有这个key时，返回None

# set 和对象的区别就是set是无序的，不能通过索引访问元素，且set只有key没有value
s = {1, 2, 3, 4, 5}
