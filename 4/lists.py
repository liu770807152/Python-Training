l = [2, 3, 4, 5]

'''
add
'''
l.append([6])
l.extend([6])
l.insert(0, 1)
print(l)

'''
delete
'''
l.remove(1) # delete the element 1
print(l)
print(l.pop())
print(l.pop(0))
print(l)

'''
check
'''
for i in range(len(l)):
    print(l[i])
for element in l:
    print(element)
for index, element in enumerate(l):
    print(index, element)
print(l[len(l) - 1])

'''
alter
'''
l[0] = 888
print(l)

'''
list 合并
'''
a = [1, 3, 5, 7, 9]
b = [2, 3, 4, 5, 6]
c = [5, 6, 7, 8, 9]
print(list(set().union(a, b, c))) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''
出现次数最多的 2 个字母
'''
from collections import Counter
c = Counter('hello world')
print(c.most_common(2)) #[('l', 3), ('o', 2)]