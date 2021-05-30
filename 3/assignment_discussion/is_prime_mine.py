# COMP1730/6730 S1 2021 - Homework 3
# Submission is due 9:00am, Monday the 29th of March, 2021.


import math


# Modify the following function so that it determines whether b is a factor of a
# The statement "return False" is just a placeholder - you should replace it.
def is_factor(a, b):
    return a % b == 0


# Modify the following function definition so that it determines whether
# n is a prime number or not.
# The statement "return False" is just a placeholder - you should replace it.
def is_prime(n):
    if n<=1:
        return False
    #2 and 3 are prime
    elif n == 2 or n == 3:
        return True
    #determine the rest range of n
    for i in range(2, n):
            if n % i == 0:
                return False
    return True


# Modify the following function definition so that it returns the number
# of prime factors of n.
# The statement "return 0" is just a placeholder - you should replace it.
def count_prime_factors(n):
    # 学生思路：
    # step1: 遍历比n小的所有正数
    # step2: 看看这个正数是不是素数，而且能整除n
    # 我的思路：
    # step1: 先找出所有因数
    # step2: 再看看哪些因数是素数
    factors = []
    result = []
    for cur in range(2, n+1):
        if is_factor(n, cur):
            factors.append(cur)
    for factor in factors:
        if factor == 2 or factor % 2 != 0 and is_prime(factor):
            result.append(factor)
    return len(result)

# REMEMBER THAT THIS FILE (WHEN YOU SUBMIT IT) MUST NOT CONTAIN ANYTHING
# OTHER THAN YOUR FUNCTION DEFINITIONS AND COMMENTS.
# YOU MAY NOT IMPORT ANY MODULES OTHER THAN THE 'math' MODULE
