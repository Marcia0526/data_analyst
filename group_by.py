import seaborn as sns
# import pandas as pd

# seaborn默认提供很多数据集，可通过load_dataset加载
planets = sns.load_dataset('planets')
df = planets.iloc[25:35, :].fillna(method='ffill', axis=0).fillna(method='bfill', axis=0)
# print(df)
print(df)
print('-----------------------------------------')
# # 按行取均值
# print(df.mean())
# print('-----------------------------------------')
# # 按列取均值
# print(df.mean(axis=1))
# print('-----------------------------------------')
# print(df.describe())
# print(df.groupby('method')['orbital_period'].median())

# for (method, group) in df.groupby('method'):
#     print('group_name:', method, '\n')
#     print(group)
#     print('~~~~~~~~~~~~~~~~~~')

# print(df.groupby('method')['year'].describe())

# print(df[['method','mass', 'year']].groupby('method').aggregate(['min', 'max', 'median']))


# def self_fun(x):
#     return (x['mass'].min() > 5) & (x['year'].min() > 2000)
#
# print(df.groupby('method').filter(self_fun))

# print(df.groupby('method').transform(lambda x: x-x.mean()))

# def self_fun(x):
#     x['new_columns'] = x['mass'] + x['year']
#     return x
#
#
# print(df[['method', 'mass', 'year']].groupby('method').apply(self_fun))

# print(df['maethod'])a
# L = [0, 1, 0, 0, 0, 1, 1, 1, 1, 'a']
# print(df.groupby(L).sum())
# print(df.groupby(df['method']).sum())

df = df.set_index('method')
print(df)
mapping = {
    'Radial Velocity': 'group_A',
    'Imaging': 'group_A',
    'Eclipse Timing Variations': 'group_B'
}
print(df.groupby([str.lower, mapping]).mean())
print(df.groupby([mapping, str.lower]).mean())
# print(df.groupby(str.lower).mean())

# print(df.groupby(mapping).sum())
