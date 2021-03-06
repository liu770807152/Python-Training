# Implement the function interval_intersection below.
# You can define other functions if it helps you decompose and solve
# the problem.
# Do not import any module that you do not use!

# Remember that if this were an exam problem, in order to be marked
# this file must meet certain requirements:
# - it must contain ONLY syntactically valid python code (any syntax
#   or indentation error that stops the file from running would result
#   in a mark of zero);
# - you MAY NOT use global variables; the function must use only the
#   input provided to it in its arguments.

'''
Write a function interval_intersection(lA, uA, lB, uB) that returns the length of the intersection of two intervals A and B.
Arguments lA and uA are the lower and upper end points of interval A, and lB and uB are the lower and upper end points of interval B.
If the intervals do not intersect, the function should return 0.

For example, interval_intersection(0, 3, 1, 5) should return 2,
because the intersection of the two intervals [0,3] and [1,5] is [1,3], which has a length of 3 - 1 = 2.
'''
def interval_intersection(lA, uA, lB, uB):
    # 先判断包含关系
    if lA >= lB and uA <= uB:
        return uA - lA
    elif lB >= lA and uB <= uA:
        return uB - lB
    # 再判断相交关系，因为相交关系的条件比较弱
    elif lB < lA < uB:
        return uB - lA
    elif lB < uA < uB:
        return uA - lB
    elif lA < lB < uA:
        return uA - lB
    elif lA < uB < uA:
        return uB - lA
    # 没有交点的情况
    else:
        return 0


def test_interval_intersection():
    """
    This function runs a number of tests of the interval_intersection function.
    If it works ok, you will just see the output ("all tests passed") at
    the end when you call this function; if some test fails, there will
    be an error message.
    """

    assert interval_intersection(0, 2, 4, 7.5) == 0.0, "no intersection (uA < lB)"
    assert interval_intersection(1, 3, 2.5, 6) == 0.5, "intersection is [2.5, 3]"
    assert interval_intersection(1, 3, 1.5, 5) == 1.5, "intersection is [1.5, 3]"
    assert interval_intersection(0, 2, -2, 1.5) == 1.5, "intersection is [0, 1.5]"
    assert interval_intersection(1, 3, 0, 3.5) == 2.0, "A is contained in B"
    assert interval_intersection(1.5, 3.5, 0, 3.5) == 2.0, "A is contained in B"

    print("all tests passed")

test_interval_intersection()