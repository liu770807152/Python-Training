import math

'''
求根的递归解法
'''
def solve_the_equation():
    '''
    This function solves the problem of following equation: r^2π = 1.
    Returns the value of r.
    '''
    rhs = 1 / math.pi
    return find_squared_root(rhs, rhs / 2)


def find_squared_root(num, guess):
    '''
    The function uses 牛顿迭代法 to find the squared root of the given number.
    Returns the squared root.
    '''
    if num < 0:
        # fail fast
        return math.nan
    quotient = num / guess
    avg = (quotient + guess) / 2
    # avg ** 2 - num == 0
    if math.fabs(avg ** 2 - num < 1e-15):
        return avg
    else:
        return find_squared_root(num, avg)


'''
纯递归，无优化版本的斐波那契数列求解
'''
def fib(n: int):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


'''
改进算法，加入备忘录，提高递归效率
'''
def fib_with_memo(n: int, mem: dict):
    # base case
    if n <= 1:
        return n
    # use memory
    if n in mem.keys():
        return mem[n]
    first = fib_with_memo(n-1, mem)
    second = fib_with_memo(n-2, mem)
    # update memory
    mem[n - 1] = first
    mem[n - 2] = second
    return first + second


def print_all_sequence(n):
    for i in range(1, n):
        print('纯递归第' + str(i) + '个: ' + str(fib(i)))

def print_all_sequence_with_memo(n):
    for i in range(1, n):
        print('优化后第' + str(i) + '个: ' + str(fib_with_memo(i, {})))


if __name__ == '__main__':
    print(solve_the_equation(), end='\n====================================\n')
    print(print_all_sequence_with_memo(300), end='\n====================================\n')
    print(print_all_sequence(300))
