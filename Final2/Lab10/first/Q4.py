def funY(x):
    i = 0
    while i < len(x):
        # 1. 困在0，死循环
        # 2. [1, 2, 3, 4] -> i = 0, 1, 3, 3, 3 ... 死循环
        # 取余运算 -> [0, len(x))
        i = i + x[i] % len(x)
    return i

# 1.
print(funY([0, 2, 3]))
# 2.
print(funY([1, 2, 3, 4]))