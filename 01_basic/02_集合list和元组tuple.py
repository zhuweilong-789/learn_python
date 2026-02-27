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