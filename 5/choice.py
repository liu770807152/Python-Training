def choices(n, k):
    '''
    Return the number of ways to choose k elements from a set of n.
    Assumptions: n and k are non-negative integers, with n >= k.
    '''
    if k == n or k == 0:
        return 1
    else:
        return choices(n - 1, k) + choices(n - 1, k - 1)

if __name__ == '__main__':
    assert(choices(30, 1) == 30)