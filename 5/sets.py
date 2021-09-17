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

s.remove(1)
s.add(5)
print(s)

for item in s:
    print(item)
