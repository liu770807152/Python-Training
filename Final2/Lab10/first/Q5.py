def smallest_non_negative(number_list):
    '''Argument is a list of numeric values (integer or float).
    Returns the smallest non-negative value in the list,
    and zero if there is no such value.'''
    pass



assert smallest_non_negative([]) == 0
assert smallest_non_negative([-1.0, -2.2, -3.3]) == 0
assert smallest_non_negative([1, 2, 3]) == 1
assert smallest_non_negative([-1.1, 0, 1]) == 0