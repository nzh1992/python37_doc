# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2023/1/23
Last Modified: 2023/1/23
Description: 本节学习列表的使用
"""

# 1.list.append(x)
# 在列表末尾添加一个元素
l = [1, 2, 3]
l.append(4)
# print(l)

# 如果用切片实现同样的功能
l[len(l):] = [5]
# print(l)


# 2. list.extend(iterable)
# 用可迭代对象从列表的末尾扩展列表
iter_a = range(3)
l2 = [1, 2, 3]
l2.extend(iter_a)
# print(l2)


# 3. list.insert(i, x)
# 在给定位置插入一个元素。第一个参数，索引位置。


# 4. list.remove(x)
# 移除列表中的一个值为x的元素。
# 如果没有值为x的元素，则引发ValueError异常。
# 如果有多个值为x的元素，则移除第一个（索引值最小的）。
l3 = [1, 2, 3, 2, 2]
l3.remove(2)
# print(l3)


# 5. list.pop([i])
# 删除列表中给定位置的元素，并返回它。
# 如果没有给定位置参数，将删除并返回列表最后一个元素。


# 6. list.clear()
# 移除列表中的所有元素。
# 等价于del a[:]
l6 = [1, 2, 3]
l6.clear()
# print(l6)


# 7. list.index(x[, start[, end]])
# 返回列表中第一个值为x的元素的从零开始的索引。
# 如果没有值为x的元素，将抛出ValueError异常。
# start和end，用于限定列表的索引的搜索范围。范围区间左闭右开。
# 需要注意，当start和end指定的搜索范围超过列表的实际索引范围时，一定会引发ValueError异常。
l7 = [1, 2, 3, 2, 2, 1]
l7_idx = l7.index(2, 2, 20)
# print(l7_idx)


# 8. list.count(x)
# 返回元素x在列表中出现的次数


# 9. list.sort(key=None, reverse=False)
# 对列表中的元素进行排序。
# 注意，此方法会改变元素在原列表的位置。

# 9.1 不传参数
# 默认升序排列
l91 = [1, 3, 5, 4, 2]
l91.sort()
# print(l91)

# 9.2 当列表中的元素是dict类型时，可以根据dict的某个key进行排序
l92 = [
    {'a': 1, 'b': 5},
    {'a': 1, 'b': 4},
    {'a': 2, 'b': 6},
]
l92.sort(key=lambda x: x['a'])
# print(l92)

# 也支持对dict中的多个key进行排序，但是lambda表示的返回值需要是一个元组(tuple)类型
# 当对多个key排序时，lambda表达式的返回值中key的顺序，就是排序的优先级。
# 当前例子，就是先根据a排序，再根究b排序
l92.sort(key=lambda x: (x['a'], x['b']))
# print(l92)


# 当dict中缺少排序key时，则会引发KeyError异常。
# 原因是，在lambda表达式中，获取key为'a'的值时，缺少key为'a'的键值对，导致dict['a']报错。
l922 = [
    {'a': 1, 'b': 5},
    {'b': 4},
    {'a': 2, 'b': 6},
]
l922.sort(key=lambda x: x['a'])
print(l922)


# 10. list.reverse()
# 翻转列表中的元素


# 11. list.copy()
# 返回列表的一个浅拷贝，相当于a[:]
