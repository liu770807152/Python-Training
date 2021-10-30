import math
import numpy as np
# 对于所有递归算法，一定有三要素：
# 1. base case
# 2. 递归函数的调用
# 3. 状态的更新


def is_palindromic(num):
    '''
    判断一个字符串是不是回文字符串
    '''
    # 如果字符串只有0个或1个字符，那么该字符串符合回文的定义
    if len(num) < 2:
        return True
    # 如果字符串不止一个字符，那么检查字串符的第一项和最后一项是否等同
    if num[0] != num[-1]:  
        return False
    return is_palindromic(num[1: -1])


def bi_search(min, max, data, target):
    '''
    二分法查找某个元素
    使用二分法的前提是：查找的序列必须有序！！！
    '''
    '''
    min表示有序列表头部索引
    max表示有序列表尾部索引
    data表示有序列表
    target表示要搜索的元素
    [1, 2, 3, 4, 5] 3 -> [1, 2] 1 -> [2]
    '''
    mid = (min + max) // 2
    # base case 1: 要找的数刚好是当前区间中间的数
    if data[mid] == target:
        print(f'找到了{data[mid]}, 在下标{mid}！')
        return True
    # base case 2: 区间没有数
    if min > max:
        print(f'没找到！')
        return False
    # 2 & 3.
    elif data[mid] < target:
        print('向右侧找！')
        print(f'min={min}, mid={mid}, max={max}')
        return bi_search(mid+1, max, data, target)
    elif data[mid] > target:
        print('向左侧找！')
        print(f'min={min}, mid={mid}, max={max}')
        return bi_search(min, mid-1, data, target)


'''
Longest Increasing Subsequence
输入: nums = [1, 5, 2, 4, 3]
输出: 3
解释: 最长递增子序列是 [1, 2, 4/3]，它的长度是 3
'''
# 递归法，无优化，存在重复计算
def LIS(nums, i) -> int:
    # 遍历到最后一个数了，返回base case
    if i == len(nums) - 1:
        return 1

    max_len = 1
    for j in range(i + 1, len(nums)):
        # 判断能否组成increasing subsequence
        if nums[j]> nums[i]:
            # 如果可以组成，能否组成更长的increasing subsequence
            max_len = max(max_len, LIS(nums, j) + 1)
    return max_len


''' 优化：加个备忘录，记录下"从i开始最长的子序列长度" '''
def LIS_optimized(nums, i, memo) -> int:
    # 遍历到最后一个数了，返回base case
    if i == len(nums) - 1:
        return 1
    if i in memo:
        return memo[i]

    max_len = 1
    for j in range(i + 1, len(nums)):
        if nums[j] > nums[i]:
            max_len = max(max_len, LIS(nums, j) + 1)
    memo[i] = max_len
    return max_len


def length_of_LIS(nums):
    max_len1 = 0
    max_len2 = 0
    for i in range(len(nums)):
        max_len1 = max(max_len1, LIS(nums, i))
        max_len2 = max(max_len2, LIS_optimized(nums, i, {}))
    return max_len1, max_len2


'''
问题：偷取商店里的若干个物品，求背包能装下的最重重量
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
    # print(w, temp1, temp2)
    if temp1 >= 0 and temp2 >= 0:
        return min(temp1, temp2)
    else:
        if temp1 > 0:
            return temp1
        elif temp2 > 0:
            return temp2
        else:
            return -1


'''
问题：偷取商店里的若干个物品，求背包能装下的最重重量
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


'''
问题：偷取商店里的若干个物品，求背包能装下的最重重量
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


'''
0-1背包问题的递归解法很难
'''
def knapsack(items, i, biggest_weight, memo):
    # 递归到了最后一个物品，如果装得下，返回base case，即该物品重量
    if i == len(items) - 1:
        return items[i] if items[i] < biggest_weight else 0
    # 如果此前已经计算过当前位置的最大重量，直接返回
    elif memo[i]:
        return memo[i]

    # 记录当前物品的重量
    current_weight = items[i]
    for j in range(i + 1, len(items)):
        # 存储往后物品的最大重量
        next_max = knapsack(items, j, biggest_weight, memo)
        # 当前物品装得下，才考虑怎么装的问题
        if current_weight < biggest_weight:
            # 1. 该循环主要考虑能正好装满背包的情况
            for key, weight in memo.items():
                if key >= j and current_weight + weight == biggest_weight:
                    memo[i] = biggest_weight
                    break
            # 2. 如果无法装满，再看看当前位置要怎么装?
            #   a. 如果当前物品重量 + 往后物品最大重量 < 背包允许重量，则一起装
            #   b. 如果当前物品重量 + 往后物品最大重量 > 背包允许重量，则只能择其一：要么装当前物品，要么装往后物品的最大
            else:
                if current_weight + next_max < biggest_weight:
                    memo[i] = max(memo[i], current_weight + next_max)
                else:
                    memo[i] = max(memo[i], max(current_weight, next_max))
    # 每次递归都返回当前求得的最大重量
    return memo[i]


def max_of_knapsack(items, biggest_weight):
    max_weight = 0
    record = {}
    for i in range(len(items)):
        record[i] = 0
    for i in range(len(items)):
        max_weight = max(max_weight, knapsack(items, i, biggest_weight, record))
    return max_weight


if __name__ == '__main__':
    print(f"number is 123321, check if it\'s palindromic: {is_palindromic('123321')}")
    print(f"number is 123320, check if it\'s palindromic: {is_palindromic('123320')}")
    print('================================================')
    data = [1, 3, 6, 13, 56, 123, 345, 1024, 3223, 6688]
    print(f'data is {data}, search for 6: {bi_search(0, len(data), data, 6)}', end='\n================================================\n')
    print(f'data is {data}, search for 7: {bi_search(0, len(data), data, 7)}')
    print('================================================')
    print(f'suquence is {[1, 5, 2, 4, 3]}, LIS is: {length_of_LIS([1, 5, 2, 4, 3])}')
    print('================================================')
    print(f'关于0-1背包问题，物品列表是: {[1, 3]}')
    print('暴力解法的结果：')
    print(4 - subset_sum_follow_up([1, 3], 4))
    print('================================================')
    print(f'关于0-1背包问题，物品列表是: {[1, 3, 4, 8, 10, 3]}')
    print('暴力解法的结果：')
    print(9 - subset_sum_follow_up([1, 3, 4, 8, 10, 3], 9))
    print('动态规划解法一的结果：')
    print(bag([1, 3, 4, 8, 10, 3], len([1, 3, 4, 8, 10, 3]), 9))
    print('动态规划解法二的结果：')
    print(bag([1, 3, 4, 8, 10, 3], len([1, 3, 4, 8, 10, 3]), 9))
    print(f'最大载重是: 9, 递归解法求得结果是: {max_of_knapsack([1, 3, 4, 8, 10, 3], 9)}')
    print(f'最大载重是: 2, 递归解法求得结果是: {max_of_knapsack([1, 3, 4, 8, 10, 3], 2)}')
    print('================================================')
    print(f'物品列表换成: {[2, 3, 5, 7, 9]}')
    print('暴力解法的结果：')
    print(25 - subset_sum_follow_up([2, 3, 5, 7, 9], 25))
    print('动态规划解法一的结果：')
    print(bag([2, 3, 5, 7, 9], len([2, 3, 5, 7, 9]), 25))
    print('动态规划解法二的结果：')
    print(bag([2, 3, 5, 7, 9], len([2, 3, 5, 7, 9]), 25))
    print(f'递归解法求得结果是: {max_of_knapsack([2, 3, 5, 7, 9], 25)}')
    # print(f'物品列表是: {[2, 2, 3, 7]}, 最大载重是: 6, 递归解法求得结果是: {max_of_knapsack([2, 2, 3, 7], 6)}')



