s = [2, 1, 4, 3, 2, 1]
# 去除重复
s = set(s)
print(s)

anotherS = {3, 4, 5}
# 交集∩
print(s & anotherS)
# 并集∪
print(s | anotherS)
# 差集
print(s - anotherS)
# 对称差集：先并再减
print(s.symmetric_difference(anotherS))

s.remove(1)
s.add(5)
print(s)

for item in s:
    print(item)

'''
例题：求多个集合的交集
'''
print('======================================')
set1 = {1, 6, 3, 7}
set2 = {8, 4, 3, 0}
set3 = {0, 7, 9, 3}
print(set1 & set2 & set3)