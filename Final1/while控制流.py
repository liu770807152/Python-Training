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
while循环大致和for循环一样，但是切记要正确地更新计数器，才能最终跳出循环！
例题：考试有可能给一段错误更新计数器的代码，让同学们找找为什么错了、哪里错了
'''
def func(lst, a, b):
    # 什么情况下会死循环?
    while b > 1:
        lst[a] += 1
        b = b % a
    return lst

def funY(x):
    i = 0
    while i < len(x):
        # 1. 困在0，死循环
        # 2. [1, 2, 3, 4] -> i = 0, 1, 3, 3, 3 ... 死循环
        # 3. 类型导致的数学运算错误，如字符串和小数
        # 取余运算 -> [0, len(x))
        i = i + x[i] % len(x)
    return i

# 1.
#print(funY([0, 2, 3]))
# 2.
print(funY([1, 2, 3, 4]))
# 3.
#print(funY(['a', 'b', 'c']))
#print(funY([1.1, 2.2, 3.3]))
#print(funY([[1.1]]))
#print(funY([(1.1, )]))
#print(funY([{1.1: 1.1}]))