'''
不太好的求根方法
'''
def sqrt_test(n):
    guess = n / 2
    while abs(guess ** 2 - n > 1e-6):
        guess = (guess + n / guess) / 2
    return guess

'''
牛顿-拉弗森方法迭代求根
'''
def sqrt(x: int) -> int:
    if x == 0:
        return 0
    C, x0 = float(x), float(x)
    while True:
        xi = 0.5 * (x0 + C / x0)
        if abs(x0 - xi) < 1e-7:
            break
        x0 = xi
    return int(x0)


if __name__ == '__main__':
    '''
    重点：测试
    总的来说，就是试图用极端的输入值让程序报错或行为异常
    '''
    assert (abs(sqrt(4) - 2 <= 1e-6))
    assert (abs(sqrt(10000) - 100 <= 1e-6))
    assert (abs(sqrt(0) == 0))
    try:
        sqrt(-1)
    except ZeroDivisionError:
        print('xxx')
    except Exception:
        print('xxx')