l = [2, 3, 4, 5]
print('=================add=================')
'''
add
'''
l.append([6])
l.extend([6])
l.insert(0, 1)
print(l)
print('=================delete=================')
'''
delete
'''
l.remove(1) # delete the element 1
print(l)
print(l.pop())
print(l.pop(0))
print(l)
print('=================search=================')
'''
search
'''
for i in range(len(l)):
    print(l[i])
for element in l:
    print(element)
for index, element in enumerate(l):
    print(index, element)
print(l[len(l) - 1])  # print(l[-1])
# print(l[-100])
print('===============alter===================')
'''
alter
'''
l[0] = 888
print(l)
print('================merge==================')
'''
list 合并
'''
# list内的元素不重复时
a = [1, 3, 5]
b = [2, 4, 6]
print(a + b)
print('===============')
import numpy as np
a = np.array([1, 3, 5])
b = np.array([2, 4, 6])
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print('===============')
# list内的元素有重复时
a = [1, 3, 5, 7, 9]
b = [2, 3, 4, 5, 6]
c = [5, 6, 7, 8, 9]
print(list(set().union(a, b, c))) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('================counter==================')
'''
出现次数最多的 2 个字母
'''
from collections import Counter
c = Counter('hello world')
print(c.most_common(2)) #[('l', 3), ('o', 2)]
print('================hard part==================')
'''
难点的代码
'''
# 1
a_list = [1, 2, 3]
b_list = a_list
a_list.append(4)
print(b_list)

# 2
a_list = [[1, 2], [3, 4]]
b_list = a_list[:]
a_list[0].reverse()
b_list.reverse()
print(b_list)

# 3
a_list = [[1, 2], [3, 4]]
b_list = a_list[:]
a_list[0] = a_list[0][::-1]
b_list.reverse()
print(b_list)

# 4
a_list = [1, 2, 3]
b_list = [4, 5, 6]
a_list.append(b_list)
c_list = a_list[:]
b_list[0] = 'A'
print(c_list)