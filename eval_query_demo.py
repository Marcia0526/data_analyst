
import pandas as pd
import numpy as np

rng = np.random
df1 = pd.DataFrame(rng.randint(0, 1000, (5, 3)), columns=['a', 'b', 'c'])
# print(df1)
# print(df2)
# print(df3)
# print(df4)
# print(df5)
# r1 = -df1 * df2 / (df3 + df4) - df5
# r2 = pd.eval('-df1 * df2 / (df3 + df4) - df5')
# r1 = (df1 < df2) & (df2 <= df3) & (df3 != df4)
# r2 = pd.eval('df1 < df2 <= df3 != df4 ')
# print(r1)
# print(r2)
# # compare r1和r2 中每个元素是否均相等
# print(np.allclose(r1, r2))

# r1 = (df1 < 100) & (df2 > 5) | (df3 < df4)
# r2 = pd.eval('(df1 < 100) & (df2 > 5) | (df3 < df4)')

# r1 = df2.T[0] + df3.iloc[1]
# r2 = pd.eval('df2.T[0] + df3.iloc[1]')
# print(r1)
# print(r2)
# # compare r1和r2 中每个元素是否均相等
# print(np.allclose(r1, r2))


# print(df1)
# df1.eval('new_column = a + b -c', inplace=True)
# print(df1)

# print(df1)
# df1.eval('b = a+2', inplace=True)
# print(df1)
# mean = df1.mean(1)
# print(mean)
# r = df1.eval('a - @mean')
# print(r)
# r = df1.query('a<500 | b>500')
# print(r)

print(df1)
c_mean = df1['c'].mean()
print('c_mean:', c_mean)
r = df1.query('a<@c_mean & b<@c_mean')
print(r)
