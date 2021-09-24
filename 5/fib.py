def fib(n: int):
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)
def printAllSequence(n):
    for i in range(n):
        print(i, fib(i))

if __name__ == '__main__':
    print(printAllSequence(30))