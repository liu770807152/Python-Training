'''
暴力求解：每次尝试装入当前数组的第一个物品。如果装得下的话，把背包称重减去该物品的重量；装不下的话，什么都不做。
最后把该物品从数组中剔除，再检查子数组中的其他物品。
一旦发现背包满了，返回True；如果背包一直装不满，返回False。
'''
def subset_sum(w, C):
    # Base case: 能否装满背包，装满返回True，反之返回False
    # Follow up: 如果不要求装满，返回能装入的最大重量？
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
print('暴力解法一的结果：')
print(subset_sum([1, 3, 10, 50, 70], 13))

'''
暴力求解：每次尝试装入当前数组的第一个物品。如果装得下的话，把背包称重减去该物品的重量；装不下的话，什么都不做。
最后把该物品从数组中剔除，再检查子数组中的其他物品。
试着装完所有物品后，返回能装下的最大重量。
'''
def subset_sum_follow_up(w, remain):
    # Base case: 装满背包，或者已经是最后一个物品
    if len(w) == 0 or remain <= 0:
        return remain
    left = right = -1
    # including w[0]
    if w[0] <= remain:
        left = subset_sum_follow_up(w[1:], remain - w[0])
    # excluding w[0]
    right = subset_sum_follow_up(w[1:], remain)
    if left >= 0 and right >= 0:
        return min(left, right)
    else:
        if left > 0:
            return left
        elif right > 0:
            return right
        else:
            return -1
print('暴力解法二的结果：')
print(13 - subset_sum_follow_up([1, 3, 10, 50, 70], 13))