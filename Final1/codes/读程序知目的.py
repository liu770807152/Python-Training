#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fun1(s, k):
    ''''''
    i = 0
    while i + k < len(s):
        sub = s[i : i+k]
        if s[i+1:].find(sub) != -1:
            return sub
        i = i+1
    return None


def fun2(s):
    '''  '''
    k = 1
    longest = ''
    while k < len(s):
        sub = fun1(s, k)
        if sub is not None:
            longest = sub
        k = k+1
    return longest