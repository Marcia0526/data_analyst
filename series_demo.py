import pandas as pd
import numpy as np

# s1 = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
# s2 = pd.Series(np.random.randn(5))
# print(s1)
# print(s2)
# print(s1['a'])
# print(s2[0])
# print(s1.get('b'))
# print(s1.get('f', np.nan))

s = pd.Series([1, 2, 'hello', 9], index=['a','b','c','d'])
print(s)
print(s['a'])
print(s.get('f'))
print(s.index)
print(s.values)  #返回数组
print(s.describe())
s = s.drop('c')
print(s)
s['a'] = 'world'
print(s)



# 字典
# d = {'b': 1, 'a': 0, 'c': 2}
# s1 = pd.Series(d)
# s2 = pd.Series(d, index=['b', 'c', 'd', 'a'])
# print(s1)
# print(s2)

# 标量
# s1 = pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])
# print(s1)