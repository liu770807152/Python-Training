'''
Explain what funX does in general. A good answer is one that describes the purpose of the function - something you would write in its docstring.
'''
def funX(a_list):
    '''
    1. a_list会被排序
    2. 取中间的元素
    '''
    index = 0 # O(1)
    while index < len(sorted(a_list)) // 2: # O(nlog(n) * n)
        index = index + 1 # O(1)
    return sorted(a_list)[index] # O(nlog(n))

print(funX([3, 2, 1, 0, -1]))


'''
funX is unnecessarily inefficient. Rewrite the function so that it does the same thing, but as efficiently as possible.
'''
def new_funX(a_list):
    # 位运算直接得出目标index
    # 4 // 2 -> 2                   5 // 2 -> 2
    # 0100 -> 0010 -> 2^1 = 2     0101 -> 0010 -> 2
    return sorted(a_list)[len(a_list) >> 1] # O(nlog(n) * 1)

print(new_funX([3, 2, 1, 0, -1]))