# 集合list
list = [1, 2, 3, 4, 5]
list.append(6) # 向列表末尾添加元素
list.insert(0, 0) # 在指定位置插入元素
list.pop() # 删除并返回列表
print(list)

# 元组tuple, 元组是不可修改的
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (1,) # 元组中只有一个元素时，需要在元素后面添加逗号
tuple3 = (1, 2, [3, 4]) # 这里的元组在第三位上是一个list，这里面list是可变的，但是这里可变实际是list内内容改变，和js中的对象内存地址类似

# 字典dict, 字典是可变的，键值对的集合
dict1 = {'name': '张三', 'age': 18}
dict2 = dict(name='张三', age=18) # 另一种创建字典的方式
print(dict1)
print(dict2)

# 集合set, 集合是可变的，不重复的元素的集合
set1 = {1, 2, 3, 4, 5}
set2 = set([1, 2, 3, 4, 5]) # 另一种创建集合的方式
print(set1)
print(set2)