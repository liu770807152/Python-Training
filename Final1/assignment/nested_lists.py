def nested_depth(l):
    def check(a_list, depth=0):
        cur_depth = depth
        for element in a_list:
            if type(element) == list:
               cur_depth = max(cur_depth, check(element, depth+1))
        return cur_depth
    return check(l)


def depth(a_list):
    if type(a_list) != list:
        return 0
    if not a_list:
        return 1
    return (max(depth(a_list[0]) + 1, depth(a_list[1:])))


def nesting_depth(a_list):
    return depth(a_list) - 1


if __name__ == '__main__':
    assert (nested_depth([[1, 2], [3, 4]]) == 1)
    assert (nested_depth([1, [2], [[3], [[4], 5]]]) == 3)
    assert (nested_depth([[[]]]) == 2)
    print(nesting_depth(depth([[1, 2], [3, 4]])))