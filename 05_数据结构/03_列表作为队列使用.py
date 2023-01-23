# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2023/1/23
Last Modified: 2023/1/23
Description: 
"""
# 队列
# 先进先出。

# 分析
# 由于list本质上是数组，所以在出队的时候，从第二个元素开始，每个元素都需要向前挪动一位，这会导致随着队列中元素的变多，效率变得越差。
# 所以需要借助 collections.deque 来实现。

from collections import deque

my_queue = deque([])

# 入队
my_queue.append(1)
my_queue.append(2)

# 出队
first_ele = my_queue.popleft()
second_ele = my_queue.popleft()
print(first_ele)
print(second_ele)

# 注意，当队列中没有元素时，再调用popleft方法，会引发IndexError异常
third_ele = my_queue.popleft()
print(third_ele)