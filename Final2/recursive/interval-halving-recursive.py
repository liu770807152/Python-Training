#!/usr/bin/env python3

import math

def interval_halving(lower, upper):
    ''' solve a function with interval halving algorithm
    lower and upper are the lower bound and upper bound
    for the solution'''
    middle = (lower + upper) / 2
    value = (middle**2)*math.pi - 1
    if abs(value) < 1e-6:
        return middle
    if value < 0:
        return interval_halving(middle, upper)
    else:
        return interval_halving(lower, middle)
    
    