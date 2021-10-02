'''
需要申请一个大小为 n*(w+1) 的数组，对空间消耗比较多
'''
import numpy as np

items = [2, 2, 4, 10, 4] # [1, 3, 10, 50, 70] -> 60
biggest_weight = 9
n = 5

'''
0   1   2   3   4   5   6   7   8   9
-------------------------------------
1   0   1   0   0   0   0   0   0   0
1   0   1   0   1   0   0   0   0   0
1   0   1   0   1   0   1   0   1   0
1   0   1   0   1   0   1   0   1   0
1   0   1   0   1   0   1   0   1   0
'''

def bag(items, n, biggest_weight):
    state = np.zeros((n, biggest_weight+1), 'uint8')
    state[0][0] = 1
    if items[0] <= biggest_weight:
        state[0][items[0]] = 1

    for i in range(1, n):
        for j in range(biggest_weight):
            if state[i-1][j] == 1:
                state[i][j] = 1
                if j + items[i] <= biggest_weight:
                    state[i][j + items[i]] = 1
    # range(start, stop, step)
    for j in range(biggest_weight, -1, -1):
        if state[n-1][j] == 1:
            return j

print(bag(items, n, biggest_weight))

'''
实际上我们只需要申请一个大小为 w+1 的数组即可，因为每次我们更新完状态的时候，前面的状态也就没用了，我们可以共用一个状态数组。
'''
def bag(items, n, biggest_weight):
    state = [0] * (biggest_weight + 1)
    state[0] = 1

    if items[0] <= biggest_weight:
        state[items[0]] = 1

    for i in range(1, n):
        # 注意这里要倒序遍历
        for j in range(biggest_weight, -1, -1):
            if state[j] == 1:
                if j + items[i] <= biggest_weight:
                    state[j + items[i]] = 1
    for j in range(biggest_weight, -1, -1):
        if state[j] == 1:
            return j

print(bag(items, n, biggest_weight))