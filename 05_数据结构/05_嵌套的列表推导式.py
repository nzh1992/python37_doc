# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2023/1/23
Last Modified: 2023/1/23
Description: 
"""
# 例如，有一个 3 * 4的矩阵，交换行和列
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# 交换行和列
transposed = [[row[i] for row in matrix] for i in range(4)]
print(transposed)

# 等价于
transposed2 = []
for i in range(4):
    transposed2.append([row[i] for row in matrix])
print(transposed2)

# 还等价于
transposed3 = []
for i in range(4):

    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])

    transposed3.append(transposed_row)

print(transposed3)


# 还有更好的办法，zip函数
zipped = zip(*matrix)
print(zipped)

print(list(zipped))