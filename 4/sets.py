s = [1, 1, 2, 2, 3, 4]
# 去除重复
s = set(s)
print(s)

anotherS = {3, 4, 5}
print(s & anotherS)
print(s | anotherS)
print(s - anotherS)

s.remove(1)
s.add(5)
print(s)

for item in s:
    print(item)