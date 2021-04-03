# list可以存储不同类型的对象
a = [1, True, (1, 2), [], {}, set(), "haha"]
print(a)

# list的增加和删除
a.append('new')
a.insert(0, 0)
print(a)
a.remove(0) # 把0这个元素移除
a.pop(0) # 把第1个元素移除
print(a)