import numpy as np

# # 基于列表创建数组：数组中元素类型必须一致
# print(np.array([1, 2, 3.14, 5]))
# # 长度为10，每个元素均为0的数组
# print(np.zeros(10, dtype=int))
# #3*5的数组，每个元素均为浮点型1.0
# print(np.ones((3, 5), dtype=float))
# #3*5的数组，每个元素均为3.14
# print(np.full((3, 5), 3.14))
# #从0开始，20结束(不包含20)，步长为2
# print(np.arange(0, 20, 2))
# #3*3，0~1随机均匀分布的数组
# print(np.random.random((3, 3)))
# #3*3,均值为0方差为1的正态分布随机数组
# print(np.random.normal(0, 1, (3, 3)))
# #3*3,[0,10]区间取值的随机整数数组
# print(np.random.randint(0, 10, (3, 3)))
# #3*3单位矩阵
# print(np.eye(3))
# #3个整数组成的未初始化数组
# print(np.empty(3))
# #5个元素的数组，5个元素平分到0~1
# print(np.linspace(0, 1, 5))
# x1 = np.arange(10)
# print(x1)
# print(x1[:5])#前5个元素
# print(x1[4:7])#第5到第7个元素，左闭右开
# x2 = np.random.randint(10, size=(4, 6))
# print(x2)
# print(x2[1:3, 2:5])
# print(x2[:4, ::2])
# print(x2[::-1, ::-1])

# x2 = np.random.randint(10, size=(4, 6))
# x2_copy = x2.copy()
# print(x2_copy)
# x2_copy[0,1]=100
# print(x2)
# print(x2_copy)



# x3 = np.random.randint(10, size=(3, 6, 2))
# # print(x3) #三维数组
# print(x3.ndim) #数组维度
# print(x3.shape) #每个维度大小
# print(x3.size) #数组总大小

#将数字0-9，放入2*5的矩阵
# arr = np.arange(0, 10)
# print(arr)
# print('-------------')
# grid = arr.reshape((2, 5))
# print(grid)
# print('-------------')
#
# x=np.array([1, 5, 7, 9])
# print(x)
# print('-------------')
# #数组--->行向量
# print(x.reshape((1, 4)))
# print(x[np.newaxis, :])
# print('-------------')
# #数组--->列向量
# print(x.reshape((4, 1)))
# print(x[:, np.newaxis])

# x = np.array([1, 2, 3])
# y = np.array([4, 5, 6])
# z = np.array([7, 8, 9])
# print(np.concatenate([x, y, z]))
# print('-------------')
#
# grid_1 = np.array([
#    [1, 2, 3],
#    [4, 5, 6]
# ])
# grid_2 = np.array([
#    [7, 7, 7],
#    [8, 8, 8]
# ])
# #纵向拼接
# print(np.concatenate([grid_1, grid_2]))
# print('-------------')
# #横向拼接
# print(np.concatenate([grid_1, grid_2], axis=1))
#
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# x1, x2, x3 = np.split(x, [2, 7])
# print(x1, x2, x3)
# print('*************')
# grid = np.arange(30).reshape((5, 6))
# print(grid)
# print('*************')
# #纵向分割
# upper, middle, lower = np.vsplit(grid, [2, 3])
# print(upper)
# print('-------------')
# print(middle)
# print('-------------')
# print(lower)
# print('*************')
#
# #横向分割
# left, between, right = np.hsplit(grid, [1, 4])
# print(left)
# print('-------------')
# print(between)
# print('-------------')
# print(right)

# x = np.arange(0, 5)
# print('x:', x)
# print('2**x:', np.power(2,x))
# y = np.zeros(10)
# print('old_y:', y)
# np.power(2, x, out=y[::2])
# print('new_y:', y)

# x = np.arange(1, 6)
# print(x)
# #sum(1,2,3,4,5)
# print('add-reduce', np.add.reduce(x))
# print('add-accumulate', np.add.accumulate(x))
# # 1*2*3*4*5
# print('multiply-reduce', np.multiply.reduce(x))
# print('multiply-accumulate', np.multiply.accumulate(x))

# x = np.arange(1, 6)
# y = np.arange(6, 11)
# print('x:', x)
# print('y:', y)
# print('multiply-outer:\n', np.multiply.outer(x, y))


