def get_depth(a_list):
    # base case
    if type(a_list) != list:
        return 0
    if a_list == []:
        return 1
    # 用于存储当前层的所有深度值
    all_depths = []
    # 递归地存储当前层的所有深度值
    for cur in a_list:
        all_depths.append(get_depth(cur))
    # 返回当前层的最大深度值，如果当前list中全是数字会返回0，记得加1
    return max(all_depths) + 1


def nesting_depth(l):
    # 因为最外层的深度算作0，所以算法多加了1，要减去
    return get_depth(l) - 1


if __name__ == '__main__':
    assert (nesting_depth([[1, 2], [3, 4]]) == 1)
    assert (nesting_depth([1, [2], [[3], [[4], 5]]]) == 3)
    assert (nesting_depth([[[]]]) == 2)