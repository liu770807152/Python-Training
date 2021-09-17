# 对于所有递归算法，一定有三要素：
# 1. base case
# 2. 递归函数的调用
# 3. 状态的更新

'''
判断一个字符串是不是回文字符串
'''
def is_palindromic(num):
    # 如果字符串只有0个或1个字符，那么该字符串符合回文的定义
    if len(num) < 2:
        return True
    # 如果字符串不止一个字符，那么检查字串符的第一项和最后一项是否等同
    if num[0] != num[-1]:  
        return False
    return is_palindromic(num[1: -1])

'''
二分法查找某个元素
使用二分法的前提是：查找的序列必须有序！！！
'''
def bi_search(min, max, data, num):
    '''
    min表示有序列表头部索引
    max表示有序列表尾部索引
    data表示有序列表
    num表示需要寻找的元素
    '''
    mid = (min + max) // 2
    # base case: 没有找到
    if mid == 0:
        return False
    # 2 & 3.
    elif data[mid] < num:
        print('向右侧找！')
        return bi_search(mid, max, data, num)
    elif data[mid] > num:
        print('向左侧找！')
        return bi_search(min, mid, data, num)
    # base case: 找到了
    else:
        print(f'找到了{data[mid]}')
        return True

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


# 优化：加个备忘录，记录下"从i开始最长的子序列长度"
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
    # return max(LIS(nums, i) for i in range(len(nums)))

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
    print(f'data is {data}, search for 3: {bi_search(0, len(data), data, 3)}')
    print('================================================')
    print(f'suquence is {[1, 5, 2, 4, 3]}, LIS is: {length_of_LIS([1, 5, 2, 4, 3])}')
    print('================================================')
    print(f'weights of commodities are {[1, 3, 4, 8, 10, 3]}, biggest weight is 9, and the result of knapsack is {max_of_knapsack([1, 3, 4, 8, 10, 3], 9)}')
    print(f'weights of commodities are {[1, 3, 4, 8, 10, 3]}, biggest weight is 2, and the result of knapsack is {max_of_knapsack([1, 3, 4, 8, 10, 3], 2)}')
    print(f'weights of commodities are {[2, 2, 3, 7]}, biggest weight is 6, and the result of knapsack is {max_of_knapsack([2, 2, 3, 7], 6)}')
    print(f'weights of commodities are {[2, 3, 5, 7, 9]}, biggest weight is 25, and the result of knapsack is {max_of_knapsack([2, 3, 5, 7, 9], 25)}')




