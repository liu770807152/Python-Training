def funX(a_list):
    '''
    1. a_list会被排序
    2. 取中间的元素
    '''
    index = 0
    # O(nlogn)
    while index < len(sorted(a_list)) // 2:
        index = index + 1
    return sorted(a_list)[index]

print(funX([3, 2, 1, 0, -1]))

# 第一次取最小的数，第二次取第二小的数...第N次(N = len(a_list) // 2)取第N小的数 ... 第K次取最大的数
# O(N) ->  N // 2 * O(N) -> O(N^2)


def new_funX(a_list):
    # 位运算直接得出目标index
    # 4 // 2 -> 2                   5 // 2 -> 2
    # 0100 -> 0010 -> 2^1 = 2     0101 -> 0010 -> 2
    return sorted(a_list)[len(a_list) >> 1]

print(new_funX([3, 2, 1, 0, -1]))