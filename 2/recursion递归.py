import math

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

print(solve_the_equation())