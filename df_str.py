import pandas as pd
s = pd.Series(['Wu/han', 'shang/Hai', 'None', 5,'chang sha', 'bei jing'])
print(s)
print('----------------------')

# print(s.str.lower())
# print('----------------------')
# print(s.str.len())
# print('----------------------')
# print(s.str.startswith('s'))
# print('----------------------')
# print(s.str.split('/'))


# print(s.str.extract('([A-Za-z]+)'))
# print('----------------------')
# print(s.str.findall(r'^[^AEIOU].*[^aeiou]$'))

# print(s.str[1:3])

# print(s.str.split('/'))
# print('-'*20)
# print(s.str.split('/').str.get(-1))

df = pd.DataFrame({
    'city': s,
    'info': ['b|c|d', 'a|b|c', 'a', 'b', 'a|b', 'c|d']
})
print(df)
print('-'*20)
print(df['info'].str.get_dummies('|'))