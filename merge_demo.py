import pandas as pd
import numpy as np

# s1 = pd.Series(['A', 'B', 'C'], index=list('123'))
# s2 = pd.Series(['D', 'E', 'F'], index=list('456'))
# print(s1), print(s2)
# print(pd.concat([s1, s2]))
#
# print('-----------concat rows---------------')
def make_df(cols, ind):
    data = {
        c: [str(c) + str(i) for i in ind] for c in cols
    }
    return pd.DataFrame(data, ind)
d1 = make_df('AB', [1, 2])
d2 = make_df('AB', [3, 4])
print(d1)
print(d2)
print(d1.append(d2))
print('---------------------------')
d3 = make_df('AB', [1, 2])
d4 = make_df('BC', [1, 2])
print(d3)
print(d4)
print(d3.append(d4))

# print(pd.concat([d1, d2]))
#
# print('------------concat columns--------------')
# d3 = make_df('AB', [0, 1])
# d4 = make_df('CD', [0, 1])
# print(d3)
# print(d4)
# print(pd.concat([d3, d4], axis=1))
# print('------------concat rows & 索引重复--------------')
# print(pd.concat([d3, d4]))
# print('------------concat rows & catch索引重复并抛异常--------------')
# # print(pd.concat([d3, d4], verify_integrity=True))
# print('------------索引重复:忽略并创建新索引--------------')
# print(pd.concat([d3, d4], ignore_index=True))
# print('------------索引重复:增加多级索引--------------')
# print(pd.concat([d3, d4], keys=['x', 'y']))
#




