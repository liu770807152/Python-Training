import time
def timeit(f):
    def timed(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        print('func:%r args:[%r, %r] took: %.20f sec' % \
          (f.__name__, args, kw, te-ts))
        return result
    return timed

'''
还记得我吗？
'''
def fib(n: int):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
@timeit
def printAllSequence(n):
    for i in range(n):
        print(i, fib(i))
print(printAllSequence(30), end='\n\n')

'''
不用动态规划，能不能改进算法效率？我们可以利用cache！
'''
from functools import cache, lru_cache
# @cache
# 缓存fib()最近五次运行的结果，存放于cache中
@lru_cache(maxsize=30)
def fib(n: int):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
print(printAllSequence(1000), end='\n\n')