'''
while循环语法
'''
i = 0
while i < 10:
    print(i)
    i += 1
else:  # else中的代码只有当循环不被break中断才执行
    print("OK!")

'''
for循环语法
'''
for i in range(10):
    print(i)
    i += 1
else:  # else中的代码只有当循环不被break中断才执行
    print("OK!")

print('=============================================================================================')

'''
例题: 检查一个list里是否有0。如果有，打印它的下标; 如果没有，则打印"No zero inside the list!"。
'''
a = [1, 2, 0, 4, 5]
# while循环
index = 0
while index < 5:
    if a[index] == 0:
        print(index)
        break
    index += 1
else:
    print('No zero inside the list!')

# for循环
for cur in a:
    if cur == 0:
        # 找不到index下标，怎么办?
        break
else:
    print('No zero inside the list!')

# for循环 + enumerate
# 切记: index下标在前，元素在后！
for index, cur in enumerate(a):
    if cur == 0:
        print(index)
        break
else:
    print('No zero inside the list!')

print('=============================================================================================')

'''
我们经常会如下这种嵌套的 for 循环代码
list1 = range(1,3)
list2 = range(4,6)
list3 = range(7,9)
for item1 in list1:
    for item2 in list2:
       for item3 in list3:
           print(item1+item2+item3)
           
这样的代码，可读性非常的差，很多人不想这么写，可又没有更好的写法。
这里介绍一种我常用的写法，使用 itertools 这个库来实现更优雅易读的代码。
'''
from itertools import product
list1 = range(1,3)
list2 = range(4,6)
list3 = range(7,9)
for item1,item2,item3 in product(list1, list2, list3):
    print(item1+item2+item3)
