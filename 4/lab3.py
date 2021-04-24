def sqrt(n):
    guess = n / 2
    while abs(guess ** 2 - n > 1e-6):
        guess = (guess + n / guess) / 2
    return guess


if __name__ == '__main__':
    assert(abs(sqrt(4) - 2 <= 1e-6))
    assert(abs(sqrt(10000) - 100 <= 1e-6))
    assert(abs(sqrt(1) - 1 <= 1e-6))
    assert(abs(sqrt(0) == -1))
