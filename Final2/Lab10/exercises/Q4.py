'''
Give an example, if possible, of an argument sequence that causes funY to get stuck in an infinite loop,
as well as an argument sequence for which the function executes without error and returns a value.
'''
def funY(x):
    i = 0
    while i < len(x):
        # 1. 困在0，死循环
        # 2. [1, 2, 3, 4] -> i = 0, 1, 3, 3, 3 ... 死循环
        # 3. 类型导致的数学运算错误，如字符串和小数
        # 取余运算 -> [0, len(x))
        i = i + x[i] % len(x)
    return i

print(funY([1, 2, 3]))

# 1. get stuck in an infinite loop,
#print(funY([0, 2, 3]))
#print(funY([1, 2, 3, 4]))
# 2. executes without error and returns a value
#print(funY([1, 2, 3]))
# 3. executes with error
#print(funY(['a', 'b', 'c']))
#print(funY([1.1, 2.2, 3.3]))
#print(funY([[1.1]]))
#print(funY([(1.1, )]))
#print(funY([{1.1: 1.1}]))