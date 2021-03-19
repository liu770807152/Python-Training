'''
else中的代码只有当for循环不被break中断才执行
'''
a = [1, 2, 3, 4, 5]
for cur in a:
    if cur == 0:
        break
else:
    print('Did not break out of the loop')

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
