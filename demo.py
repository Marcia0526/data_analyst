import numpy as np

# a = [1, 'hello', 'world', 9, 10, 8, 5, 3, 6, 7]
# print(a)
# a.append('2w')
# print(a)
# print(a.pop())
# a.remove('hello')
# print(a)
# print(a[0])
# print(a[2:4]) #左闭右开：a[2],a[3]
# print(a[2:6:2]) #第三个参数为步长：a[2],a[4]
# print(a[::-1]) #倒序输出
# print(a+a) #列表合并
# a[4:]=[1,2,3,3] #a[4]之后的元素都被替换成[1,2,3,3
# print(a)


# a = (1, [1, 'n'], 3, 'hello')
# print(type(a))
# print(a)
# print(a[1:3])


a = np.array([1,2,3,4,5,6])
print(a)
print(a[1])
print(a[:3:2]) #第一个到第四个元素，左闭右开，步长为2：第一，第三个元素：[1 3]

b = np.array([[1, 2, 3], [4, 5, 6],[7,8,9]])
print(b)
print(b[1, 1])
print(b[2][1])
print(b[0:2, 1:2])

