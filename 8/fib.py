import time
def timeit(f):
    def timed(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        #print('func:%r args:[%r, %r] took: %.20f sec' % \
        # (f.__name__, args, kw, te-ts))
        print('func:%r took: %.20f sec' % \
              (f.__name__, te - ts))
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
printAllSequence(30)

'''
改进算法，加入备忘
'''
def fib(n: int, mem: dict):
    # base case
    if n <= 1:
        return n
    # use memory
    if n in mem.keys():
        return mem[n]
    first = fib(n-1, mem)
    second = fib(n-2, mem)
    # update memory
    mem[n - 1] = first
    mem[n - 2] = second
    return first + second
@timeit
def printAllWithMemory(n: int, mem: dict):
    for i in range(n):
        print(i, fib(i, mem))
printAllWithMemory(200, {1: 1})
print('Done!')