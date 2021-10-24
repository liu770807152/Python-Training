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
例题: 计算是否为某个input数字的倍数的数字个数
'''
num = input()
source_list = [0, 5, 8, 6, 7, 31, 2, 45, 125, 97, 54, 77, 68, 98]
#len([cur for cur in source_list if cur % num == 0])

'''
例题：下面一段程序的输出结果是什么? x和y最终的值是什么?
'''
x, y = 0, 0
def func(x, y):
    for x in range(11):
        y = 2 * x + 1
        print(y)
        if y > 7:
            break
    return x, y
print(func(x, y), x, y)
