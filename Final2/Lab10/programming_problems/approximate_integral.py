# Implement the function approximate_integral below.
# (The statement "pass" is just a placeholder that does nothing: you
# should replace it.)
# You can define other functions if it helps you decompose and solve
# the problem.
# Do not import any module that you do not use!

# Remember that if this were an exam problem, in order to be marked
# this file must meet certain requirements:
# - it must contain ONLY syntactically valid python code (any syntax
#   or indentation error that stops the file from running would result
#   in a mark of zero);
# - you MAY NOT use global variables; the function must use only the
#   input provided to it in its arguments.


'''
Let f(x) be the function that we want to integrate. The area of the trapezoid over the interval [x,x+d] is ((f(x) + f(x + d)) / 2) * d.
Write a function approximate_intergral(lower, upper, nterms)
that calculates an approximation of the integral of the function f(x) = x3 (that is, x cubed) over a bounded interval using the trapezoid method.

For example, approximate_integral(0, 2, 2) should return 5.
The first trapezoid is over the interval [0,1] and has an area of 0.5 (((0 + 1) / 2) * 1);
the second is over the interval [1,2] and has an area of 4.5 (((1 + 8) / 2) * 1).
'''
def approximate_integral(lower, upper, nterms):
    partition = (upper - lower) / nterms
    sum = 0
    for _ in range(nterms):
        sum += get_area(lower, lower + partition, partition)
        lower += partition
    return sum


def get_area(first, second, d):
    # ((f(x) + f(x + d)) / 2) * d.
    return (first ** 3 + second ** 3) / 2 * d


def test_approximate_integral():
    """
    This function runs a number of tests of the approximate_integral function.
    If it works ok, you will just see the output ("all tests passed") at
    the end when you call this function; if some test fails, there will
    be an error message.
    """
    
    assert abs(approximate_integral(0, 1, 1) - 0.5) < 1e-6, 'sum of 0.5'
    assert abs(approximate_integral(1, 2, 1) - 4.5) < 1e-6, 'sum of 4.5'
    assert abs(approximate_integral(0, 2, 1) - 8.0) < 1e-6, 'sum of 8.0'
    assert abs(approximate_integral(0, 1, 2) - 0.3125) < 1e-6, 'sum of 0.03125, 0.28125'
    assert abs(approximate_integral(1, 2, 2) - 3.9375) < 1e-6, 'sum of 1.09375, 2.84375'
    assert abs(approximate_integral(0, 2, 2) - 5.0) < 1e-6, 'sum of 0.5, 4.5'
    assert abs(approximate_integral(0, 1, 5) - 0.26) < 1e-6, 'sum of 0.0008000000000000003, 0.007200000000000002, 0.028000000000000014, 0.07280000000000002, 0.1512'
    assert abs(approximate_integral(1, 2, 5) - 3.7799999999999994) < 1e-6, 'sum of 0.2728, 0.4472, 0.6839999999999998, 0.9927999999999998, 1.3831999999999995'
    assert abs(approximate_integral(0, 2, 5) - 4.16) < 1e-6, 'sum of 0.012800000000000004, 0.11520000000000004, 0.44800000000000023, 1.1648000000000003, 2.4192'

    assert abs(approximate_integral(-1, 0, 1) - -0.5) < 1e-6, 'sum of -0.5'
    assert abs(approximate_integral(-2, -1, 1) - -4.5) < 1e-6, 'sum of -4.5'
    assert abs(approximate_integral(-2, 0, 1) - -8.0) < 1e-6, 'sum of -8.0'
    assert abs(approximate_integral(-1, 0, 2) - -0.3125) < 1e-6, 'sum of -0.28125, -0.03125'
    assert abs(approximate_integral(-2, -1, 2) - -3.9375) < 1e-6, 'sum of -2.84375, -1.09375'
    assert abs(approximate_integral(-2, 0, 2) - -5.0) < 1e-6, 'sum of -4.5, -0.5'
    assert abs(approximate_integral(-1, 0, 5) - -0.260) < 1e-6, 'sum of -0.1512, -0.07280, -0.0280, -0.00720, -0.00080'
    assert abs(approximate_integral(-2, -1, 5) - -3.780) < 1e-6, 'sum of -1.38320, -0.99280, -0.6840, -0.44720, -0.27280'
    assert abs(approximate_integral(-2, 0, 5) - -4.160) < 1e-6, 'sum of -2.4192, -1.16480, -0.4480, -0.11520, -0.01280'

    assert abs(approximate_integral(-1, 1, 1) - 0.0) < 1e-6, 'sum of 0.0'
    assert abs(approximate_integral(-1, 1, 2) - 0.0) < 1e-6, 'sum of -0.5, 0.5'
    assert abs(approximate_integral(-1, 1, 4) - 0.0) < 1e-6, 'sum of -0.28125, -0.03125, 0.03125, 0.28125'
    assert abs(approximate_integral(-2, 2, 1) - 0.0) < 1e-6, 'sum of 0.0'
    assert abs(approximate_integral(-2, 2, 2) - 0.0) < 1e-6, 'sum of -8.0, 8.0'
    assert abs(approximate_integral(-2, 2, 4) - 0.0) < 1e-6, 'sum of -4.5, -0.5, 0.5, 4.5'

    print("all tests passed")

test_approximate_integral()