'''
Iterable对象的迭代器iterator
'''
l = [11, 22, 33]
# 1. 通过iter函数获取迭代器，并用next()进行迭代
it = iter(l)
print(next(it))
print(next(it))
print(next(it))

# 2. iter()的本质就是__iter__()这一内部函数，而next()的本质是__next__()这一内部函数
it = l.__iter__()
print(it.__next__())
print(it.__next__())
print(it.__next__())

print('=============================================')

'''
reversed函数(不建议使用)
'''
lst = ["胡辣汤", "三德子", "法印"]
r = reversed(lst)  # 把列表翻转. 返回迭代器
print(r)
print(r.__next__())
print(r.__next__())
print(r.__next__())
print(lst) # 原列表不变

lst.reverse()
print(lst) # 原列表改变
print('=============================================')

'''
sorted函数
'''
lst = [13, 28, 1, 36, 17, 58]
res = sorted(lst, reverse=True)
print(res)

# 需要自己去定义排序规则，根据名字的长度进行排序
lst = ["赵本山", "斯琴高娃", "周杰", "丁俊晖"]
res = sorted(lst, key=lambda item: len(item))
print(res)

# 按照年龄对学生信息进行排序
lst = [{"id": 1, "name": '盖伦', "age": 18},
       {"id": 2, "name": '杰斯', "age": 16},
       {"id": 3, "name": '压缩', "age": 17}]
print(sorted(lst, key=lambda dic: dic['age'], reverse=True))

print('=============================================')

'''
random类
'''
# 生成一个范围内的整数(左闭右开)，可以帮我们生成验证码
import random
n = random.randint(65, 92)  # 大写英文字母对应的ascii
print(chr(n))

# 生成[0, 1)之间的一个float类型数字
for _ in range(5):
    n = random.random()
    print(n)
    # 我们也可以缩放[0, 1)这一范围至[0, n)，这里以10为例
    print(int(n * 10))

# 随机选取一个容器内的元素
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(5):
    print(f'{i}: {random.choice(lst)}')

print('=============================================')

'''
zip()与dir()

The dir() function returns all properties and methods of the specified object, without the values.
This function will return all the properties and methods, even built-in properties which are default for all object.

The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, 
and then the second item in each passed iterator are paired together etc.
'''
lst1 = ["赵本山", "苏有朋", '']
print(dir(lst1))
print("__iter__" in dir(lst1))
lst2 = ["马大帅", "情深深雨蒙蒙", "情深深雨蒙蒙"]
lst3 = ['马大帅', "啊飞", "小男孩"]

a = zip(lst1, lst2, lst3)
for item in a:
    print(item)
print('=============================')
lst1 = ["胡辣汤", "疙瘩汤", "紫菜蛋花汤"]
lst2 = ["我喜欢吃", "我更喜欢吃", "我不喜欢吃"]
# 可以快速构建字典. 记住
d = dict(zip(lst1, lst2))
print(d)
print('=============================================')


'''
The map() function executes a specified function for each item in an iterable. 
The item is sent to the function as a parameter.
'''
# 让列表中的每一个数字都增加1
lst = [18, 22, 17, 5, 9]
m = map(lambda x: x + 1, lst)
print(list(m))
# 等效于
lst2 = [item+1 for item in lst]
print(lst2)

print('=============================================')

'''
The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.
'''
# 把能被3整除的数摘出来
lst = [7, 21, 3, 46, 61, 3, 5]
f = filter(lambda x: x % 3 == 0, lst)
print(list(f))