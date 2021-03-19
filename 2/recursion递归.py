import math

def solveTheEquation():
    '''
    This function solves the problem of following equation: r^2π = 1.
    Returns the value of r.
    '''
    rhs = 1 / math.pi
    return findSquaredRoot(rhs, rhs / 2)

def findSquaredRoot(num, guess):
    '''
    The function uses 牛顿迭代法 to find the squared root of the given number.
    Returns the squared root.
    '''
    if num < 0:
        # fail fast
        return math.nan
    quotient = num / guess
    avg = (quotient + guess) / 2
    if math.fabs(avg ** 2 - num < 1e-15):
        return avg
    else:
        return findSquaredRoot(num, avg)

print(solveTheEquation())