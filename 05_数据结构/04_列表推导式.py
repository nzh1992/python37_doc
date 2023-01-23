# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2023/1/23
Last Modified: 2023/1/23
Description: 
"""
# 列表推导式
# 这是python提供一个更加单的创建列表的方法。
# 就是把某种操作应用于序列或者可迭代对象的每个元素上，然后使用其结果来创建列表，或者通过满足某些特定条件来创建子序列。

# 例如，创建一个平方列表。
l = [1, 2, 3, 4]
squares = []
for i in l:
    squares.append(i ** 2)

print(squares)


# 按照列表推导式的定义来看，我们还可以定义一个计算平方的函数，并将此函数应用到列表的所有元素上。
def cal_square(x):
    return x ** 2

squares2 = [cal_square(i) for i in l]
print(squares2)


# 列表推导式中还可以出现多个for子句
# 例如，输出一个3 * 3 的坐标系
locations = [(x, y) for x in [1,2,3] for y in [4,5,6]]
print(locations)

# 相当于嵌套for循环
locations2 = []
for x in [1,2,3]:
    for y in [4,5,6]:
        locations2.append((x, y))

print(locations2)


# 稍微复杂一些
# 当我们想循环一个嵌套列表，将每个元素放入同一列表时（拍平，或叫降维）
ll = [
    [1,2,3],
    [4,5,6]
]
new_l = [(idx, x) for idx, i in enumerate(ll) for x in i]
print(new_l)


# 条件筛选
# 在for子句后面添加if表达式即可。
# 注意，当有多个for子句时，if表达式判断位于最内层。


#