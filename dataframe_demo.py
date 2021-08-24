import pandas as pd
import numpy as np
# # series--->dataframe
# d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
#    'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
# df = pd.DataFrame(d)
# print(df)
# print(df.index)
# print(df.columns)
# # index:行标签  columns：列标签
# # dict ---> dataframe
# d2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
# print(pd.DataFrame(d2))
#
# # list ---> dataframe
# d3 = {'one': [1., 2., 3., 4.],
#    'two': [4., 3., 2., 1.]}
# print(pd.DataFrame(d3))
#
# # tuple ---> 多层索引dataframe
# d4 = {
#     ('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
#     ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
#     ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
#     ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
#     ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}
# }
# print(pd.DataFrame(d4))

area = pd.Series({
    'wuhan': 100,
    'changsha': 220,
    'shanghai': 330,
    'beijing': 900,
    'guangzhou': 110
})
pop = pd.Series({
    'wuhan': 38332521,
    'changsha': 26448193,
    'shanghai': 19651127,
    'beijing': 19552860,
    'guangzhou': 12882135
})
data = pd.DataFrame({
    'area': area,
    'pop': pop
})
# print(data)

# 建议使用data['area']
# print(data['area'])
# print(data.area)
data['density'] = data['pop']/data['area']
# print(data.values)
# print(data.values[0])
# print(data.T)
# print(data)
# data.iloc[1, 0] = 250
# print(data)
# print(data.loc[data['area'] > 200, ['area', 'pop']])
# print(data['area'] > 200)
# print(data[data['area'] > 200])
# print(data['pop'])
# print(data['changsha':'beijing'])
# print(data[0:2])
# print(data.iloc[1:3, :2])
# print(data.iloc[0, 2])
# print(data.loc[:'shanghai', :'pop'])

# data = pd.DataFrame(np.random.randint(1, 10, (3, 5)), columns=['a', 'b', 'c', 'd', 'e'])
# print('data:\n', data)
# print('-------------------')
# print(np.power(data, 2))

# x = pd.DataFrame(np.random.randint(1, 6, (2, 3)), columns=list('abc'))
# print('x:\n', x)
# print('-------------------')
# y = pd.DataFrame(np.random.randint(1, 6, (3, 2)), columns=list('ab'))
# print('y:\n', y)
# print('------x+y：含缺失值：Na----------')
# print( x + y)
# print('-------x中所有元素的平均值---------')
# fill = x.stack().mean() # x中所有元素的平均值
# print(fill)
# print('------缺失值填充----------')
# print(x.add(y, fill_value=fill))

# x = pd.DataFrame(np.random.randint(1, 10, (3, 4)), columns=list('abcd'))
# print('x:\n', x)
# print('-------------------')
# gap = x['b']
# print(gap)
# # 每列减列值
# print('-------列运算：axis=0------------')
# print(x.subtract(gap, axis=0))
# # 每列减行值
# print('-------行运算------------')
# delta = x.iloc[0]
# print(delta)
# print('-------------------')
# print(x.subtract(delta))

# x = np.array([1, np.nan, 3, 4])
# print('x:', x)
# print(x.dtype)
# y = np.array([1, 2, 3, 4])
# print(y.dtype)

# x = pd.Series([1, np.nan, 'hello', None])
# print('origional_x:\n', x)
# print('-----series-dropna-------')
# print(x.dropna())
#
# print('***********分割线***************')
#
# y = pd.DataFrame([
#     [1, np.nan, 2],
#     [2, 3, 5],
#     [None, 4, 6]
# ])
# print('origional_y:\n', y)
# print('-------dataframe-dropna-----------')
# # 默认剔除所有含缺失值的行
# print(y.dropna())
# print('-------------------------')
# # 剔除所有含缺失值的列
# print(y.dropna(axis='columns'))
# print('***********分割线***************')
#
# y[3] = [None, None, None]
# print('new_y:\n', y)
# print(y.dropna(axis='columns', how='all'))
# print(y.dropna(axis='columns', thresh=3))
# print('-----------y_T-------------')
# print('y_T:\n', y.T)
# print(y.T.dropna(how='all'))
# print(y.T.dropna(axis='rows', thresh=3))

x = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
print('x:\n', x)
print('------fillna with 0------')
print(x.fillna(0))
print('------fillna with forward-fill------')
print(x.fillna(method='ffill'))
print('------fillna with back-fill------')
print(x.fillna(method='bfill'))

print('***********分割线***************')

y = pd.DataFrame([
    [1, np.nan, 2, None],
    [2, 3, 5, None],
    [None, 4, 6, None]
])
print('y:\n', y)
print('------fillna with 0------')
print(y.fillna(0))
print('------fillna with forward-fill based on rows------')
print(y.fillna(method='ffill', axis=1))
print('------fillna with back-fill based on columns------')
print(y.fillna(method='bfill', axis=0))




