# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2023/1/23
Last Modified: 2023/1/23
Description: 
"""
import datetime

# 元组
# 元组是有几个由逗号分开的值组成
t1 = 123, '456', datetime.datetime.now()
# print(t1)

# 元素也可能是被嵌套的
t2 = 123, '456', [1, 2, 3]
print(t2)
print(t2[2])

# 元组中的每个元素是不可被修改的。
# 这句话不严谨，应该是，元组中每个不可变元素是不能被修改的。
# 例如元组中有list类型的元素时，我们仍可以修改了list中的元素。
# 原因在于，不可变对象，修改值时是在内存中重新开辟一块内存，然后存储值，此时不可变对象的内存地址(也就是引用)发生了变化
# 而tuple会检查每个元素的内存地址，如果内存地址变化了，则会引发TypeError异常。
# 但元素为可变对象时（例如list），即使修改了可变对象的内容，但是可变对象的内存地址（引用）没有发生任何变化。
t2[2][0] = 10
print(t2)


# 序列解包
t3 = (1, 'b', 5, 8)
x, y, z, i = t3
print(x, y, z, i)

# 只要前两个元素
print(t3[0:2])      # 支持切片
x, y = t3[0:2]
print(x, y)