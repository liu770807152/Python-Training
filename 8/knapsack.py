import numpy as np

'''
暴力求解：每次尝试装入当前数组的第一个物品。如果装得下的话，把背包称重减去该物品的重量；装不下的话，什么都不做。
最后把该物品从数组中剔除，再检查子数组中的其他物品。
一旦发现背包满了，返回True；如果背包一直装不满，返回False。
'''
def subset_sum(w, C):
    # Base case: 能否装满背包，装满返回True，反之返回False
    # Follow up: 如果不要求装满，而是尽可能地装多点呢？
    if len(w) == 0:
        return C == 0
    # including w[0]
    if w[0] <= C:
        if subset_sum(w[1:], C - w[0]):
            return True
    # excluding w[0]
    if subset_sum(w[1:], C):
        return True
    return False

'''
暴力求解：每次尝试装入当前数组的第一个物品。如果装得下的话，把背包称重减去该物品的重量；装不下的话，什么都不做。
最后把该物品从数组中剔除，再检查子数组中的其他物品。
试着装完所有物品后，返回能装下的最大重量。
'''
def subset_sum_follow_up(w, remain):
    # Base case: 装满背包，或者已经是最后一个物品
    if len(w) == 0 or remain <= 0:
        return remain
    temp1 = temp2 = -1
    # including w[0]
    if w[0] <= remain:
        temp1 = subset_sum_follow_up(w[1:], remain - w[0])
    # excluding w[0]
    temp2 = subset_sum_follow_up(w[1:], remain)
    if temp1 >= 0 and temp2 >= 0:
        return min(temp1, temp2)
    else:
        if temp1 > 0:
            return temp1
        elif temp2 > 0:
            return temp2
        else:
            return -1
print('暴力解法二的结果：')
print(13 - subset_sum_follow_up([1, 3, 10, 50, 70], 13))

'''
动态规划：记录之前装入的物品重量，每次遇到一个物品作出抉择：装入或者不装入。装入则更新记录，不装入则不更新。
需要申请一个大小为 n*(w+1) 的数组，对空间消耗比较多
'''
items = [2, 2, 4, 10, 4]
biggest_weight = 9
n = 5

'''
纵坐标是物品，横坐标是背包载重
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
print('动态规划解法一的结果：')
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
print('动态规划解法二的结果：')
print(bag(items, n, biggest_weight))