import numpy as np
import pandas as pd


# x = pd.DataFrame(np.random.randint(1, 10, (4, 2)),
#                  index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
#                  columns=['data1', 'data2'])
# print(x)
# print('-------------------')
# x.index.names = ['row_group', 'row_name']
# print(x)
# print('-------------------')
#
# y = pd.Series(
#     {
#         ('wuhan', 2000): 100,
#         ('wuhan', 2010): 220,
#         ('shanghai', 2000): 330,
#         ('shanghai', 2010): 900,
#         ('guangzhou', 2000): 110,
#         ('guangzhou', 2010): 500
#     }
# )
# print(y)
# print('-------------------')
# y.index.names = ['area', 'year']
# print(y)
#
# print('***********************')
# # from_product:笛卡尔积
# # 行索引
# index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]], names=['year', 'visit'])
# # 列索引
# columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']], names=['subject', 'type'])
# # 模拟数据
# data = np.round(np.random.randn(4, 6), 1)
# data[:, ::2] *= 10
# data += 37
# # print(data)
# # 数据填充
# health_data = pd.DataFrame(data, index=index, columns=columns)
# print(health_data)


# y = pd.Series(
#     {
#         ('wuhan', 2000): 100,
#         ('wuhan', 2010): 220,
#         ('shanghai', 2000): 330,
#         ('shanghai', 2010): 900,
#         ('guangzhou', 2000): 110,
#         ('guangzhou', 2010): 500
#     }
# )
# # print(y)
# # print('-------------------')
# y.index.names = ['area', 'year']
# print(y)
# print('-------------------')
# print(y['wuhan'])
# print('-------------------')
# # 高级索引-->低级索引
# print(y['wuhan', 2000])
# print('-------------------')
# # 需要有序
# # print(y.loc['wuhan':'shanghai'])
# print(y.loc[:, 2000])
# print('-------------------')
# print(y[y > 200])
# print('-------------------')
# # 无需有序
# print(y[['wuhan', 'guangzhou']])
from pandas.tests.indexes.multi.conftest import idx

# index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]], names=['year', 'visit'])
# # 列索引
# columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']], names=['subject', 'type'])
# # 模拟数据
# data = np.round(np.random.randn(4, 6), 1)
# data[:, ::2] *= 10
# data += 37
# # print(data)
# # 数据填充
# health_data = pd.DataFrame(data, index=index, columns=columns)
# print(health_data)
# print('-----------------------------------')
# # 高级索引--> 低级索引
# print(health_data['Bob', 'HR'])
# print('-----------------------------------')
# print(health_data.iloc[:2, :2])
# print('-----------------------------------')
# # 行：所有行；列：高级索引&低级索引组合过滤
# print(health_data.loc[:, ('Bob', 'HR')])
# print('-----------------------------------')
# # idx[:, 1]:行：高级索引全选，低级索引为1的行； idx[:, 'HR']：列：高级索引全选，低级索引为'HR'的列
# idx = pd.IndexSlice
# print(health_data.loc[idx[:, 1], idx[:, 'HR']])

# y = pd.Series(
#     {
#         ('wuhan', 2000): 100,
#         ('wuhan', 2010): 220,
#         ('shanghai', 2000): 330,
#         ('shanghai', 2010): 900,
#         ('guangzhou', 2000): 110,
#         ('guangzhou', 2010): 500
#     }
# )
# y.index.names = ['area', 'year']
# print(y)
# print('-------------------')
# print(y.sort_index())
# print('-------------------')
# print(y.sort_index().loc['shanghai':'wuhan'])

# y = pd.Series(
#     {
#         ('wuhan', 2000): 100,
#         ('wuhan', 2010): 220,
#         ('shanghai', 2000): 330,
#         ('shanghai', 2010): 900,
#         ('guangzhou', 2000): 110,
#         ('guangzhou', 2010): 500
#     }
# )
# y.index.names = ['area', 'year']
# # y = y.unstack()
# print(y)
# print('--------------------')
# y = y.reset_index(name='population')
# print(y)
# print('--------------------')
# print(y.set_index(['area', 'year']))


# print(y.stack())
# print('---------低级索引----------')
# print(y.stack())

# print('--------高层级:level=0-----------')
# print(y.unstack(level=0))
# print('---------低层级:level=1----------')
# print(y.unstack(level=1))


# index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]], names=['year', 'visit'])
# # 列索引
# columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']], names=['subject', 'type'])
# # 模拟数据
# data = np.round(np.random.randn(4, 6), 1)
# data[:, ::2] *= 10
# data += 37
# # print(data)
# # 数据填充
# health_data = pd.DataFrame(data, index=index, columns=columns)
# print(health_data)
# print('-----------行索引：按year分组取平均值-------------')
# print(health_data.mean(level='year'))
# print('-----------列索引：按type分组取平均值-------------')
# print(health_data.mean(axis=1, level='type'))