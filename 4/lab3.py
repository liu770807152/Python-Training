def sqrt_test(n):
    guess = n / 2
    while abs(guess ** 2 - n > 1e-6):
        guess = (guess + n / guess) / 2
    return guess


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
    assert(abs(sqrt(4) - 2 <= 1e-6))
    assert(abs(sqrt(10000) - 100 <= 1e-6))
    assert(abs(sqrt(1) - 1 <= 1e-6))
    assert(abs(sqrt(0) == 0))
